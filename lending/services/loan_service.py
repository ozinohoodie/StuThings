from django.conf import settings
from django.db import transaction
from lending.models import Book, Member, Loan
from .exceptions import NoCopiesError, MaxLoansExceededError, AlreadyReturnedError

class LoanService:
    """Orchestrates borrowing and returning with transactional safety."""

    def __init__(self, max_loans: int | None = None):
        self.max_loans = max_loans or getattr(settings, "MAX_ACTIVE_LOANS_PER_MEMBER", 1)

    @transaction.atomic
    def borrow(self, book_id: int, member_id: int) -> Loan:
        # TODO: select_for_update on Book, fetch Member
        # TODO: if no copies -> raise NoCopiesError
        # TODO: if member has >= max_loans -> raise MaxLoansExceededError
        # TODO: book.take_one(); save; create Loan; return it
        ...

    @transaction.atomic
    def return_loan(self, loan_id: int) -> Loan:
        # TODO: select_for_update on Loan
        # TODO: if returned -> raise AlreadyReturnedError
        # TODO: mark_returned; increment book; save; return
        ...
