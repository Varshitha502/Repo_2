from django.urls import path
from IND_AP import views
urlpatterns=[
    path('chittoor/',views.chittoor,name='chittoor'),
    path('kadapa/',views.kadapa,name='kadapa')
]