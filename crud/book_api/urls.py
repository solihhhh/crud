from django.urls import path

# function
# from book_api.views import book_list, book_detail
# class
from book_api.views import BookList, BookDetail

urlpatterns = [
    # function
    # path('',book_list),
    # path('<int:pk>/',book_detail),
    #  class
    path('', BookList.as_view()),
    path('<int:pk>/', BookDetail.as_view()),
]