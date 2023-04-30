# Generated by Django 3.2.13 on 2022-11-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_movie',
            field=models.ManyToManyField(related_name='like_users', to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='user',
            name='like_review',
            field=models.ManyToManyField(related_name='like_users', to='movies.Review'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
