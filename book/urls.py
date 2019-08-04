from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.Contacts.as_view(), name='contact'),
    path('contact/create', views.Create.as_view(), name='create'),
    path('contact/edit', views.Edit.as_view(), name='edit'),
    path('contact/delete', views.Delete.as_view(), name='delete'),
]
