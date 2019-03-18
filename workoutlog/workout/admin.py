from django.contrib import admin
from .models import Target, Exercise, Workout

# Register your models here.
admin.site.register(Target)
admin.site.register(Exercise)
admin.site.register(Workout)
