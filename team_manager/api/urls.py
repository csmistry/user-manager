from django.urls import path

from .views import MemberDelete, MembersList, MemberCreate, MemberEdit

urlpatterns = [
    path('', MembersList.as_view(), name='members'),
    path('member-create/', MemberCreate.as_view(), name='member-create'),
    path('member-edit/<int:pk>', MemberEdit.as_view(), name='member-edit'),
    path('member-delete/<int:pk>', MemberDelete.as_view(), name='member-delete'),

]