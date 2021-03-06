from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from .models import MetaCommune, MetaCountries


def index(request):
    try:
        countries = MetaCountries.get_countries()
        template = loader.get_template('index.html')
        votes = MetaCommune.get_votes()
        suma = 0
        areas_ids = MetaCommune.get_areas_ids()
        for v, k in votes.items():
            suma = suma + k
        percent = dict()
        for v,k in votes.items():
            value = float(100 * k / suma)
            value = "%.2f" % value
            percent[v] = (k, value)
        counties = MetaCommune.get_county()
        pol_map_url = "https://i.imgur.com/CMqffTQ.png"
        context = {
            'votes': votes,
            'suma': suma,
            'percent': percent,
            'counties': counties,
            'areas_ids': areas_ids,
            'countries': countries,
            'pol_map_url': pol_map_url,
        }
    except Exception:
        raise Http404
    return HttpResponse(template.render(context, request))


def county(request, county_name):
    try:
        countries = MetaCountries.get_countries()
        template = loader.get_template('county.html')
        votes = MetaCommune.get_votes_county(county_name)
        suma=0
        areas_ids = MetaCommune.get_areas_ids()
        print(county_name)
        areas = MetaCommune.get_areas(county_name)
        for v, k in votes.items():
            suma = suma + k
        percent = dict()
        for v, k in votes.items():
            value = float(100 * k / suma)
            value = "%.2f" % value
            percent[v] = (k, value)
        counties = MetaCommune.get_county()

        context = {
            'votes': votes,
            'suma': suma,
            'percent': percent,
            'counties': counties,
            'county_name': county_name,
            'areas': areas,
            'areas_ids': areas_ids,
            'countries': countries
        }
    except Exception:
        raise Http404
    return HttpResponse(template.render(context, request))


def subarea(request, county_name, subarea_name):
    try:
        countries = MetaCountries.get_countries()
        template = loader.get_template('areas.html')
        votes = MetaCommune.get_votes_subarea(subarea_name)
        suma=0
        areas_ids = MetaCommune.get_areas_ids()
        areas = MetaCommune.get_areas(county_name)
        for v, k in votes.items():
            suma = suma + k
        percent = dict()
        for v, k in votes.items():
            value = float(100 * k / suma)
            value = "%.2f" % value
            percent[v] = (k, value)
        counties = MetaCommune.get_county()

        context = {
            'votes': votes,
            'suma': suma,
            'percent': percent,
            'counties': counties,
            'county_name': county_name,
            'areas': areas,
            'areas_ids': areas_ids,
            'subarea_name': subarea_name,
            'countries': countries
        }
    except Exception:
        raise Http404
    return HttpResponse(template.render(context, request))


def areas(request, area_id):
    try:
        countries = MetaCountries.get_countries()
        template = loader.get_template('areas.html')
        votes = MetaCommune.get_votes_area(area_id)
        suma = 0
        areas_ids = MetaCommune.get_areas_ids()
        for v, k in votes.items():
            suma = suma + k
        percent = dict()
        for v, k in votes.items():
            value = float(100 * k / suma)
            value = "%.2f" % value
            percent[v] = (k, value)
        counties = MetaCommune.get_county()
        context = {
            'votes': votes,
            'suma': suma,
            'percent': percent,
            'counties': counties,
            'areas_ids': areas_ids,
            'area_id': area_id,
            'countries': countries
        }
    except Exception:
        raise Http404
    return HttpResponse(template.render(context, request))


def country(request, country_name):
    try:
        countries = MetaCountries.get_countries()
        template = loader.get_template('areas.html')
        votes = MetaCountries.get_votes(country_name)
        suma=0
        areas_ids = MetaCommune.get_areas_ids()
        for v, k in votes.items():
            suma = suma + k
        percent = dict()
        for v, k in votes.items():
            value = float(100 * k / suma)
            value = "%.2f" % value
            percent[v] = (k, value)
        counties = MetaCommune.get_county()

        context = {
            'votes': votes,
            'suma': suma,
            'percent': percent,
            'counties': counties,
            'areas': areas,
            'areas_ids': areas_ids,
            'countries': countries,
            'country_name': country_name
        }
    except Exception:
        raise Http404
    return HttpResponse(template.render(context, request))