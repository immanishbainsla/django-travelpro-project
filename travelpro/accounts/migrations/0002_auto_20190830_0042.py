# Generated by Django 2.2.3 on 2019-08-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(help_text='Enter your Email here.', max_length=254),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(help_text='Enter your Name here.', max_length=255),
        ),
    ]
