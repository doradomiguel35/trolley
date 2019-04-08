from .models import Board, Team, List, Ticket
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
			'name',
			'description'
		)


class TicketCreationSerializer(serializers.ModelSerializer):
	"""
	Ticket Creation serializer
	"""
	class Meta:
		model = Ticket
		fields = ('name',)