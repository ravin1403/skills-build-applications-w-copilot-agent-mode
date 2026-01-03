from django.db import models

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=24, blank=True, null=True)
    is_superhero = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    user = models.CharField(max_length=24)
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.user}"

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    team = models.CharField(max_length=24)
    total_points = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Leaderboard for {self.team}"
