# Generated by Django 4.2.6 on 2023-10-23 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="cart creation date"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="collection name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="first name"),
                ),
                (
                    "family_name",
                    models.CharField(max_length=255, verbose_name="family name"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                ("phone", models.CharField(max_length=20, verbose_name="Phone Number")),
                (
                    "birth_date",
                    models.DateField(null=True, verbose_name="date of birth"),
                ),
                (
                    "membership",
                    models.CharField(
                        choices=[("b", "bronze"), ("s", "silver"), ("g", "gold")],
                        default="b",
                        max_length=1,
                        verbose_name="membership level",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Promotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="promotion name"),
                ),
                ("discount", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="product title"),
                ),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("inventory", models.IntegerField()),
                ("last_update", models.DateTimeField(auto_now=True)),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.collection",
                    ),
                ),
                ("promotions", models.ManyToManyField(to="store.promotion")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "placed_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Time of order placement"
                    ),
                ),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("f", "failed"), ("c", "complete"), ("p", "pending")],
                        default="p",
                        max_length=1,
                        verbose_name="payment status",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.customer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.cart"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="store.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "street",
                    models.CharField(max_length=255, verbose_name="street address"),
                ),
                ("city", models.CharField(max_length=255, verbose_name="city")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.customer"
                    ),
                ),
            ],
        ),
    ]
