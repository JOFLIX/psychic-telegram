#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import models
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, ListView
from django.contrib.postgres.search import SearchVector
from app.models import Album, AlbumImage
from django.db.models import Q
from .models import Album
# from playhouse.sqlite_ext import SqliteExtDatabase
def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

    return render(request, 'gallery.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context

class SearchResultsView(DetailView):
    model = Album
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = AlbumImage.objects.filter(
        # slug__icontains=Album
        Q(tags__icontains=query)
            # Q(album=query) | Q(image=query)| Q(thumb=query)| Q(id=query)|Q(alt=query) |Q(album_id=query)|Q(slug=query)| Q(tags=query)
        )
        return object_list
    @classmethod
    def search_by_title(cls,search_term):
        albums = cls.objects.filter(title__icontains=search_term)
        return albums


def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

    def get_object(self):
        return get_object_or_404(User, pk=request.session['user_id'])
