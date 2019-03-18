from django import forms
from .models import Target, Exercise, Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model=Workout
        fields='__all__'