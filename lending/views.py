from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from lending.models import Book, Loan
from lending.forms import BorrowForm, ReturnForm
from lending.services.loan_service import LoanService
from lending.services.exceptions import NoCopiesError, MaxLoansExceededError, AlreadyReturnedError

class BookListView(ListView):
    model = Book
    template_name = "lending/book_list.html"
    context_object_name = "books"

class LoanDetailView(DetailView):
    model = Loan
    template_name = "lending/loan_detail.html"

class BorrowBookView(FormView):
    template_name = "lending/book_list.html"

    def form_valid(self, form):
        svc = LoanService()
        try:
            svc.borrow(form.cleaned_data["book"].id, form.cleaned_data["member"].id)
        except (NoCopiesError, MaxLoansExceededError) as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
        return super().form_valid(form)

class ReturnBookView(FormView):
    template_name = "lending/loan_detail.html"
    form_class = ReturnForm
    success_url = reverse_lazy("lending:book_list")

    def form_valid(self, form):
        svc = LoanService()
        try:
            svc.return_loan(form.cleaned_data["loan"].id)
        except AlreadyReturnedError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
        return super().form_valid(form)