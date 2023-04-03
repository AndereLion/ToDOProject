from django.test import TestCase

from todo.models import Task, Tag


class ModelsTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            content="Test Task",
            deadline="2021-04-30",
            is_completed=False
        )
        self.tag = Tag.objects.create(name="Test Tag")

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Test Tag")
