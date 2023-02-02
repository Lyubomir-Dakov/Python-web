from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from users_demos.auth_app.forms import SignUpForm

# Register your models here.
# UserModel - navsqkude kudeto se izpolzva osven tam kudeto e definiran i settings.pyq treabva da bude izvikan s get_user_model()
UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ()
    add_form = SignUpForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'age'),
        }),
    )
