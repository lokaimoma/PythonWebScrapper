from models import Model
from dataclasses import dataclass, field
import uuid
from models.users import error 
from common import Utils


@dataclass(eq=False)
class User(Model):
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    collection: str = field(init=False, default='users')


    def json(self):
        return {
            "email": self.email,
            "password": self.password,
            "_id": self._id
        }

    @classmethod
    def find_by_email(cls, email):
        try:
            return cls.find_only_one("email", email)
        except TypeError:
            raise error.UserNotFoundError('User not registered.')


    @classmethod
    def register_user(cls, email, password):
        if not Utils.email_is_valid(email):
            raise error.InvalidEmailError('Email format error')
        

        try:
            cls.find_by_email(email)
            raise error.UserAlreadyRegisteredError("User already exits try forgot password if you''ve lost password.")
        except error.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True


    @classmethod
    def is_login_valid(cls, email, password):
        
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise error.IncorrectPasswordError('Incorrect password or email try forgot password.')

        return True
