from django.urls import path
from .views import HobbyAddView, HobbyListView

app_name = 'hobby'

urlpatterns = [
    path('', HobbyListView.as_view(), name='hobbies_list'),
    path('add/', HobbyAddView.as_view(), name='add_hobby'),
]