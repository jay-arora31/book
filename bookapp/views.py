from bookapp.models import Bookinfo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render, redirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import bookform,yourForm
from django.contrib import messages

from operator import and_
from django.db.models import Q
# Create your views here.


###-----------------------------------------------Adding New Book-----------------------------------------------------##
class AddBook(TemplateView):
  template_name = 'book/addbook.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = bookform()
    form1=yourForm()
    context = {'form':fm,'form1':form1}
    return context
  

  def post(self, request):
       bookform=forms.bookform()
       if request.method=='POST':
            productForm=forms.bookform(request.POST, request.FILES)
            if productForm.is_valid():
                book_name= productForm.cleaned_data['book_name']
                author= productForm.cleaned_data['author']
                genre= productForm.cleaned_data['genre']
                language= productForm.cleaned_data['language']
                
                if Bookinfo.objects.filter(Q(book_name__icontains=book_name) & Q(author__icontains=author) & Q(genre__icontains=genre) & Q(language__icontains=language)).exists(): 
                  messages.success(request, 'Book is Already Exist')
                  return HttpResponseRedirect('/')
                else:
                    productForm.save()
                    print("HEreeeeeeeeeeeeeeeeee")
                    return HttpResponseRedirect('/ShowBook')

###-----------------------------------------------View Book and Search Book-----------------------------------------------------##


class ShowBook(TemplateView):
  template_name = 'book/showbooks.html'
  def get_context_data(self):
        book=Bookinfo.objects.all()
        data = {}
        data['book'] = book
        genrelist=[]
        for i in book:
            genrelist.append(i.genre)
            genre_unique = []
            unique_numbers = set(genrelist)
        for number in unique_numbers:
            genre_unique.append(number)
        data['k']=genre_unique
        language_list=[]
        for i in book:
            language_list.append(i.language)
            language_unique = []
            unique_numbers = set(language_list)
        for number in unique_numbers:
            language_unique.append(number)
        print(language_unique)
        data['la']=language_unique
        return data
  def post(self, request):
    print("This is Post Function")
    genrelist1 = request.POST.getlist('genrecheck1[]')
    print(genrelist1)
    #genrelist1 = request.POST.getlist('genrecheck[]')
    languagelist1 = request.POST.getlist('langauagecheck[]')
    print
    data = {}
    book1=Bookinfo.objects.all()
    genrelist=[]
    
    for i in book1:
      genrelist.append(i.genre)
    genre_unique = []
    unique_numbers = set(genrelist)

    for number in unique_numbers:
        genre_unique.append(number)
    data['k']=genre_unique

    language_list=[]
    for i in book1:
      language_list.append(i.language)
    language_unique = []
    unique_numbers = set(language_list)
    for number in unique_numbers:
        language_unique.append(number)
    data['la']=language_unique

    if not genrelist1:
        genrelist1=genre_unique

    if not languagelist1:
        languagelist1=language_unique
    book= Bookinfo.objects.filter(Q(genre__in=genrelist1) & Q(language__in=languagelist1))
    
    data['book'] = book
    data['selectedlist']=genrelist1
    return render(request,'book/showbooks.html',data)
    
    
