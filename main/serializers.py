from .models import Board, Team, List, Ticket, Comment
from rest_framework import serializers


class ListSerializer(serializers.ModelSerializer):
	"""
	Comment Serializer

	"""
	class Meta:
		model = List
		fields = (
			'id',
			'name',
		)


class TicketSerializer(serializers.ModelSerializer):
	"""
	Ticket serializer
	"""
	class Meta:
		model = Ticket
		fields = (
			'id',
			'name',
			'description',
			'lists',
		)


class TicketCreationSerializer(serializers.ModelSerializer):
	"""
	Ticket Creation serializer
	"""
	class Meta:
		model = Ticket
		fields = ('id','name',)


class CommentSerializer(serializers.ModelSerializer):
	"""
	Comment Serializer
	"""
	class Meta:
		model = Comment
		fields = (
			'id',
			'user',
			'comment',
			'ticket',
		)


class TicketDescSerializer(serializers.ModelSerializer):
	"""
	Ticket Description Serializer
	"""
	class Meta:
		model = Ticket
		fields = ('id','description',)


class CommentEditSerializer(serializers.ModelSerializer):
	"""
	comment edit serializer
	"""
	class Meta:
		model = Comment
		fields = ('id','comment',)


class BoardSerializer(serializers.ModelSerializer):
	"""
	board serializer
	"""
	class Meta:
		model = Board
		fields = ('id','title',)

