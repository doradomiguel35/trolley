from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('home/<int:id>/', views.MainView.as_view(), name='home'),
    path('home/search/', views.SearchBoardView.as_view(), name='search_board'),
    path('team/create/', views.TeamView.as_view(), name='create'),
    path('team/<int:id>/', views.TeamView.as_view(), name='team'),
    path('board/create/', views.BoardView.as_view(), name='board'),
    path('board/close/<int:board_id>/', views.CloseBoardView.as_view(), name="close_board"),
    path('board/<int:id>', views.BoardView.as_view(), name='board_view'),
    path('board/create/list/<int:board_id>/', views.ListView.as_view(), name='list_create'),
    path('board/create/card/<int:list_id>/', views.TicketView.as_view(), name='card_create'),
    path('board/card/change/<int:ticket_id>/<int:lists_id>/', views.UpdateCardListView.as_view(), name='drag_card'),
    path('board/invite/<int:board_id>/', views.InviteToBoardView.as_view(), name='invite_member'),
    path('board/invite/view/', views.BoardInvites.as_view(), name='view_invites'),
    path('board/invite/confirm/<int:board_id>/<int:invite_id>/', views.BoardInvites.as_view(), name="confirm_invite"),
    path('board/view/members/<int:board_id>/', views.MemberBoardView.as_view(), name="members"),
    path('board/view/card/<int:ticket_id>/',views.TicketView.as_view(), name='ticket_view'),
    path('board/view/card/comment/<int:ticket_id>/', views.CommentView.as_view(), name='ticket_comment'),
    path('board/view/card/description/<int:ticket_id>/', views.UpdateDescTicketView.as_view(), name='ticket_description'),
    path('board/view/card/comment/edit/<int:comment_id>/', views.EditComment.as_view(), name="edit_comment"),
    path('board/view/card/comment/get/<int:comment_id>/',views.CommentView.as_view(),name='get_comment'),
    path('board/view/card/comment/delete/<int:comment_id>/',views.DeleteComment.as_view(),name='delete_comment'),
]