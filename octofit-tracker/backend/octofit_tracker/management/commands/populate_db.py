from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data in correct order to avoid FK issues
        Activity.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()
        Leaderboard.objects.filter(pk__isnull=False).delete()
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()

        # Create teams with string IDs
        marvel = Team.objects.create(id='marvel', name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(id='dc', name='DC', description='DC Superheroes')

        # Create users with string IDs and team references
        ironman = User.objects.create(id='ironman', name='Iron Man', email='ironman@marvel.com', team='marvel', is_superhero=True)
        cap = User.objects.create(id='cap', name='Captain America', email='cap@marvel.com', team='marvel', is_superhero=True)
        spiderman = User.objects.create(id='spiderman', name='Spider-Man', email='spiderman@marvel.com', team='marvel', is_superhero=True)
        superman = User.objects.create(id='superman', name='Superman', email='superman@dc.com', team='dc', is_superhero=True)
        batman = User.objects.create(id='batman', name='Batman', email='batman@dc.com', team='dc', is_superhero=True)
        wonderwoman = User.objects.create(id='wonderwoman', name='Wonder Woman', email='wonderwoman@dc.com', team='dc', is_superhero=True)

        # Create activities with user string IDs
        Activity.objects.create(id='act1', user='ironman', type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(id='act2', user='cap', type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(id='act3', user='superman', type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(id='act4', user='batman', type='Yoga', duration=20, date=timezone.now().date())

        # Create workouts with suggested_for as list of user IDs
        workout1 = Workout.objects.create(id='workout1', name='Cardio Blast', description='High intensity cardio', suggested_for=['ironman', 'cap', 'superman'])
        workout2 = Workout.objects.create(id='workout2', name='Strength Training', description='Build muscle', suggested_for=['batman'])

        # Create leaderboards with team string IDs
        Leaderboard.objects.create(id='lb_marvel', team='marvel', total_points=120)
        Leaderboard.objects.create(id='lb_dc', team='dc', total_points=110)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
