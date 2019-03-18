from django.shortcuts import render, get_object_or_404
from .models import Exercise, Workout
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'workout/index.html')

def exercises(request):
    exercise_list=Exercise.objects.all()
    return render (request, 'workout/exercises.html', {'exercise_list': exercise_list})

def getworkouts(request):
    workout_list=Workout.objects.all()
    return render (request, 'workout/workouts.html', {'workout_list': workout_list})

def workoutdetail(request, id):
    detail=get_object_or_404(Workout, pk=id)
    return render (request, 'workout/logentry.html', {'detail': detail})

#form view
@login_required
def newWorkout(request):
    form=WorkoutForm
    if request.method=='POST':
        form=WorkoutForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=WorkoutForm()
    else:
        form=WorkoutForm()
    return render (request, 'workout/newworkout.html', {'form': form})

def loginmessage(request):
    return render (request, 'workout/loginmessage.html')

def logoutmessage(request):
    return render (request, 'workout/logoutmessage.html')