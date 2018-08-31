from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('county/<county_name>/', views.county, name='county'),
    path('subarea/<county_name>/<subarea_name>', views.subarea, name='subarea'),
    path('areas/<area_id>/', views.areas, name='areas'),
    path('country/<country_name>', views.country, name="country")
]
