from django.urls import path,include
from django.conf.urls import url
from bookapp import views

urlpatterns = [
      path('addbook/', views.AddBook.as_view(), name='AddBook'),

    path('',views.ShowBook.as_view(), name='ShowBook'),
]