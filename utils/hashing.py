import bcrypt


def hash_password(password: str) -> str:
    """
    Returns a salted bcrypt hash.
    """

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )

    return hashed.decode("utf-8")


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Returns True if password matches stored hash.
    """

    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    )