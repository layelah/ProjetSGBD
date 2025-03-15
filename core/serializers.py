from rest_framework import serializers
from .models import User, Exercise, Submission

# Serializer pour le modèle User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# Serializer pour le modèle Exercise
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'professor', 'title', 'pdf_file', 'correction_models']

# Serializer pour le modèle Submission
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'student', 'exercise', 'pdf_file', 'grade', 'feedback']