import unittest

from models.tasks import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        """Clear all tasks before each test"""
        Task.all.clear()

    def test_task_attributes(self):
        """Test task has correct attributes"""
        # Tasks are created through CLI, just verify class structure
        self.assertTrue(hasattr(Task, "all"))
        self.assertIsInstance(Task.all, list)

    def test_task_all_list(self):
        """Test Task.all is a list"""
        self.assertEqual(len(Task.all), 0)
        self.assertIsInstance(Task.all, list)


if __name__ == "__main__":
    unittest.main()
