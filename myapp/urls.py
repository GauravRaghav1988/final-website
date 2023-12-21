from django.contrib import admin
from django.urls import path
from .import views
# from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',views.home),
    path('registration/',views.register),
    path('login/',views.user_login),
    path('account/',views.account), 
    path('changepassword/',views.change_password),
    path('logout/',views.logoutuser),   
    path('quiz/',views.quiz_home,name='quiz_home'),
    path('add_question/',views.addQuestion,name='addQuestion'),
    # path('showpost', post_list, name='post_list'),
    # path('post/<int:post_number>/', post_detail, name='post_detail'),
    path('blog/',views.blog_list , name='blog_list'),
 
]


urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
