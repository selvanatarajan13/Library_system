from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('save_json',views.save_json,name='save-json'),
    path('library/members',views.member),
    path('Add_new_member', views.Add_new_member),
    path('library/Create_new_book',views.Add_new_book),
    path('library/Add_new_member',views.Add_new_member),
    path('library/single_book_view/<int:pk>/',views.single_book_view,name='single_book_view'),
    path('library/single_member_view/<int:pk>/',views.single_member_view,name='single_member_view'),
    path('library/Update_book/<int:pk>/',views.update_book,name='update_book'),
    path('delete_book/<int:pk>/',views.delete_book, name='delete_book'),
    path('library//delete_member/<int:pk>/',views.delete_member, name='delete_member'),
    path('library/book_issue/<int:pk>/',views.book_issue,name='book_issue'),
    path('library/transaction',views.transaction_data),
]