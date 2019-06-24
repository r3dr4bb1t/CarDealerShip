from django.urls import path

from . import views


app_name = 'search'
urlpatterns = [
   # path('', views.show_genres, name='index'),
    path('', views.IndexView.as_view(), name='index' ),
    path('make/<int:pk>', views.ResultsView.as_view(), name='results'),
    path('make/<int:pk>/model/<int:pk>', views.ResultsView.as_view(), name='results'),
#    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
