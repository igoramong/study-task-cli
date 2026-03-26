import unittest
import sys
import os

# Permitir importar arquivos da pasta src
sys.path.append(os.path.abspath("src"))

from task import Task


class TestTask(unittest.TestCase):

    def test_create_task(self):
        task = Task("Estudar Python")

        self.assertEqual(task.title, "Estudar Python")
        self.assertFalse(task.completed)

    def test_complete_task(self):
        task = Task("Estudar Python")

        task.completed = True

        self.assertTrue(task.completed)

    def test_to_dict(self):
        task = Task("Estudar Python")

        data = task.to_dict()

        self.assertEqual(data["title"], "Estudar Python")
        self.assertFalse(data["completed"])

    def test_from_dict(self):
        data = {
            "title": "Estudar Python",
            "completed": True
        }

        task = Task.from_dict(data)

        self.assertEqual(task.title, "Estudar Python")
        self.assertTrue(task.completed)


if __name__ == "__main__":
    unittest.main()