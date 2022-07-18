from django.urls import path

from .views import MembersList, MemberDetail, MemberCreate

urlpatterns = [
    path('', MembersList.as_view(), name='members'),
    path('member/<int:pk>', MemberDetail.as_view(), name='member'),
    path('member-create/', MemberCreate.as_view(), name='member-create'),

]