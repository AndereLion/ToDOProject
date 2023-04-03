from django.test import TestCase

from todo.forms import TaskForm
from todo.models import Tag


class FormTests(TestCase):
    def test_task_create_form(self):
        tag = Tag.objects.create(name="Test Tag")
        form = TaskForm(data={
            "content": "Test task",
            "deadline": "2021-01-01",
            " is_completed": False,
            "tags": [tag.id]

        })

        self.assertTrue(form.is_valid())

    def test_task_form_blank_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())

    def test_task_form_invalid_data(self):
        form = TaskForm(data={
            "content": "Test task",
            "deadline": "2021-01-01",
            " is_completed": False,
            "tags": [1]

        })

        self.assertFalse(form.is_valid())
