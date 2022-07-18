from django.urls import path

from .views import MembersList, MemberDetail

urlpatterns = [
    path('', MembersList.as_view(), name='members'),
    path('member/<int:pk>', MemberDetail.as_view(), name='member'),

]