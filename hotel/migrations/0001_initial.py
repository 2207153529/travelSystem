# Generated by Django 2.2 on 2020-05-12 12:01

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/%Y%m%d/')),
                ('name', models.TextField()),
                ('score', models.TextField()),
                ('msg', models.TextField()),
                ('price', models.FloatField()),
                ('addr', models.TextField()),
                ('href', models.TextField()),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
