from Post import views
from django.urls import path

urlpatterns=[
    path('single/',views.all_posts),
    path('travel/<Id>',views.post_by_category),
    path('onePost/<Id>',views.show_comments),
                 


]