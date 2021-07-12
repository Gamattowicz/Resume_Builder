from django.urls import path
from .views import HobbyCreateView, HobbyAddView, HobbyListView

app_name = 'hobby'

urlpatterns = [
    path('create/', HobbyCreateView.as_view(), name='create_hobby'),
    path('', HobbyListView.as_view(), name='hobbies_list'),
    path('add/', HobbyAddView.as_view(), name='add_hobby'),
]