from django.urls import path,include
from watchlist_app.api import views

from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('list/',views.movie_list,name='movie_list'),
#     path('<int:pk>',views.movie_detail,name='movie_detail'),
# ]

router = DefaultRouter()
router.register(r'stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',views.WatchDetailAV.as_view(),name='movie-detail'),
    
    path('', include(router.urls)),
    
    # path('stream/',views.StreamPlatformAV.as_view(),name='streamplatform-list'),
    # path('stream/<int:pk>',views.StreamPlatformDeatilAV.as_view(),name='streamplatform-detail'),
    
    # path('review/',views.ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),
    
    path('stream/<int:pk>/review-create/',views.ReviewCreate.as_view(),name='review-list'),
    path('stream/<int:pk>/review/',views.ReviewList.as_view(),name='review-create'),
    path('stream/review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),
    

]