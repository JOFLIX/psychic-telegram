from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth
import app.forms
import app.views
from app.views import SearchResultsView
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.gallery, name='gallery'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    url(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()

    # Auth related urls

    url(r'^accounts/login/$', views.LoginView, name='login'),
    url(r'^logout$', views.LogoutView, { 'next_page': '/', }, name='logout'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    # searching the dir

    # url(r'^search/(?P<slug>[+\w]+)$', SearchResultsView.as_view(), name='search_results'),
    # url(r'^search/(?P<pk>\d+)/$', SearchResultsView.as_view(template_name ='search_results.html'), name='search_results'),
    url(r'^search/({slug_field: slug})', SearchResultsView.as_view(), name='search_results'),


    #enabling Auth
    ##### user related path##########################
    # path('', include('user.urls')),
    url(r'^login/', user_view.Login, name ='login'),
    url(r'^logout/', auth.LogoutView.as_view(template_name ='user / index.html'), name ='logout'),
    url(r'^register/', user_view.register, name ='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.handler404'
