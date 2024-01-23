from django.urls import path
from watchlist_app.api import views

# urlpatterns = [
#     path('list/',views.movie_list,name='movie_list'),
#     path('<int:pk>',views.movie_detail,name='movie_detail'),
# ]

urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',views.WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',views.StreamPlatformAV.as_view(),name='streamplatform-list'),
    path('stream/<int:pk>',views.StreamPlatformDeatilAV.as_view(),name='streamplatform-detail'),
]