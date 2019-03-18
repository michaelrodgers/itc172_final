from django.test import TestCase
from .models import Target, Exercise, Workout
from .forms import WorkoutForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.

# model tests
class TargetTest(TestCase):
    def test_stringOutput(self):
        target=Target(targetname='Cardio')
        self.assertEqual(str(target), target.targetname)

    def test_tablename(self):
        self.assertEqual(str(Target._meta.db_table), 'target')

class ExerciseTest(TestCase):
    def test_stringOutput(self):
        exercise=Exercise(exercisename='Cycling')
        self.assertEqual(str(exercise), exercise.exercisename)

    def test_tablename(self):
        self.assertEqual(str(Exercise._meta.db_table), 'exercise')

class ReviewTest(TestCase):
    def test_stringOutput(self):
        workout=Workout(workoutname='Night Jog')
        self.assertEqual(str(workout), workout.workoutname)

    def test_tablename(self):
        self.assertEqual(str(Workout._meta.db_table), 'workout')


class TestIndex(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout/index.html')

class TestExercises(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/workout/exercises')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('exercises'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('exercises'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout/exercises.html')

class New_Workout_Form_Test(TestCase):

    # Valid Form Data
    def test_productForm_is_valid(self):
        form = WorkoutForm(data={'userid': "michael", 'workoutname': "Night Ride", 'workoutdate': "2018-12-17", 'workouttime': "06:34:30", 'workoutlocation':"Cal Anderson Park", 'exercises':"Cycling" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = WorkoutForm(data={'userid': "michael", 'workoutname': "Night Ride", 'workoutdate': "2018-12-17", 'workouttime': "06:34:30", 'workoutlocation':"Cal Anderson Park", 'exercises':"Cycling" })
        self.assertFalse(form.is_valid())

