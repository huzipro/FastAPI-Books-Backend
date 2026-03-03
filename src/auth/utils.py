from passlib.context import CryptContext

passwd_context = CryptContext(schemes=['bcrypt'])

def generate_pw_hash(pw:str):
    if not pw:
        raise ValueError('Incorrect! Empty string cannot be hashed')
    hash = passwd_context.hash(pw)
    return hash

def verify_pw_hash (pw: str, hash:str) -> bool:
    return passwd_context.verify(pw, hash)
