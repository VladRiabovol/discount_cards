from django.urls import path
from management_discount_cards import views

urlpatterns = [
    path('all_cards/', views.CardsListView.as_view(), name='cards-list'),
    path('card/<int:pk>/', views.CardDetailView.as_view(), name='card-detail'),
    path('delete_page/', views.delete_page, name='delete-page'),
    path('search_page/', views.search_page, name='search-page'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('change_status/', views.change_status, name='change-status'),
    path('cards_api/', views.CardAPIListView.as_view(), name='cards_api'),
]

