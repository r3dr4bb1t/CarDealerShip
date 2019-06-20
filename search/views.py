from .models import Car
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
# Create your views here.


class IndexView(generic.ListView):
    model = Car
    template_name = 'search/index.html'


class SearchView(generic.ListView):
    template_name = 'search/search_list.html'
    context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]
#
class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'