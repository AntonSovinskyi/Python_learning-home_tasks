# Generated by Django 4.1.3 on 2022-11-29 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(default='', max_length=1000)),
                ('reminder', models.DateTimeField(verbose_name='date published')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_category', to='notes.categories')),
            ],
        ),
    ]
