from django.urls import path
from . import views

app_name="Automata"
urlpatterns=[
        path("",views.HomeView.as_view(),name="Home"),
        path("result/automata",views.ResultView.as_view(),name="result")
]