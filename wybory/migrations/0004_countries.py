# Generated by Django 2.0.3 on 2018-08-28 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wybory', '0003_contries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=30, unique=True)),
                ('subareas', models.IntegerField(blank=True, null=True)),
                ('uprawnieni', models.IntegerField(blank=True, null=True)),
                ('people', models.IntegerField(blank=True, null=True)),
                ('sent', models.IntegerField(blank=True, null=True)),
                ('invalid', models.IntegerField(blank=True, null=True)),
                ('valid', models.IntegerField(blank=True, null=True)),
                ('grabowski', models.IntegerField(blank=True, null=True)),
                ('ikonowicz', models.IntegerField(blank=True, null=True)),
                ('kalinowski', models.IntegerField(blank=True, null=True)),
                ('korwin', models.IntegerField(blank=True, null=True)),
                ('krzaklewski', models.IntegerField(blank=True, null=True)),
                ('kwasniewski', models.IntegerField(blank=True, null=True)),
                ('lepper', models.IntegerField(blank=True, null=True)),
                ('lopuszanski', models.IntegerField(blank=True, null=True)),
                ('olechowski', models.IntegerField(blank=True, null=True)),
                ('pawlowski', models.IntegerField(blank=True, null=True)),
                ('walesa', models.IntegerField(blank=True, null=True)),
                ('wilecki', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'countries',
            },
        ),
    ]
