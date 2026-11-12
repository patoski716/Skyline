from django.urls import path
from .views import (ContactCreate,ContactView,ContactUpdate,ContactDelete)

urlpatterns = [
    path('postcontact/', ContactCreate.as_view(),name='contact'),
    path('viewcontact/', ContactView.as_view(),name='contact-view'),
    path('updatecontact/<int:pk>/', ContactUpdate.as_view(),name='contact-update'),
    path('deletecontact/<int:pk>/', ContactDelete.as_view(),name='contact-delete'),
]