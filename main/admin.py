from django.contrib import admin
from. models import Board, Team, Ticket, Comment, List, InviteToBoard, ActivityLog, Checklist, Progress


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


class ActivityLogAdmin(admin.ModelAdmin):
	"""
	Activity log admin
	"""
	model = ActivityLog
	list_display = ('activity','board','date_created')


class ProgressAdmin(admin.ModelAdmin):
	"""
	Progress admin
	"""
	model = Progress
	list_display = ('title','progress','ticket')


class ChecklistAdmin(admin.ModelAdmin):
	"""
	Checklist admin
	"""
	model = Checklist
	list_display = ('name','progress','done',)

admin.site.register(Board, BoardAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(InviteToBoard, InviteBoardAdmin)
admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Checklist, ChecklistAdmin)