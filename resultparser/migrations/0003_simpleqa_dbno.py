# Generated by Django 4.0 on 2021-12-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultparser', '0002_simpleqa_project_simpleqa_test_suite'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleqa',
            name='dbno',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
