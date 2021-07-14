from django.urls import path
from .views import HobbyCreateView, HobbyUpdateView, HobbyAddView, HobbyListView

app_name = 'hobby'

urlpatterns = [
    path('<int:pk>/create/', HobbyCreateView.as_view(), name='create_hobby'),
    path('<int:pk>/update', HobbyUpdateView.as_view(), name='update_hobby'),
    path('', HobbyListView.as_view(), name='hobbies_list'),
    path('add/', HobbyAddView.as_view(), name='add_hobby'),
]