from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.urls import reverse_lazy
from django.shortcuts import resolve_url
from users_demos.auth_app.forms import SignUpForm


# class SignUpView(generic.CreateView):
#     template_name = 'auth/sign-up.html'


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm  # this form is buildIn from django
    success_url = reverse_lazy('index')

    # Signs the user in after successful register
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SighInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or resolve_url(settings.LOGIN_REDIRECT_URL)


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'

# class SignInform(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()


# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInform()
#     else:
#         form = SignInform(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context)
