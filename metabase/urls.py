from django.urls import path
from .views import *

urlpatterns = [

path('post',metapost.as_view()),    
path('get/<str:userId>/<str:questionids>/',metabaseclass.as_view()),
# path('get',metabaseclass.as_view()),
path('getbyuserid/<int:UserId>/',metaget.as_view())

]