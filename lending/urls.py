from django.urls import path
from .views import BookListView, LoanDetailView, BorrowBookView, ReturnBookView

app_name = "lending"
urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("loans/<int:pk>/", LoanDetailView.as_view(), name="loan_detail"),
    path("borrow/", BorrowBookView.as_view(), name="borrow"),
    path("return/", ReturnBookView.as_view(), name="return"),

]