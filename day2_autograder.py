import unittest

from utils.hashing import hash_password
from utils.hashing import verify_password

from auth.register import register_user
from auth.login import login_user

from database.users import users


class TestCyberVault(unittest.TestCase):

    def setUp(self):
        users.clear()

    def test_hash(self):

        h = hash_password("password123")

        self.assertNotEqual(h, "password123")

        self.assertTrue(h.startswith("$2"))

    def test_verify(self):

        h = hash_password("hello")

        self.assertTrue(
            verify_password("hello", h)
        )

        self.assertFalse(
            verify_password("wrong", h)
        )

    def test_registration(self):

        self.assertTrue(
            register_user("alice", "secret")
        )

        self.assertFalse(
            register_user("alice", "another")
        )

    def test_login(self):

        register_user("bob", "abc123")

        self.assertTrue(
            login_user("bob", "abc123")
        )

        self.assertFalse(
            login_user("bob", "wrong")
        )


if __name__ == "__main__":
    unittest.main()