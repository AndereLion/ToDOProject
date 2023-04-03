from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateField(
        label="What is deadline?",
        widget=forms.SelectDateWidget
    )

    class Meta:
        model = Task
        fields = "__all__"
