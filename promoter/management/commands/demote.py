"""
Allow LDAP user demotion
"""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Demote a staff, admin, or superuser member to simple user
    """

    help = 'Demote a user to superuser'

    def add_arguments(self, parser):
        """Get username."""
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        """Try to demote user, or fail."""
        username = options.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError('User %s does not exist' % username)
        user.is_superuser = False
        user.is_staff = False
        user.is_admin = False
        user.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully demoted user %s' % username
        ))


__all__ = ['Command']
