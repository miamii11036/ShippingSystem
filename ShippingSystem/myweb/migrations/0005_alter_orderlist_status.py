# Generated by Django 5.1.3 on 2024-12-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myweb", "0004_alter_orderdetail_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderlist",
            name="status",
            field=models.CharField(default="start", max_length=100),
        ),
    ]