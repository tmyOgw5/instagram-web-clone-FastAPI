from passlib.context import CryptContext

pwd_txt = CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash():
    def bcrypt(password: str):
        return pwd_txt.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_txt.verify(plain_password,hashed_password)