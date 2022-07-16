from django.urls import path

from . import views

urlpatterns = [
    path('members', views.ListMembersView.as_view())
]