from django.urls import path
from .views import (Clientview, ClientsGetView, ClientPostView, LoginWorkersView, UniverGetView,
                    UniversityView, UniversityGet, GetConsulting, GetConsultings, GetConsultClients)

urlpatterns = [
    path('client_get/<str:email>/', Clientview.as_view()), #url for sreach one student
    path('client_post/', ClientPostView.as_view()), # url for add new student
    path('gets/', ClientsGetView.as_view()), # urls for get all students for consult
    path('workers_login/', LoginWorkersView.as_view()), # url for login workers
    path('getUniver/', UniverGetView.as_view()), # url for get all students for univer(without contacts)
    path("addUniver/", UniversityView.as_view()), # url for add new universities
    path("univers/", UniversityGet.as_view()), # url for get universities for choisefield
    path("consulting/", GetConsulting.as_view()), # url for get one consulting data
    path("consultings/", GetConsultings.as_view()), # url for get all consulting data
    path("cunsilting_clients/", GetConsultClients.as_view()), # url for get all clients for one consulting
]