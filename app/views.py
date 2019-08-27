#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import models
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, ListView
from django.contrib.postgres.search import SearchVector
from app.models import Album, AlbumImage
from django.db.models import F
from django.db.models import Q
from .models import Album

search_vector = SearchVector('album_text', 'album_tags')

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

        def __str__(self):
            return self.name

# class SearchResultsView(DetailView):
#     # """
#     # Render a "detail" view of an object.
#     #
#     # By default this is a model instance looked up from `self.queryset`, but the
#     # view will support display of *any* object by overriding `self.get_object()`.
#     # """

#     model = Album
#     template_name = 'search_results.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         object_list = AlbumImage.objects.filter(
#             Q(album=query) | Q(image=query)| Q(thumb=query)| Q(id=query)|Q(alt=query) |Q(album_id=query)|Q(slug=query)| Q(alt=query)
#         )
#         return object_list
class SearchResultsView(ListView):
    model = AlbumImage
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Album.image.filter(
            Q(album__icontains=query) | Q(image__icontains=query)
        )
        return object_list
# Author.objects.filter(
# name__contains='Terry'
# ).values_list('name', flat=True)

    def __str__(self):
        return self.name
# Album.objects.filter(
# tags__contains='tags'
# ).values_list('tags', flat=True)
#Trying vector serching using DRY principles to enable multiple field search
# tags_vector = SearchVector('tags')
# category_title_vector = SearchVector('category__title')
# Album.objects.annotate(search=F('tags') + F('title')).filter(search='')

def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

    def get_object(self):
        return get_object_or_404(User, pk=request.session['user_id'])
