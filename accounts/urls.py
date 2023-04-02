from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterView, CustomLogoutView
from Player import settings


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    # path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    path('register/', RegisterView.as_view(), name="register")
]
