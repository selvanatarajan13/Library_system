from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .forms import AddBookForm,UpdateBookForm,AddMemberForm,IssuedBookForm
from .models import *
from datetime import datetime, timedelta, date
from django.core.exceptions import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# Create your views here.

def header(request):
    return render(request, 'header.html',{})


# The below function handles incoming JSON data and saves it to the database.
@csrf_exempt
def save_json(request):
    if request.method == "POST":
        json_payload = json.loads(request.body)
        bookID = json_payload.get('bookID')
        title = json_payload.get('title')
        authors = json_payload.get('authors')
        average_rating = json_payload.get('average_rating')
        isbn = json_payload.get('isbn')
        isbn13 = json_payload.get('isbn13')
        language_code = json_payload.get('language_code')
        num_pages = json_payload.get('num_pages')
        ratings_count = json_payload.get('ratings_count')
        text_reviews_count = json_payload.get('text_reviews_count')
        publication_date = json_payload.get('publication_date')
        publisher = json_payload.get('publisher')

        book = Book.objects.create(
            bookID=bookID,
            title=title,
            authors=authors,
            average_rating=average_rating,
            isbn=isbn,
            isbn13=isbn13,
            language_code=language_code,
            num_pages=num_pages,
            ratings_count=ratings_count,
            text_reviews_count=text_reviews_count,
            publication_date=publication_date,
            publisher=publisher
        )
    return HttpResponse('JSON data was saved successfully!')

# CRUD Operations

# Fetch the Data
# Book data

def index(request):
    searched = ''
    tot_book = 0
    book_not = ''
    Books_data = Book.objects.all()
    p = Paginator(Books_data, 8)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    if 'search' in request.POST:
        searched = request.POST['search']
        page_obj = Book.objects.filter(title__contains = searched)
        if not page_obj:
            book_not = 'Book not available..'
    else:
        tot_book = len(Books_data)
    
    context = {'data' : page_obj, 'tot_book':tot_book, 'book_not':book_not}
    return render(request, 'library/index.html', context)

# Member data

def member(request):
    searched = ''
    if 'search' in request.POST:
        searched = request.POST['search']
        member_data = members.objects.filter(member_name__icontains = searched)
        if not member_data:
            member_data = "Book not available"
    else:
        member_data = members.objects.all()
    
    context = {'data' : member_data}

    return render(request, 'library/members.html', context) 


# Create Operation
# Book

def Add_new_book(request):
    form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    context = {'form':form}
    return render(request,'library/Add_new_book.html',context=context)


# Add Member
def Add_new_member(request):
    form = AddMemberForm()
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/library/members')
        else:
            return redirect('/library/members')
    context = {'form':form}
    return render(request,'library/Add_new_member.html',context=context)

# Read operation
# single data fetch (Read)
    
def single_book_view(request,pk):
    if request.method == "GET":
        single_record = Book.objects.get(bookID=pk)
        context = {'data':single_record}
    return render(request, 'library/single_book_view.html',context=context)


def single_member_view(request,pk):
    if request.method == "GET":
        single_record = members.objects.get(memberId=pk)
        try:
            book_data = Book_Issued.objects.filter(memberId=pk)
        except Book_Issued.DoesNotExist:
            book_data = "No books rental."
        context = {'data':single_record,'book_data':book_data}
    return render(request, 'library/single_member_view.html',context=context)


# Update Operation
# Book
def update_book(request,pk):
    record = Book.objects.get(bookID=pk)
    form = UpdateBookForm(instance=record)
    if request.method == "POST":
        form = UpdateBookForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/readers')
    context = {'form':form}
    return render(request,'library/Update_book.html',context=context)


# Delete Operation
# Book
def delete_book(request,pk):
    record = Book.objects.get(bookID = pk)
    record.delete()    
    return redirect('/')



# Member
def delete_member(request,pk):
    record = members.objects.get(memberId = pk)
    record.delete()   
    return redirect('/library/members')



# Book issue
def book_issue(request, pk):
    record = Book.objects.get(bookID=pk)
    mem_record = members.objects.all()
    form = IssuedBookForm()
    rent_fees = 50
    maximum_debt = 500

    if request.method == 'POST':
        form = IssuedBookForm(request.POST)
        if form.is_valid():
            # Get input data from the form
            issue_BookId = request.POST.get('issue_BookId')
            issue_BookTitle = request.POST.get('issue_BookTitle')
            issue_BookAuthor = request.POST.get('issue_BookAuthor')
            issue_BookIsbn = request.POST.get('issue_BookIsbn')
            memberId = request.POST.get('memberId')
            issue_MemberName = request.POST.get('issue_MemberName')
            return_date = request.POST.get('return_date')

            # Check if the member exists
            try:
                member = members.objects.get(memberId=memberId)
                existing_transactions = Book_Issued.objects.filter(memberId=memberId).count()

                if existing_transactions >= 2:
                    return render(request, 'library/transaction_limit_exceeded.html')
                    
            except members.DoesNotExist:
                # Member doesn't exist, display an error message
                return render(request, 'library/member_not_found.html')

            # Create and save the Book_Issued object
            obj = Book_Issued()
            obj.issue_BookId = issue_BookId
            obj.issue_BookTitle = issue_BookTitle
            obj.issue_BookAuthor = issue_BookAuthor
            obj.issue_BookIsbn = issue_BookIsbn
            obj.memberId = memberId
            obj.issue_MemberName = issue_MemberName
            obj.return_date = datetime.now() + timedelta(int(return_date))   
            obj.rent_fee = rent_fees
            obj.save()

            return redirect('/library/transaction')
        else:
            return render(request, 'library/members.html')

    context = {'form': record, 'mem_record': mem_record}
    return render(request, 'library/book_issue.html', context=context)


# Transaction
def transaction_data(request):
    searched = ''
    tot_transaction = []
    book_not = ''
    ack = ''
    fine = 0
    return_date_limit = 10
    maximum_debt = 500
    transaction_data = Book_Issued.objects.all()

    if 'search' in request.POST:
        searched = request.POST['search']
        transaction_data = Book_Issued.objects.filter(issue_MemberName__contains = searched)
        tot_transaction.append(transaction_data)
        tot_transaction = len(transaction_data)

        if not transaction_data:
            book_not = 'no transaction'
    else:
        tot_transaction = len(transaction_data)
        if not transaction_data:
            ack = "No record found."

    today_date = datetime.now().date()
    for transaction in transaction_data:      
        if transaction.return_date < today_date:
            days = (today_date - transaction.return_date).days
            transaction.fine = days * 10
        
        else:
            transaction.fine = 0
        # total outstanding amount calculation
        transaction.total_debt = transaction.fine + transaction.rent_fee
        transaction.save()
        
        if transaction.total_debt > maximum_debt:  
            transaction.total_debt = maximum_debt  
        transaction.save()
    
    context = {'data' : transaction_data, 'tot_transaction':tot_transaction, 'book_not':book_not,'ack':ack}    
    return render(request, 'library/transaction.html', context)