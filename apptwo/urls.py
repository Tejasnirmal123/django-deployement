from django.urls import path,include
from apptwo import views

urlpatterns=[

     path("",views.users,name='users'),
     #path(""'first_app'/include('first_app.urls')),
]