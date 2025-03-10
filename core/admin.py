from django.contrib import admin
from .models import User, Exercise, Submission

# Enregistrer les modèles dans l'admin
admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Submission)