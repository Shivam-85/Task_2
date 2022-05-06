class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class AdminAlreadyExistsError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class DeleteAccountError(Exception):
    pass


class UpdateAccountError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class NotAnAdminError(Exception):
    pass


class AccountModificationError(Exception):
    pass


class EmailDoesnotExistsError(Exception):
    pass


class BadTokenError(Exception):
    pass


errors = {
    "AccountModificationError": {
        "message": "Something went wrong",
        "status": 500
    },
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "AdminAlreadyExistsError": {
        "message": "Admin with given id already exists",
        "status": 400
    },
    "UserAlreadyExistsError": {
        "message": "User already exists",
        "status": 403
    },
    "DeleteAccountError": {
        "message": "Not an authorized person to perform this",
        "status": 403
    },
    "UpdateAccountError": {
        "message": "Not an authorized person to perform this",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "EmailDoesnotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400
    },
    "BadTokenError": {
        "message": "Invalid token",
        "status": 403
    }
}
