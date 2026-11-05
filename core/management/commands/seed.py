from django.core.management.base import BaseCommand

from core.districts import seed_districts


class Command(BaseCommand):
    help = "Create / update the districts of Karakalpakstan"

    def handle(self, *args, **opts):
        n = seed_districts()
        self.stdout.write(self.style.SUCCESS(f"{n} districts ready"))
