import json
from .models import Car, Make, Model, SubModel
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render

from django.http import Http404, HttpResponse

#from infinite_scroll_pagination import paginator
#from infinite_scroll_pagination import serializers
#
#
# def pagination_ajax(request):
#     if not request.is_ajax():
#         return Http404()
#
#     try:
#         value, pk = serializers.page_key(request.GET.get('p', ''))
#     except serializers.InvalidPage:
#         return Http404()
#
#     try:
#         page = paginator.paginate(
#             query_set=Car.objects.all(),
#             lookup_field='registered_day',
#             value=value,
#             pk=pk,
#             per_page=20,
#             move_to=paginator.NEXT_PAGE)
#     except paginator.EmptyPage:
#         data = {'error': "this page is empty"}
#     else:
#         data = {
#             'articles': [{'title': article.title} for article in page],
#             'has_next': page.has_next(),
#             'has_prev': page.has_previous(),
#             'next_objects_left': page.next_objects_left(limit=100),
#             'prev_objects_left': page.prev_objects_left(limit=100),
#             'next_pages_left': page.next_pages_left(limit=100),
#             'prev_pages_left': page.prev_pages_left(limit=100),
#             'next_page': serializers.to_page_key(**page.next_page()),
#             'prev_page': serializers.to_page_key(**page.prev_page())}
#
#     return HttpResponse(json.dumps(data), content_type="application/json")
#
# def show_genres(request):
#     return render(request, "search/index.html", {'genres': Make.objects.all()})


class IndexView(generic.ListView):
    model = 'Make'
    template_name = 'search/index.html'
    context_object_name = 'make'
    #
    # def get_queryset(self):
    #     return Car.objects.order_by('-pub_date')[:5]
    #
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['model'] = Model.objects.all()
        return context

    def get_queryset(self):
        return Model.objects.all()
    #
    #     return render(request, '/category_list.html', {'categories': categories})

class SearchView(generic.ListView):
    template_name = 'search/search_list.html'
    context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]
#
class DetailView(generic.DetailView):
    model = Model
    template_name = 'search/detail.html'
#

class ResultsView(generic.ListView):
    model = Model
    template_name = 'search/results.html'