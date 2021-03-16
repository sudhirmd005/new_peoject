from django.urls import path
from . import views

urlpatterns = [
    path('country',views.index, name='index'),
    path('we_are_working_on_this', views.work, name='work'),
    path('country/states', views.states,name='states'),
    path('country/state/cities',views.city,name="city"),
    path('country/state/cities1',views.city1,name="city1"),
    path('country/state/cities2',views.city2,name="city2"),
    path('country/state/cities3',views.city3,name="city3"),
    path('country/state/cities4',views.city4,name="city4"),
    path('country/state/cities5',views.city5,name="city5"),
    path('country/state/cities6',views.city6,name="city6"),
    path('country/state/cities7',views.city7,name="city7"),
    path('country/state/cities8',views.city8,name="city8"),
    path('country/state/cities9',views.city9,name="city9"),

]