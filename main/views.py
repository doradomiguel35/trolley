from django.shortcuts import render
from .models import Board, Team
from .forms import BoardForms, TeamForms
from trolley.settings import AUTH_USER_MODEL
from django.views.generic import TemplateView
from django.http import JsonResponse


class TeamView(TemplateView):
    """
    Create boards here
    """
    def post(self, request, *args, **kwargs):
        team_form = TeamForms(request.POST)

        if team_form.is_valid():
            print('valid')
            team = team_form.save()
            team = Team.objects.get(id=team.id)


            