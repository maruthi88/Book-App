from app.models import Book,Rating
from rest_framework import serializers
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ('name','created_at','updated_at','description','price', "id","publish")

class RatingSerializer(serializers.ModelSerializer):

	# book = serializers.ReadOnlyField(source='book.name')
	# user = serializers.PrimaryKeyRelatedField(
	# 	default=serializers.CurrentUserDefault(), queryset=User.objects.all()
	# )
	class Meta:
		model = Rating
		fields = ('rating','id','user','book')
		read_only_fields = ('user',)

	def create(self, validated_data):
		return Rating.objects.create(user=self.context["request"].user, **validated_data)

	def validate(self, validated_data):
		user = self.context["request"].user
		if "book" in validated_data and user == validated_data["book"].author:
			raise serializers.ValidationError("You are the author. NOT ALLOWED TO RATE")
		return validated_data