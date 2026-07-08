from database.users import add_user
from utils.hashing import hash_password


def register_user(username, password):

    if not username or not password:
        return False

    hashed = hash_password(password)

    return add_user(username, hashed)