from django.core.management.base import BaseCommand

from apps.profiles.models import Interest, SpeakingGoal


INTERESTS = [
    "Programming",
    "Technology",
    "Artificial Intelligence",
    "Business",
    "Startup",
    "Movies",
    "Books",
    "Football",
    "Cricket",
    "Travel",
    "Cooking",
    "Music",
]


GOALS = [
    "Daily Conversation",
    "Fluency",
    "IELTS",
    "TOEFL",
    "Job Interview",
    "Business English",
    "Presentation",
    "Public Speaking",
]


class Command(BaseCommand):
    help = "Seed profile lookup data."

    def handle(self, *args, **options):

        for interest in INTERESTS:
            Interest.objects.get_or_create(
                name=interest,
            )

        for goal in GOALS:
            SpeakingGoal.objects.get_or_create(
                name=goal,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Profile lookup data seeded successfully."
            )
        )