from rest_framework import viewsets
from .models import User, Exercise, Submission
from .serializers import UserSerializer, ExerciseSerializer, SubmissionSerializer

# ViewSet pour le modèle User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet pour le modèle Exercise
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# ViewSet pour le modèle Submission
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer