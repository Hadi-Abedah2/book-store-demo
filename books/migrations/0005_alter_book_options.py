# Generated by Django 4.2.6 on 2023-10-12 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_review_cover_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
