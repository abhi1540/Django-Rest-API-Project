import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to pause execution until we db connection is available"""

    def handle(self, *ars, **other_options):
        self.stdout.write("waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write("waiting 1 sec for database to be available")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
