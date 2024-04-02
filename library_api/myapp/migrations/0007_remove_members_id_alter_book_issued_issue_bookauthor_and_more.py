# Generated by Django 5.0.3 on 2024-03-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_issue_memberid_book_issued_memberid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='id',
        ),
        migrations.AlterField(
            model_name='book_issued',
            name='issue_BookAuthor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book_issued',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='memberId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='members',
            name='member_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='members',
            name='place',
            field=models.CharField(max_length=50),
        ),
    ]