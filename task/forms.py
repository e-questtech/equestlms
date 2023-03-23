from django import forms

from .models import Task, TaskSubmission


class TaskSubmissionForm(forms.ModelForm):
    tasks = forms.ModelChoiceField(
        queryset=Task.objects.values_list("course_tasks", flat=True).distinct(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    task_file = forms.ImageField(
        required=True, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )

    class Meta:
        model = TaskSubmission
        fields = ["tasks", "task_file"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     student = Student.objects.filter(user=self.instance.student)
    #     self.fields["tasks"].queryset = TaskSubmission.objects.filter(student=student)
