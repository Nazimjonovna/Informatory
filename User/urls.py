from django.urls import path
from .views import Clientview, ClientsGetView, ClientPostView, LoginWorkersView

urlpatterns = [
    path('client_get/<str:email>/', Clientview.as_view()),
    path('client_post/', ClientPostView.as_view()),
    path('gets/', ClientsGetView.as_view()),
    path('workers_login/', LoginWorkersView.as_view()),
]