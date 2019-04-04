from django import forms
from .models import Board, Team


class BoardForms(forms.ModelForm):
    """
    Board forms
    """
    class Meta:
        model = Board
        fields = ('title', 'visibility', 'description')


class TeamForms(forms.ModelForm):
    """
    Team forms
    """
    class Meta:
        model = Team
        fields = ('name', 'description', 'website')