import unittest

from models.projects import Project


class TestProject(unittest.TestCase):
    def setUp(self):
        """Clear all projects before each test"""
        Project.all.clear()

    def test_create_project(self):
        """Test creating a project"""
        project = Project(title="Test Project", due_date="2025-12-31")
        self.assertEqual(project.title, "Test Project")
        self.assertEqual(project.due_date, "2025-12-31")

    def test_project_in_all(self):
        """Test that created project is added to Project.all"""
        project = Project(title="Test Project", due_date="2025-12-31")
        self.assertIn(project, Project.all)
        self.assertEqual(len(Project.all), 1)

    def test_multiple_projects(self):
        """Test creating multiple projects"""
        proj1 = Project(title="Project 1", due_date="2025-12-31")
        proj2 = Project(title="Project 2", due_date="2026-01-15")
        self.assertEqual(len(Project.all), 2)
        self.assertIn(proj1, Project.all)
        self.assertIn(proj2, Project.all)


if __name__ == "__main__":
    unittest.main()
