# Generated by Django 2.1.2 on 2018-11-11 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HappyPaws', '0005_grooming'),
    ]

    operations = [
        migrations.CreateModel(
            name='pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('days_of_stay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HappyPaws.boarding')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HappyPaws.dog')),
            ],
        ),
    ]
