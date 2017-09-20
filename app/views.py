from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.serializers import BookSerializer ,RatingSerializer
from app.models import Book,Rating
from rest_framework.decorators import api_view

class BookViewSet(ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	permission_classes = (IsAuthenticated,)

class RatViewSet(ModelViewSet):

	serializer_class = RatingSerializer
	queryset = Rating.objects.all()
	permission_classes = (IsAuthenticated,)

# class BookDetailsViewSet(viewsets.ViewSet):

# 	def list(self,request):

# 		book = Book.objects.all()
# 		serializer = BookSerializer(book, many=True)
# 		return Response(serializer.data)

# 	def create(self,request):
		
# 		permission_classes = (IsAuthenticated,)
# 		serializer = BookSerializer(data=request.data)
# 		if serializer:
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def retrive(self,request,pk):

# 		book = Book.objects.all()
# 		book_list = get_object_or_404(book,pk)
# 		serializer = BookSerializer(book_list)
# 		return Response(serializer.data)

# 	def partial_update(self,request,pk):

# 		book = Book.get_object(pk)
# 		serializer = BookSerializer(book,request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 	def destroy(self,request,pk):

# 		book = Book.get_object(pk)
# 		book.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

# class RatingViewSet(viewsets.GenericViewSet):
# 		permission_classes = (IsAuthenticated,)
	

# 		def list(self,request):

# 			rating = Rating.objects.all()
# 			serializer = RatingSerializer(rating,many=True)
# 			return Response(serializer.data)


# 		# def create(self,request):
			
# 		# 	serializer = RatingSerializer(data=request.data)
# 		# 	if serializer.is_valid():
# 		# 		serializer.save()
# 		# 		return Response(serializer.data,status=status.HTTP_201_CREATED)
# 		# 	return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
			
# 		def retrive(self,request,pk):

# 			rating = get_object_or_404(pk)
# 			serializer = RatingSerializer(rating)
# 			return Response(serializer.data)

# 		def partial_update(self,request,pk):

# 			rating = Rating.get_object(pk)
# 			serializers = RatingSerializer(rating,request.data)
# 			if serializer.is_valid():
# 				serializer.save()
# 				return Response(serializer.data)
# 			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 		def destroy(self,request,pk):

# 			rating = Rating.get_object(pk)
# 			rating.delete()
# 			return Response(status=status.HTTP_204_NO_CONTENT)
