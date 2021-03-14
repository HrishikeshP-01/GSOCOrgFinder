from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    url(r'^$',csrf_exempt(views.find_projects),name='find_projects')
    ]
