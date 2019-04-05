from django import forms
from .models import Board, Team
from users.models import User


class BoardForms(forms.ModelForm):
    """
    Board forms
    """
    description = forms.CharField(widget=forms.Textarea, required=False)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False)

    class Meta:
        model = Board
        fields = ('title', 'visibility', 'description', 'team')


class TeamForms(forms.ModelForm):
    """
    Team forms
    """
    description = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.CharField(required=False)

    class Meta:
        model = Team
        fields = ('name', 'description', 'website')
