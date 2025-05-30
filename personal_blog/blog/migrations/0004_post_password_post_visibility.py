# Generated by Django 5.2 on 2025-04-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'Publiczny'), ('private', 'Prywatny (chroniony hasłem)')], default='public', max_length=10),
        ),
    ]
