from django import forms
from lending.models import Book, Member, Loan

class BorrowForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    member = forms.ModelChoiceField(queryset=Member.objects.all())

class ReturnForm(forms.Form):
    loan = forms.ModelChoiceField(queryset=Loan.objects.active())