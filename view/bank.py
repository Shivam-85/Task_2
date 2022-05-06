from flask import Response, request, Flask
from flask_restful import Resource
from models.models import Account, Admin, User
from flask_httpauth import HTTPBasicAuth
import json
from urls.errors import *

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    if not (email and password):
        return False
    ad = Admin.objects().to_json()
    res = json.loads(ad)
    for i in range(len(res)):
        if any(email == res[i]["email"] and password == res[i]["password"] for d in res):
            return True
        else:
            return False


class GetAllAccounts(Resource):
    def get(self):
        accounts = Account.objects().to_json()
        return Response(accounts, mimetype="application/json", status=200)


class OpenAccount(Resource):
    def get(self):
        Acc = Account.objects().to_json()
        return Response(Acc, mimetype="application/json", status=200)

    @auth.login_required()
    def post(self):
        try:
            body = request.get_json(force=True)
            Acc = Account(**body).save()
            response = Acc.id
            return {'id': str(response)}, 200
        except Exception as e:
            raise AccountModificationError("Account already exists!")


class DeleteAndUpdateAccount(Resource):
    @auth.login_required()
    def delete(self, id):
        try:
            Acc = Account.objects.get(phone=id).delete()
            return "Account Deleted Successfully!", 200
        except Exception as e:
            raise AccountModificationError("Account not found with given Number!")

    @auth.login_required()
    def put(self, id):
        try:
            body = request.get_json(force=True)
            Account.objects.get(phone=id).update(**body)
            return "Account Details Updated", 200
        except Exception as e:
            raise AccountModificationError("Account can't be found for updation!")


class UserDetails(Resource):
    def get(self):
        try:
            usr = User.objects().to_json()
            return Response(usr, mimetype="application/json", status=200)
        except Exception as e:
            raise UnauthorizedError("Not an authorized person!")


class RegisterUser(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            usr = User(**body)
            usr.save()
            uid = usr.id
            return {'id': str(uid)}, 200
        except:
            return "Username should be unique", 500


class UpdateUser(Resource):
    def put(self, id):
        try:
            body = request.get_json(force=True)
            User.objects.get(userid=id).update(**body)
            return 'User Details Updated Successfully!', 200
        except Exception as E:
            raise UnauthorizedError("User does not Exist!")


class AdminDetails(Resource):
    def get(self):
        try:
            adm = Admin.objects().to_json()
            return Response(adm, mimetype="application/json", status=200)
        except Exception as e:
            raise UnauthorizedError("Not an authorised person!")


class RegisterAdmin(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            adm = Admin(**body)
            adm.hash_password()
            adm.save()
            aid = adm.id
            return {'id': str(aid)}, 200
        except (UnauthorizedError, AdminAlreadyExistsError):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError("Id Already Exists! Admin ID should be unique.")


class UpdateAdmin(Resource):
    @auth.login_required()
    def put(self, id):
        try:
            body = request.get_json(force=True)
            Admin.objects.get(admid=id).update(**body)
            return 'Admin Details Updated Successfully!', 200
        except Exception as E:
            raise UnauthorizedError("Admin does not Exist!")
