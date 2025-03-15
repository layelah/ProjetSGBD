from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('PROF', 'Professeur'),
        ('STUDENT', 'Étudiant'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')

    # Ajoute ces lignes pour résoudre le conflit
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="core_user_groups",  # Nom unique pour éviter le conflit
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="core_user_permissions",  # Nom unique pour éviter le conflit
        related_query_name="user",
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

# Modèle Exercise
class Exercise(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='exercises/')
    correction_models = models.JSONField(default=list)  # Pour stocker les modèles de correction

    def __str__(self):
        return self.title

# Modèle Submission
class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='submissions')
    pdf_file = models.FileField(upload_to='submissions/')
    grade = models.FloatField(null=True, blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.exercise.title}"