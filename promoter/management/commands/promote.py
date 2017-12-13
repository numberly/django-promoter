"""
Allow LDAP user promotion
"""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Promote a user to staff, admin, or superuser.
    """

    help = 'Promote a user to superuser'

    def add_arguments(self, parser):
        """Get username."""
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        """Try to promote user, or fail."""
        username = options.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError('User %s does not exist' % username)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully promoted user %s' % username
        ))


__all__ = ['Command']
