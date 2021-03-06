# Generated by Django 2.0.3 on 2018-08-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCommune',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('county', models.CharField(max_length=32)),
                ('area', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('subareas', models.IntegerField()),
                ('people', models.IntegerField()),
                ('cards', models.IntegerField()),
                ('invalid', models.IntegerField()),
                ('grabowski', models.IntegerField()),
                ('ikonowicz', models.IntegerField()),
                ('kalinowski', models.IntegerField()),
                ('korwin', models.IntegerField()),
                ('krzaklewski', models.IntegerField()),
                ('kwasniewski', models.IntegerField()),
                ('lepper', models.IntegerField()),
                ('lopuszanski', models.IntegerField()),
                ('olechowski', models.IntegerField()),
                ('pawlowski', models.IntegerField()),
                ('walesa', models.IntegerField()),
                ('wilecki', models.IntegerField()),
            ],
            options={
                'db_table': 'main_commune',
                'managed': False,
            },
        ),
    ]
