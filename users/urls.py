from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    # path('', views.HomeView.as_view(), name="home"),
    path('', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout")
]