# Generated by Django 3.2 on 2021-04-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('description', models.TextField()),
                ('image', models.ImageField(default='', height_field='height_field', upload_to='images_dir', width_field='width_field')),
                ('height_field', models.PositiveIntegerField(default=0)),
                ('width_field', models.PositiveIntegerField(default=0)),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=8, max_digits=9)),
            ],
            options={
                'verbose_name': 'Набор',
                'verbose_name_plural': 'Наборы',
            },
        ),
    ]
