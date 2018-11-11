# Generated by Django 2.1.2 on 2018-11-11 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HappyPaws', '0004_boarding'),
    ]

    operations = [
        migrations.CreateModel(
            name='grooming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=128)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HappyPaws.dog')),
            ],
        ),
    ]
