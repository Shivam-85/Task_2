from view.bank import GetAllAccounts, OpenAccount, DeleteAndUpdateAccount, UserDetails, AdminDetails, RegisterAdmin, \
    RegisterUser, UpdateAdmin, UpdateUser

from .reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(GetAllAccounts, '/accounts')
    api.add_resource(OpenAccount, '/openaccount')
    api.add_resource(DeleteAndUpdateAccount, '/modifyaccount/<id>')
    api.add_resource(UserDetails, '/users')
    api.add_resource(AdminDetails, '/admin')
    api.add_resource(RegisterAdmin, '/registeradmin')
    api.add_resource(UpdateAdmin, '/updateadmin/<id>')
    api.add_resource(RegisterUser, '/registeruser')
    api.add_resource(UpdateUser, '/updateuser/<id>')
    api.add_resource(ForgotPassword, '/auth/forgot')
    api.add_resource(ResetPassword, '/auth/reset')
