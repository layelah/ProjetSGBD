from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core import views

# Créer un routeur et enregistrer les ViewSets
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'submissions', views.SubmissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Tous les endpoints API seront sous /api/
    path('api-auth/', include('rest_framework.urls')),  # Pour l'authentification
]