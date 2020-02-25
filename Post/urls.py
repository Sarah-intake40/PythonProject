from Post import views
from django.urls import path

urlpatterns=[
    path('single/',views.all_posts),
    

]