from django.shortcuts import render
from .models import Board, Team, List, Ticket, Comment
from .forms import (BoardForms, TeamForms, ListForms, TicketCreationForms, CommentForms, 
    TicketDescForms, EditCommentForms, SearchForm,)

from trolley.settings import AUTH_USER_MODEL
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .serializers import (ListSerializer, TicketCreationSerializer, TicketSerializer, 
    CommentSerializer, TicketDescSerializer, CommentEditSerializer, BoardSerializer,)


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
        search_form = SearchForm()
        comment_form = CommentForms()
        teams = self.request.user.teams.all()
        boards = Board.objects.filter(owner_id=self.request.user.id)
        return render(self.request, 'main/home.html',
            {'team_form': team_form,
             'board_form': board_form,
             'teams': teams,
             'boards': boards,
             'search_form': search_form,
             'comment_form': comment_form})

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
    comment_form = CommentForms()
    ticket_desc_form = TicketDescForms()
    search_form = SearchForm()
    # image_form = CommentImageForm()
    # file_form = CommentFileForm()

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
             'ticket_form': self.ticket_form,
             'comment_form': self.comment_form,
             'ticket_desc_form': self.ticket_desc_form,
             'search_form': self.search_form})
        # ,
        #          'image_form': self.image_form,
        #          'file_form': self.file_form}

            

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
                 'ticket_form': self.ticket_form,
                 'comment_form': self.comment_form,
                 'ticket_desc_form': self.ticket_desc_form,
                 'search_form': self.search_form})
            # ,
            #      'image_form': self.image_form,
            #      'file_form': self.file_form}
                
  

        teams = self.request.user.teams.all()
        boards = Board.objects.filter(owner_id=self.request.user.id)
        return render(self.request, 'main/home.html',
            {'team_form': self.team_form,
             'board_form': self.board_form,
             'teams': teams,
             'boards': boards})


class ListView(View):
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


class TicketView(View):
    """
    Ticket view
    """

    def get(self, *args, **kwargs):
        ticket = Ticket.objects.get(id=kwargs.get('ticket_id'))
        comments = Comment.objects.filter(
            ticket_id=kwargs.get('ticket_id')).values('id','user_id','user__first_name','user__last_name','comment','ticket_id','image','file')
        try:
            serialize = TicketSerializer(ticket).data
            serialize['comment']= list(comments)
            return JsonResponse(serialize, safe=False)

        except:
            serialize = TicketSerializer(ticket).data
            return JsonResponse(serialize, safe=False)

           

    def post(self, *args, **kwargs):
        ticket_form = TicketCreationForms(self.request.POST)
        if ticket_form.is_valid():
            ticket = Ticket(name=ticket_form.cleaned_data['name'],
                lists_id=kwargs.get('list_id'))
            ticket.save()

            serialize = TicketCreationSerializer(ticket)

            return JsonResponse(serialize.data, safe=False)


class UpdateDescTicketView(View):
    """
    update description of the ticket ticket
    """

    def post(self, *args, **kwargs):
        ticket_desc_form = TicketDescForms(self.request.POST)
        if ticket_desc_form.is_valid():
            ticket = Ticket.objects.get(id=kwargs.get('ticket_id'))
            ticket.description = ticket_desc_form.cleaned_data['description']
            ticket.save()
            
            serialize = TicketDescSerializer(ticket).data
            return JsonResponse(serialize, safe=False)
            

class CommentView(View):
    """
    Comment view
    """

    def get(self, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs.get('comment_id'))
        serialize = CommentSerializer(comment).data
        serialize['first_name'] = comment.user.first_name
        serialize['last_name'] = comment.user.last_name

        return JsonResponse(serialize, safe=False)


    def post(self, *args, **kwargs):
        comment_form = CommentForms(data=self.request.POST,files=self.request.FILES)
        if comment_form.is_valid():
            comment = Comment(user_id=self.request.user.id,
                comment=comment_form.data.get('comment'),
                file=comment_form.cleaned_data['file'],
                image=comment_form.cleaned_data['image'],
                ticket_id=kwargs.get('ticket_id'))

            comment.save()
            serialize = CommentSerializer(comment).data
            serialize['first_name'] = self.request.user.first_name
            serialize['last_name'] = self.request.user.last_name
            return JsonResponse(serialize, safe=False)


class EditComment(View):
    """
    Edit comment
    """

    def post(self, *args, **kwargs):
        comment_form = EditCommentForms(self.request.POST)
        if comment_form.is_valid():
            comment = Comment.objects.get(id=kwargs.get('comment_id'))
            comment.comment = comment_form.cleaned_data['comment']
            comment.save()
            serialize = CommentEditSerializer(comment).data
            serialize['first_name'] = comment.user.first_name
            serialize['last_name'] = comment.user.last_name
            return JsonResponse(serialize, safe=False)


class SearchBoardView(View):
    """
    Search board view
    """

    def get(self, *args, **kwargs):
        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            board = Board.objects.filter(title=search_form.cleaned_data['title'],visibility='Public').values('id','title')
            serializer = {'boards': list(board)}
            
            return JsonResponse(serializer, safe=False)
           

class DeleteComment(View):
    """
    Delete a ticket
    """ 

    def post(self, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs.get('comment_id'))
        comment.delete()

        serializer = CommentEditSerializer(comment).data
        return JsonResponse(serializer, safe=False)