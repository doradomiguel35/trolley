from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('board/create/', views.TeamView.as_view(), name='board'),
]