# Generated by Django 4.1.2 on 2022-10-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_alter_documentimage_options_add_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAuthorProperty',
            fields=[
                ('id', models.AutoField(db_column='RecordID', primary_key=True, serialize=False)),
                ('wikidata_id', models.CharField(db_column='WikidataID', max_length=100)),
                ('personal_author_name', models.CharField(db_column='PersonalAuthorName', max_length=200)),
                ('honorific', models.CharField(blank=True, db_column='Honorific', max_length=100)),
                ('personal_author_description', models.CharField(db_column='PersonalAuthorDescription', max_length=1000)),
                ('name', models.CharField(db_column='Property', max_length=100)),
                ('value', models.CharField(db_column='Entity', max_length=200)),
                ('qualifier', models.CharField(db_column='Qualifier', max_length=100)),
                ('qualifier_value', models.CharField(db_column='QualValue', max_length=200)),
                ('load_timestamp', models.DateTimeField(db_column='LoadTimestamp')),
            ],
            options={
                'verbose_name_plural': 'Personal author properties',
                'db_table': 'tblNurAuthorsWikidataPropertiesAndQualifiers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalAuthorPropertyRank',
            fields=[
                ('id', models.AutoField(db_column='RecordID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Property', max_length=200, unique=True)),
                ('instance_count', models.IntegerField(db_column='InstanceCount')),
                ('rank', models.IntegerField(db_column='PropertyRank')),
                ('load_timestamp', models.DateTimeField(db_column='LoadTimeStamp')),
            ],
            options={
                'db_table': 'tblNurAuthorsWikidataPropertiesRanked',
                'managed': False,
            },
        ),
    ]
