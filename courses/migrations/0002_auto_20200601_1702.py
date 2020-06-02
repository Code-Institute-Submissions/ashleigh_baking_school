# Generated by Django 3.0.6 on 2020-06-01 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='course',
            name='day',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_list3',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo_course',
            field=models.ImageField(upload_to='media/photos/'),
        ),
    ]