
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
urlpatterns = [
         path('', views.index, name ='index'),
             ##### user related path##########################
         path('', include('user.urls')),
         path('login/', user_view.Login, name ='login'),
         path('logout/', auth.LogoutView.as_view(template_name ='user / index.html'), name ='logout'),
         path('register/', user_view.register, name ='register'),
]
