from database.users import get_user
from utils.hashing import verify_password


def login_user(username, password):

    if not username or not password:
        return False

    user = get_user(username)

    if user is None:
        return False

    return verify_password(
        password,
        user["password"]
    )