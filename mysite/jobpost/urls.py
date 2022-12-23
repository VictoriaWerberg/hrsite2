from django.urls import path

from .views import *

urlpatterns = [

    path('', job_list, name='job-list'),
    path('category/<int:category_id>/', job_category, name='job-category'),   
]