from rest_framework import serializers
from todo import models



class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id','title','content')
		model = models.Todo






