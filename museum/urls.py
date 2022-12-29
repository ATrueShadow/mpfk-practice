from django.urls import path
from . import views

urlpatterns = [
    # views for everyone
    path('', views.ToursIndexListView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('tour/<int:pk>', views.TourIndexDetailView.as_view(), name='tour-info'),

    # views & actions for visitors and staff
    path('tickets/', views.TicketListView.as_view(), name='tickets'),
    path('tickets/view/<int:pk>', views.TicketDetailView.as_view(), name='ticket-manage'),
    path('tickets/update/<int:pk>', views.TicketUpdateView.as_view(), name='ticket-update'),
    path('tickets/delete/<int:pk>', views.TicketDeleteView.as_view(), name='ticket-delete'),
    path('tickets/new', views.TicketNewView.as_view(), name='ticket-new'),

    path('tours/', views.ToursListView.as_view(), name='tours'),
    path('tours/<int:pk>', views.TourDetailView.as_view(), name='tour-manage'),
    path('tours/update/<int:pk>', views.TourUpdateView.as_view(), name='tour-update'),
    path('tours/delete/<int:pk>', views.TourDeleteView.as_view(), name='tour-delete'),
    path('tours/new', views.TourNewView.as_view(), name='tour-new'),

    path('exhibitions/', views.ExhibitionListView.as_view(), name='exhibitions'),
    path('exhibitions/view/<int:pk>', views.ExhibitionDetailView.as_view(), name='exhibition-manage'),
    path('exhibitions/update/<int:pk>', views.ExhibitionUpdateView.as_view(), name='exhibition-update'),
    path('exhibitions/delete/<int:pk>', views.ExhibitionDeleteView.as_view(), name='exhibition-delete'),
    path('exhibitions/new', views.ExhibitionNewView.as_view(), name='exhibition-new'),

    path('storage', views.StorageListView.as_view(), name='storage'),
    path('storage/view/<int:pk>', views.StorageDetailView.as_view(), name='storage-manage'),
    path('storage/update/<int:pk>', views.StorageUpdateView.as_view(), name='storage-update'),
    path('storage/delete/<int:pk>', views.StorageDeleteView.as_view(), name='storage-delete'),
    path('storage/new', views.StorageNewView.as_view(), name='storage-new'),

    # buying tickets
    path('tickets/buy', views.BuyTicketView.as_view(), name='buy-ticket'),
]