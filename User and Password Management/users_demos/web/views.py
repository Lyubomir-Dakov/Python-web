from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views import generic as views

from users_demos.auth_app.models import AppUser

UserModel = get_user_model()


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['has_email'] = AppUser.has_email(self.request.user)
        return context
