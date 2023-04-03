from django.urls import path

from todo.views import (
    index, TaskCreateView, toggle_change_task_status, TaskDeleteView,
    TaskUpdateView,
    TagsListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

app_name = "todo"

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks_status/<int:pk>/",
        toggle_change_task_status,
        name="tasks-change-status"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/",
        TagsListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
