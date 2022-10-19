from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

from equestlms.home.models import CustomUser
from equestlms.utils.forms import CssForm


class ProfileUpdateForm(UserChangeForm, CssForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "mobile_no",
            "birthday",
            "gender",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "birthday": forms.DateField(),
            "gender": forms.ChoiceField(),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email address", "readonly": True}
            ),
            "mobile_no": forms.TextInput(
                attrs={"type": "tel", "placeholder": "077 1234 5678"}
            ),
            "profile_pic": forms.FileInput(),
        }


class PasswordUpdateForm(PasswordChangeForm, CssForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
