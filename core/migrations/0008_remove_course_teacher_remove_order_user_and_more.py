# Generated by Django 4.2.3 on 2023-07-09 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_studant_teacher_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Studant',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
