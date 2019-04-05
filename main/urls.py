from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('home/<int:id>/', views.MainView.as_view(), name='home'),
    path('team/create/', views.TeamView.as_view(), name='create'),
    path('team/<int:id>/', views.TeamView.as_view(), name='team'),
    path('board/create/', views.BoardView.as_view(), name='board'),
    path('board/<int:id>', views.BoardView.as_view(), name='board_view')
]