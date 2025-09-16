from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    copies_available = models.PositiveIntegerField(default=1)

    #TODO: return True if a copy can be borrowed
    def can_borrow(self) -> bool:
        ...

    #TODO: copies reduced or increased or have an Error for no copies
    def take_one(self) -> None:
        ...

    #TODO: increasing of copies
    def put_back_one(self) -> None:
        ...

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    #TODO: Count active loans for the member
    def active_loans_count(self) -> int:
        ...

class LoanQuerySet(models.QuerySet):
        def active(self):
            return self.filter(returned_at__isnull=True)

class LoanManager(models.Manager):
        def get_queryset(self):
            return LoanQuerySet(model=self.model, using=self._db)
        def active(self):
            return self.get_queryset().active()

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="loans")
    borrowed_at = models.DateTimeField(default=timezone.now)
    returned_at = models.DateTimeField(null=True, blank=True)

    objects = LoanManager()

    #TODO: set returned_at or raise AlreadyReturnedError/ValueError
    def mark_returned(self) -> None:
        ...
