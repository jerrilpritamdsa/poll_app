# Generated by Django 3.0.8 on 2020-07-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=20)),
                ('option_two', models.CharField(max_length=20)),
                ('option_three', models.CharField(max_length=20)),
                ('count_one', models.IntegerField(default=0)),
                ('count_two', models.IntegerField(default=0)),
                ('count_three', models.IntegerField(default=0)),
            ],
        ),
    ]
