from django import forms

from .models import Task, TaskSubmission


class TaskSubmissionForm(forms.ModelForm):
    task = forms.ModelChoiceField(
        queryset=Task.objects.values_list("title", flat=True).distinct(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    task_file = forms.ImageField(
        required=True, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["task"].queryset = self.fields["task"].queryset.filter(
            tasks__course=self.instance.course
        )

    class Meta:
        model = TaskSubmission
        fields = ["task", "task_file"]
