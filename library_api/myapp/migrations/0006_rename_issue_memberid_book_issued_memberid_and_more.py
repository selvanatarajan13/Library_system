# Generated by Django 5.0.3 on 2024-03-21 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_book_issued_return_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_issued',
            old_name='issue_MemberId',
            new_name='memberId',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='reference_id',
            new_name='memberId',
        ),
    ]