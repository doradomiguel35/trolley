from django.db import models
from trolley import settings


class Board(models.Model):
    """
    Boards is where the list's tickets are managed
    """
    VIS_P = 'Private'
    VIS_PU = 'Public'

    VISIBILITY_CHOICES = (
        (VIS_PU, 'Public'),
        (VIS_P, 'Private'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="")
    visibility = models.CharField(max_length=50, choices=VISIBILITY_CHOICES, default=VIS_PU)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    team = models.ForeignKey('main.Team', on_delete=models.SET_NULL, null=True, to_field='name')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Team(models.Model):
    """
    Teams can own boards, composed of a group of users
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, default="", blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'   


class Ticket(models.Model):
    """
    Ticket model, the task
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="", blank=True, null=True)
    lists = models.ForeignKey('main.List', on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    Comment model, comment on tickets 
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    ticket = models.ForeignKey('main.Ticket', on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class List(models.Model):
    """
    List model
    """
    name = models.CharField(max_length=100)
    board = models.ForeignKey('main.Board', on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
