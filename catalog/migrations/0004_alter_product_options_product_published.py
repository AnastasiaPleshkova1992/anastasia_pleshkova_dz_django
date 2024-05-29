# Generated by Django 4.2.2 on 2024-05-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_product_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["product_name", "category"],
                "permissions": [
                    ("can_cancel_puplication", "Может отменять публикацию"),
                    ("can_change_desription", "Может менять описание"),
                    ("can_change_category", "Может менять категорию"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="published",
            field=models.BooleanField(default=False, verbose_name="Опубликован"),
        ),
    ]
