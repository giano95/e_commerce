# Generated by Django 2.2.8 on 2020-08-20 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20200508_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='item.ItemCategory'),
        ),
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.ManyToManyField(related_name='color', to='item.ItemColor'),
        ),
        migrations.AlterField(
            model_name='item',
            name='images',
            field=models.ManyToManyField(related_name='images', to='item.ItemImage'),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantities_size',
            field=models.ManyToManyField(related_name='quantities_size', to='item.ItemQuantitySize'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(upload_to='item/img/'),
        ),
    ]
