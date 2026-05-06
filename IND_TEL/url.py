from django.urls import path
from IND_TEL import views
urlpatterns=[
    path('hyderabad/',views.hyderabad,name='hyderabad'),
    path('warangal/',views.warangal,name='warangal')
]