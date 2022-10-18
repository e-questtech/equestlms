from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.utils.translation import gettext_lazy as _

from equestlms.home.models import CustomUser
from equestlms.utils.choices import GENDER_CHOICES
from equestlms.utils.forms import CssForm


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = CustomUser


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = CustomUser

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class ProfileUpdateForm(admin_forms.UserChangeForm, CssForm):
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
            "birthday": forms.DateInput(
                format=("%m-%Y-%d"), attrs={"placeholder": "Date of Birth"}
            ),
            "gender": forms.Select(
                choices=GENDER_CHOICES,
                attrs={
                    "placeholder": "Preference",
                    "class": "form-select select country-select",
                },
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email address", "readonly": True}
            ),
            "mobile_no": forms.TextInput(
                attrs={"type": "tel", "placeholder": "077 1234 5678"}
            ),
            "profile_pic": forms.FileInput(),
        }


class PasswordUpdateForm(admin_forms.PasswordChangeForm, CssForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
