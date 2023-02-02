from django.contrib.auth.views import LoginView
from django.urls import path

from users_demos.auth_app.views import SignUpView, SighInView, SignOutView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', SighInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out')
)
