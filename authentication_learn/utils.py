# -- FOR HASHING PASWWORD --

# import libraries
from passlib.context import CryptContext


# create variable for store Crypt context
pwd_context = CryptContext(
    schemes=["bcrypt"]
)

# function for hashing
def hash(passsword: str):
    return pwd_context.hash(passsword)

# function for verify password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)