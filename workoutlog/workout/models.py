from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Target(models.Model):
    targetname = models.CharField(max_length=255)

    def __str__(self):
        return self.targetname

    class Meta:
        db_table = 'target'

class Exercise(models.Model):
    exercisename = models.CharField(max_length=255)
    exercisedescription = models.TextField(null=True, blank=True)
    target = models.ForeignKey(Target, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.exercisename

    class Meta:
        db_table = 'exercise'

class Workout(models.Model):
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    workoutname = models.CharField(max_length=255, null=True, blank=True)
    workoutdate = models.DateField()
    workouttime = models.TimeField()
    workoutlocation = models.CharField(max_length=255, null=True, blank=True)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.workoutname

    class Meta:
        db_table = 'workout'