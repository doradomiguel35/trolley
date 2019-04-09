from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('home/<int:id>/', views.MainView.as_view(), name='home'),
    path('team/create/', views.TeamView.as_view(), name='create'),
    path('team/<int:id>/', views.TeamView.as_view(), name='team'),
    path('board/create/', views.BoardView.as_view(), name='board'),
    path('board/<int:id>', views.BoardView.as_view(), name='board_view'),
    path('board/create/list/<int:board_id>/', views.ListView.as_view(), name='list_create'),
    path('board/create/card/<int:list_id>/', views.TicketView.as_view(), name='card_create'),
    path('board/view/card/<int:ticket_id>/',views.TicketView.as_view(), name='ticket_view'),
    path('board/view/card/comment/<int:ticket_id>/', views.CommentView.as_view(), name='ticket_comment'),
    path('board/view/card/description/<int:ticket_id>/', views.UpdateDescTicketView.as_view(), name='ticket_description'),
    path('board/view/card/comment/edit/<int:comment_id>/', views.EditComment.as_view(), name="edit_comment"),
    path('board/view/card/comment/get/<int:comment_id>/',views.CommentView.as_view(),name='get_comment'),
]