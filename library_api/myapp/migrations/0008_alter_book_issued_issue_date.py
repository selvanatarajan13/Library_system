# Generated by Django 5.0.3 on 2024-03-22 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_members_id_alter_book_issued_issue_bookauthor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issued',
            name='issue_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
