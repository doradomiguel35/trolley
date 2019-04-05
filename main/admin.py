from django.contrib import admin
from. models import Board, Team, Ticket, Comment, List


class BoardAdmin(admin.ModelAdmin):
	"""
	Board Admin
	"""
	model = Board

	list_display = ('title','description','visibility','owner','team','date_created','date_modified' )




class TeamAdmin(admin.ModelAdmin):
	"""
	Team Admin
	"""
	model = Team
	list_display = ('name','description','website')


admin.site.register(Board, BoardAdmin)
admin.site.register(Team, TeamAdmin)