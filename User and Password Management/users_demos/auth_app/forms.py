from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms
from users_demos.auth_app.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):  # taka lesno mojem da extendvame
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')
        field_classes = {'username': auth_forms.UsernameField}

    # save with data for profile
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    # For demo purposes only ! Ne se pravi taka!
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     user.username = user.first_name + '-' + user.last_name
    #
    #     if commit:
    #         user.save()
    #         return user
