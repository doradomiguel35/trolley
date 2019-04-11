from django import forms
from .models import Board, Team, List, Ticket, Comment, InviteToBoard
from users.models import User


class BoardForms(forms.ModelForm):
    """
    Board forms
    """
    description = forms.CharField(widget=forms.Textarea, required=False)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False)

    class Meta:
        model = Board
        fields = ('title', 'visibility', 'description', 'team',)


class TeamForms(forms.ModelForm):
    """
    Team forms
    """
    description = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.CharField(required=False)

    class Meta:
        model = Team
        fields = ('name', 'description', 'website',)


class ListForms(forms.ModelForm):
    """
    List forms
    """

    class Meta:
        model = List
        fields = ('name',)


class TicketCreationForms(forms.ModelForm):
    """
    Card forms
    """

    class Meta:
        model = Ticket 
        fields = ('name',)


class TicketForms(forms.ModelForm):
    """
    Ticket forms
    """

    class Meta:
        model = Ticket
        fields = ('name','description',)


class TicketDescForms(forms.ModelForm):
    """
    Ticket description
    """
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Ticket
        fields = ('description',)


class CommentForms(forms.ModelForm):
    """
    Comment forms
    """
    comment = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
    file = forms.FileField(required=False)

    class Meta:
        model = Comment
        fields = ('comment','file','image',)


class EditCommentForms(forms.ModelForm):
    """
    Edit commen form
    """
    comment = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Comment
        fields = ('comment',)


class SearchForm(forms.ModelForm):
    """
    Search Form for board
    """
    title =  forms.CharField(required=False)

    class Meta:
        model = Board
        fields = ('title',)


class InviteUserBoardForm(forms.Form):
    """
    Invite user to board
    """
    email = forms.EmailField()
    

