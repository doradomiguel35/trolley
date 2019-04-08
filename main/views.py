from django.shortcuts import render
from .models import Board, Team, List, Ticket
from .forms import BoardForms, TeamForms, ListForms, TicketCreationForms
from trolley.settings import AUTH_USER_MODEL
from django.views.generic import TemplateView
from django.http import JsonResponse
from .serializers import ListSerializer, TicketCreationSerializer


class TeamView(TemplateView):
    """
    Create boards here
    """

    def get(self, *args, **kwargs):
        team = Team.objects.get(id=kwargs.get('id'))
        
        return render(self.request, 'team/team.html',
            {'team_profile': team,
             'user': self.request.user})

    def post(self, request, *args, **kwargs):
        team_form = TeamForms(request.POST)

        if team_form.is_valid():
            team = team_form.save()
            team = Team.objects.get(id=team.id)
            request.user.teams.add(team)

            return render(request, 'team/team.html',
                {'team_profile': team,
                 'user': request.user})


class MainView(TemplateView):
    """
    Home view
    """
    def get(self, *args, **kwargs):
        team_form = TeamForms()
        board_form = BoardForms()
        teams = self.request.user.teams.all()
        boards = Board.objects.filter(owner_id=self.request.user.id)
        return render(self.request, 'main/home.html',
            {'team_form': team_form,
             'board_form': board_form,
             'teams': teams,
             'boards': boards})

    def post(self, request, *args, **kwargs):
        team_form = TeamForms(request.POST)


class BoardView(TemplateView):
    """
    Board view
    """
    team_form = TeamForms()
    board_form = BoardForms()
    list_form = ListForms()
    ticket_form = TicketCreationForms()

    def get(self, *args, **kwargs):
        board = Board.objects.get(id=kwargs.get('id'))
        team = self.request.user.teams.all()
        lists = List.objects.filter(board_id=board.id)
        tickets = Ticket.objects.filter(lists_id__in=lists)


        return render(self.request, 'board/board.html',
            {'user': self.request.user,
             'board': board,
             'team': team,
             'lists': lists,
             'tickets': tickets,
             'list_form': self.list_form,
             'board_form': self.board_form,
             'team_form': self.list_form,
             'ticket_form': self.ticket_form})

    def post(self, *args, **kwargs):
        self.board_form = BoardForms(self.request.POST)
        if self.board_form.is_valid():
            board = Board(title=self.board_form.cleaned_data['title'],
                    visibility=self.board_form.cleaned_data['visibility'],
                    description=self.board_form.cleaned_data['description'],
                    team=self.board_form.cleaned_data['team'],
                    owner_id=self.request.user.id)
            board.save()
            team = self.request.user.teams.all()
            lists = List.objects.filter(board_id=board.id)
            tickets = Ticket.objects.filter(lists_id__in=lists)



            return render(self.request, 'board/board.html',
                {'user': self.request.user,
                 'board': board,
                 'team': team,
                 'lists': lists,
                 'tickets': tickets,
                 'list_form': self.list_form,
                 'board_form': self.board_form,
                 'team_form': self.list_form,
                 'ticket_form': self.ticket_form})    

        teams = self.request.user.teams.all()
        boards = Board.objects.filter(owner_id=self.request.user.id)
        return render(self.request, 'main/home.html',
            {'team_form': self.team_form,
             'board_form': self.board_form,
             'teams': teams,
             'boards': boards})


class ListView(TemplateView):
    """
    List View
    """

    def post(self, *args, **kwargs):
        list_form = ListForms(self.request.POST)
        if list_form.is_valid():
            lists = List(name=list_form.cleaned_data['name'],
                board_id=kwargs.get('board_id'))
            lists.save()
            serialize = ListSerializer(lists)

            return JsonResponse(serialize.data, safe=False)


class TicketView(TemplateView):
    """
    Ticket view
    """

    def post(self, *args, **kwargs):
        ticket_form = TicketCreationForms(self.request.POST)
        if ticket_form.is_valid():
            ticket = Ticket(name=ticket_form.cleaned_data['name'],
                lists_id=kwargs.get('list_id'))
            ticket.save()

            serialize = TicketCreationSerializer(ticket)

            return JsonResponse(serialize.data, safe=False)





