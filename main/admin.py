from django.contrib import admin
from. models import Board, Team, Ticket, Comment, List, InviteToBoard


class BoardAdmin(admin.ModelAdmin):
	"""
	Board Admin
	"""
	model = Board

	list_display = ('title','description','visibility','owner','team','date_created','date_modified' )


class TicketAdmin(admin.ModelAdmin):
	"""
	Ticket Admin
	"""
	model = Ticket

	list_display = ('name', 'description', 'lists')


class TeamAdmin(admin.ModelAdmin):
	"""
	Team Admin
	"""
	model = Team
	list_display = ('name','description','website')


class CommentAdmin(admin.ModelAdmin):
	"""
	Comment Admin
	"""
	model = Comment
	list_display = ('user','comment','ticket')


class ListAdmin(admin.ModelAdmin):
	"""
	List Admin
	"""
	model = List
	list_display = ('name','board')


class InviteBoardAdmin(admin.ModelAdmin):
	"""
	Invite to Board Admin
	"""
	model = InviteToBoard
	list_display = ('confirmed','user','board')


admin.site.register(Board, BoardAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(InviteToBoard, InviteBoardAdmin)