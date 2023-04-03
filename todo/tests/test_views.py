from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag


class PublicTaskTests(TestCase):
    def test_index_view_with_no_tasks(self):
        response = self.client.get(reverse("todo:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["tasks"], [])

    def test_index_view_with_tasks(self):
        task1 = Task.objects.create(
            content="Task1",
            deadline="2021-04-30",
            is_completed=False)

        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["tasks"], [task1]
        )

    def test_task_create_view_template_used(self):
        response = self.client.get(reverse("todo:task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_create_view_with_valid_data(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(reverse("todo:task-create"), {
            "content": "Test task",
            "deadline": "2021-01-01",
            " is_completed": False,
            "tags": [tag.id]
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().content, "Test task")

    def test_task_create_view_with_invalid_data(self):
        response = self.client.post(reverse("todo:task-create"), {
            "content": "Test task",
            "deadline": "2021-01-01",
            " is_completed": False,
            "tags": [1]
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_update_view_with_valid_data(self):
        task = Task.objects.create(
            content="Task1",
            deadline="2021-04-30",
            is_completed=False)
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(
            reverse("todo:task-update", kwargs={"pk": task.id}), {
                "content": "Test task",
                "deadline": "2021-01-01",
                " is_completed": False,
                "tags": [tag.id]
            })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().content, "Test task")

    def test_task_update_view_with_invalid_data(self):
        task = Task.objects.create(
            content="Task1",
            deadline="2021-04-30",
            is_completed=False)
        response = self.client.post(
            reverse("todo:task-update", kwargs={"pk": task.id}), {
                "content": "Test task",
                "deadline": "2021-01-01",
                " is_completed": False,
                "tags": [1]
            })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().content, "Task1")

    def test_task_delete_view(self):
        task = Task.objects.create(
            content="Task1",
            deadline="2021-04-30",
            is_completed=False)
        response = self.client.post(
            reverse("todo:task-delete", kwargs={"pk": task.id}))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_tag_create_view_template_used(self):
        response = self.client.get(reverse("todo:tag-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_tag_create_view_with_valid_data(self):
        response = self.client.post(reverse("todo:tag-create"), {
            "name": "Test Tag"
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, "Test Tag")

    def test_tag_create_view_with_invalid_data(self):
        response = self.client.post(reverse("todo:tag-create"), {
            "name": ""
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tag.objects.count(), 0)

    def test_tag_update_view_with_valid_data(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(
            reverse("todo:tag-update", kwargs={"pk": tag.id}), {
                "name": "Test Tag 2"
            })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, "Test Tag 2")

    def test_tag_update_view_with_invalid_data(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(
            reverse("todo:tag-update", kwargs={"pk": tag.id}), {
                "name": ""
            })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, "Test Tag")

    def test_tag_delete_view(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(
            reverse("todo:tag-delete", kwargs={"pk": tag.id}))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 0)


