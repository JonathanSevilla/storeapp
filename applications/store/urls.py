from django.urls import path, include, re_path
from . import views

urlpatterns = [  
    path('brands/', views.brands),
    path('stores/', views.store),
    path('deals/', views.deals),
    path('post-subscriptions/', views.post_subscriptions),
    path('subscriptions/<int:store_id>/users/', views.UserListByStoreView.as_view(), name='users-by-store'),
]