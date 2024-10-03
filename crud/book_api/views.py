from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from book_api.models import Book
from book_api.serializers import BookSerializer


# Create your views here.

# def book_list(request):
#     books = Book.objects.all()
#     return JsonResponse({"books":list(books.values())})
#
# def book_detail(request,pk):
#     book = Book.objects.get(pk=pk)
#     data = {
#         "id":book.pk,
#         "title":book.title,
#         "author":book.author,
#         "price":book.price
#     }
#     return JsonResponse(data)

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     try:
#         book = get_object_or_404(Book, pk=pk)
#     except:
#         return Response({"Error": "Book not found"}, status=404)
#
#     if request.method == "GET":
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=204)


class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetail(APIView):
    def get(self, request, pk):
        try:
            book = get_object_or_404(Book, pk=pk)
        except:
            return Response({"Error": "Book not found"}, status=404)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    def put(self, request, pk):
        try:
            book = get_object_or_404(Book, pk=pk)
        except:
            return Response({"Error": "Book not found"}, status=404)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
         serializer.save()
        return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def delete(self, request, pk):
        try:
            book = get_object_or_404(Book, pk=pk)
        except:
            return Response({"Error": "Book not found"}, status=404)
        book.delete()
        return Response(status=204)