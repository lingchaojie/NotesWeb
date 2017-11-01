from django.http import HttpResponse
from .models import Note
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('index.html')
#     context = {
#         'all_album':all_albums,
#     }
#     return HttpResponse(template.render(context,request))

def index(request):
    all_Notes = Note.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        'all_Notes':all_Notes,
    }
    return HttpResponse(template.render(context,request))


def addNote(request):
    title = content = ''
    if (request.method == "POST"):
        NoteTitle = request.POST['title']
        NoteContent = request.POST['content']
        note = Note(title = NoteTitle,content=NoteContent)
        note.save()
        if note is not None:
            return render(request,'homepage.html')
    return render(request,'EnterNote.html')

def register(request):
    username = password = ''
    if (request.method == "POST"):
        userName = request.POST['username']
        passWord = request.POST['password']
        Email = request.POST['email']
        user = User.objects.create_user(username=userName,email=Email,password=passWord)
        user.save()
        user = authenticate(username=userName,password=passWord)
        if user is not None:
            if user.is_active:
                login(request, user)
            return render(request,'homepage.html')

    return render(request,'register.html')


#
# def Register(request):
#     return render(request,'register.html')


#
# def login_user(request):
#     logout(request)
#     username = password = ''
#
#     if (request.method == "POST"):
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/home')
#     return render(request,'form.html')
