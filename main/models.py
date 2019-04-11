from django.db import models
from users.models import User
from trolley import settings

def ticket_file_upload_path(instance, filename):
    return f'tickets/{instance.user.id}/comments/{instance.ticket.id}/{filename}'

def ticket_image_file_upload_path(instance, filename):
    return f'ticket_images/{instance.user.id}/comments/{instance.ticket.id}/{filename}'

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
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="admin")
    team = models.ForeignKey('main.Team', on_delete=models.SET_NULL, null=True, to_field='name')
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="members")

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
    assigned = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    lists = models.ForeignKey('main.List', on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    Comment model, comment on tickets 
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    file = models.FileField(upload_to=ticket_file_upload_path, null=True)
    image = models.ImageField(upload_to=ticket_image_file_upload_path, null=True)
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


class InviteToBoard(models.Model):
    """
    Invite to board
    """
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    confirmed = models.BooleanField(default=False)
    board = models.ForeignKey('main.Board', on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)




