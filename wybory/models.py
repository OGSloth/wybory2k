# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Count, Sum


class MainCommune(models.Model):
    id = models.IntegerField(primary_key=True)
    county = models.CharField(max_length=32)
    area = models.IntegerField()
    name = models.CharField(max_length=255)
    subareas = models.IntegerField()
    people = models.IntegerField()
    cards = models.IntegerField()
    invalid = models.IntegerField()
    grabowski = models.IntegerField()
    ikonowicz = models.IntegerField()
    kalinowski = models.IntegerField()
    korwin = models.IntegerField()
    krzaklewski = models.IntegerField()
    kwasniewski = models.IntegerField()
    lepper = models.IntegerField()
    lopuszanski = models.IntegerField()
    olechowski = models.IntegerField()
    pawlowski = models.IntegerField()
    walesa = models.IntegerField()
    wilecki = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_commune'


#class countries:



class MetaCommune(models.Model):

    @staticmethod
    def get_votes():
        votes = MainCommune.objects.aggregate(
            GRABOWSKI=Sum('grabowski'),
            IKONOWICZ=Sum('ikonowicz'),
            KORWIN=Sum('korwin'),
            KALINOWSKI=Sum('kalinowski'),
            KRZAKLEWSKI=Sum('krzaklewski'),
            KWASNIEWSKI=Sum('kwasniewski'),
            LEPPER=Sum('lepper'),
            LOPUSZANSKI=Sum('lopuszanski'),
            OLECHOWSKI=Sum('olechowski'),
            PAWLOWSKI=Sum('pawlowski'),
            WALESA=Sum('walesa'),
            WILECKI=Sum('wilecki'),
            NIEWAZNE=Sum('invalid'),
        )
        return votes

    @staticmethod
    def get_county():
        counties_q = MainCommune.objects.all().values_list('county').distinct().annotate(n=models.Count("county"))
        counties = list()
        for v, k in counties_q:
            counties.append(v)
        return counties

    @staticmethod
    def get_votes_county(county):
        votes = MainCommune.objects.filter(county=county).aggregate(
            GRABOWSKI=Sum('grabowski'),
            IKONOWICZ=Sum('ikonowicz'),
            KORWIN=Sum('korwin'),
            KALINOWSKI=Sum('kalinowski'),
            KRZAKLEWSKI=Sum('krzaklewski'),
            KWASNIEWSKI=Sum('kwasniewski'),
            LEPPER=Sum('lepper'),
            LOPUSZANSKI=Sum('lopuszanski'),
            OLECHOWSKI=Sum('olechowski'),
            PAWLOWSKI=Sum('pawlowski'),
            WALESA=Sum('walesa'),
            WILECKI=Sum('wilecki'),
            NIEWAZNE=Sum('invalid'),
        )
        return votes

    @staticmethod
    def get_areas(county_name):
        areas = MainCommune.objects.filter(county=county_name).values('name').distinct()
        return areas.values('name').order_by('name')

    @staticmethod
    def get_subareas(area_name):
        subareas = MainCommune.objects.filter(name=area_name)
        return subareas

    @staticmethod
    def get_votes_subarea(subarea):
        votes = MainCommune.objects.filter(name=subarea).aggregate(
            GRABOWSKI=Sum('grabowski'),
            IKONOWICZ=Sum('ikonowicz'),
            KORWIN=Sum('korwin'),
            KALINOWSKI=Sum('kalinowski'),
            KRZAKLEWSKI=Sum('krzaklewski'),
            KWASNIEWSKI=Sum('kwasniewski'),
            LEPPER=Sum('lepper'),
            LOPUSZANSKI=Sum('lopuszanski'),
            OLECHOWSKI=Sum('olechowski'),
            PAWLOWSKI=Sum('pawlowski'),
            WALESA=Sum('walesa'),
            WILECKI=Sum('wilecki'),
            NIEWAZNE=Sum('invalid'),
        )
        return votes


    @staticmethod
    def get_areas_ids():
        areas = MainCommune.objects.values('area').distinct().values('area')
        return areas

    @staticmethod
    def get_votes_area(area_id):
        votes = MainCommune.objects.filter(area=area_id).aggregate(
            GRABOWSKI=Sum('grabowski'),
            IKONOWICZ=Sum('ikonowicz'),
            KORWIN=Sum('korwin'),
            KALINOWSKI=Sum('kalinowski'),
            KRZAKLEWSKI=Sum('krzaklewski'),
            KWASNIEWSKI=Sum('kwasniewski'),
            LEPPER=Sum('lepper'),
            LOPUSZANSKI=Sum('lopuszanski'),
            OLECHOWSKI=Sum('olechowski'),
            PAWLOWSKI=Sum('pawlowski'),
            WALESA=Sum('walesa'),
            WILECKI=Sum('wilecki'),
            NIEWAZNE=Sum('invalid'),
        )
        return votes