import unittest

from models.users import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Clear all users before each test"""
        User.all.clear()

    def test_create_user(self):
        """Test creating a user"""
        user = User(username="testuser", email="test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

    def test_user_in_all(self):
        """Test that created user is added to User.all"""
        user = User(username="testuser", email="test@example.com")
        self.assertIn(user, User.all)
        self.assertEqual(len(User.all), 1)

    def test_multiple_users(self):
        """Test creating multiple users"""
        user1 = User(username="user1", email="user1@example.com")
        user2 = User(username="user2", email="user2@example.com")
        self.assertEqual(len(User.all), 2)
        self.assertIn(user1, User.all)
        self.assertIn(user2, User.all)


if __name__ == "__main__":
    unittest.main()
