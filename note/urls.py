from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="note"),
    path('dict',views.dict,name='dict')
]