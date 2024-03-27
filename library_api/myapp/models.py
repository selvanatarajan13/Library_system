from django.db import models
import json

# Create your models here.


# Book model

class Book(models.Model):

    bookID = models.IntegerField(primary_key=True)
    title = models.CharField(blank=True,max_length=200)
    authors = models.CharField(blank=True,max_length=200)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    isbn = models.IntegerField()
    isbn13 = models.IntegerField()
    language_code = models.CharField(max_length=20)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField(auto_now_add=True)
    publisher = models.CharField(blank=True,max_length=100)

    # show the author name on database
    def __str__(self):
        return self.authors

# member model

class members(models.Model):

    memberId = models.IntegerField(primary_key=True)
    member_name = models.CharField(max_length=20)
    contact = models.IntegerField(blank=False)
    place = models.CharField(max_length=50)
    no_of_rental = models.CharField(max_length=20)

    # show the author name on database

    def __str__(self):
        return self.member_name


class Book_Issued(models.Model):

    id = models.AutoField(primary_key=True)

    issue_BookId = models.IntegerField(blank=False)
    issue_BookTitle = models.CharField(blank=False,max_length=200)
    issue_BookAuthor = models.CharField(blank=False,max_length=50)
    issue_BookIsbn = models.IntegerField()

    memberId = models.IntegerField(blank=False)
    issue_MemberName = models.CharField(max_length=255)

    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    fine = models.IntegerField(default=0)
    rent_fee = models.IntegerField(blank=False,default=0)
    total_debt = models.IntegerField(default=0)

    def __str__(self):
        return self.issue_MemberName