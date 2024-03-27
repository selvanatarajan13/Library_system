from django import forms
from .models import Book, members, Book_Issued


# Adding or Create a new records

class AddBookForm(forms.ModelForm):
    
    class Meta:

        model = Book
        fields = ['bookID','title','authors','average_rating','isbn','isbn13','language_code','num_pages','ratings_count','text_reviews_count','publisher']

# update the book records

class UpdateBookForm(forms.ModelForm):
    
    class Meta:

        model = Book
        fields = ['bookID','title','authors','average_rating','isbn','isbn13','language_code','num_pages','ratings_count','text_reviews_count','publisher']

# Add the new member records

class AddMemberForm(forms.ModelForm):

    class Meta:

        model = members
        fields = ['memberId','member_name','contact','place','no_of_rental']


# update the member records

class UpdateMemberForm(forms.ModelForm):

    class Meta:

        model = members
        fields = ['memberId','member_name','contact','place','no_of_rental']


class IssuedBookForm(forms.ModelForm):

    class Meta:

        model = Book_Issued
        fields = ['issue_BookId','issue_BookTitle','issue_BookAuthor','issue_BookIsbn','memberId','issue_MemberName']