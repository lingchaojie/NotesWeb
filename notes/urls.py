from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^Addnote$',views.addNote,name='addNote'),
    url(r'^Register$',views.register,name = 'register'),
]