"""Create the Django admin user once, if it does not exist yet.

Username/password come from the ADMIN_USERNAME / ADMIN_PASSWORD environment variables
(default: admin / admin123 for the contest prototype). An existing user is never overwritten,
so a password changed in /admin/ stays changed after redeploys.
"""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create the default superuser if it is missing"

    def handle(self, *args, **opts):
        User = get_user_model()
        username = os.environ.get("ADMIN_USERNAME", "admin")
        password = os.environ.get("ADMIN_PASSWORD", "admin123")
        if User.objects.filter(username=username).exists():
            self.stdout.write(f"admin user '{username}' already exists")
            return
        User.objects.create_superuser(username=username, email="", password=password)
        self.stdout.write(self.style.SUCCESS(f"created admin user '{username}'"))
