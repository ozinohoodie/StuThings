from django.core.management.base import BaseCommand
from lending.models import Book, Member

class Command(BaseCommand):
    help = "Seed demo data"
    def handle(self, *args, **options):
        Book.objects.get_or_create(title="Clean Code", author="Robert C. Martin", defaults={"copies_available": 2})
        Book.objects.get_or_create(title="Design Patterns", author="GoF", defaults={"copies_available": 1})
        Book.objects.get_or_create(title="Practical Django", author="S. Rivera", defaults={"copies_available": 1})
        Member.objects.get_or_create(email="alice@example.com", defaults={"name": "Alice"})
        Member.objects.get_or_create(email="bob@example.com", defaults={"name": "Bob"})
        self.stdout.write(self.style.SUCCESS("Seeded data"))