# Generated by Django 5.0.7 on 2024-08-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esewaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
