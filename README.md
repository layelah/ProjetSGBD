# Projet : Plateforme intelligente d'évaluation automatisée des exercices de bases de données

Ce projet consiste à développer une plateforme web permettant aux professeurs de déposer des sujets d'exercices en bases de données et aux étudiants de soumettre leurs réponses sous forme de fichiers PDF. La plateforme intègre un moteur d'intelligence artificielle pour la correction automatique des exercices.

## Technologies utilisées

- **Backend** : Django (Python)
- **Frontend** : Angular (à développer)
- **Base de données** : PostgreSQL
- **Stockage de fichiers** : Système de fichiers local (pour le moment)
- **API** : Django REST Framework (DRF)
- **Gestion de version** : Git / GitHub

---

## Prérequis

Avant de commencer, assure-toi d'avoir installé les outils suivants :

1. **Python 3.10+** : [Télécharger Python](https://www.python.org/downloads/)
2. **PostgreSQL** : [Télécharger PostgreSQL](https://www.postgresql.org/download/)
3. **Git** : [Télécharger Git](https://git-scm.com/downloads)
4. **Node.js** (pour Angular) : [Télécharger Node.js](https://nodejs.org/)
5. **PyCharm** (optionnel) : [Télécharger PyCharm](https://www.jetbrains.com/pycharm/download/)

---

## Installation et configuration

### 1. Cloner le dépôt

Ouvre un terminal et clone le dépôt GitHub :

```bash
git clone https://github.com/layelah/ProjetSGBD.git
cd ProjetSGBD
```

### 2. Configurer l'environnement virtuel

Crée un environnement virtuel et active-le :

```
python -m venv .venv
.venv\Scripts\activate  # Sur Windows
source .venv/bin/activate  # Sur macOS/Linux
```

### 3. Installer les dépendances Python

Installe les packages nécessaires :

```
pip install -r requirements.txt
```

### 4. Configurer la base de données

1. **Créer une base de données PostgreSQL** :
    
    - Ouvre pgAdmin ou un autre client PostgreSQL.
        
    - Crée une base de données appelée `sgbd_platform` avec comme mot de passe `postgres`

### 5. Appliquer les migrations

Applique les migrations pour créer les tables dans la base de données :

```
python manage.py migrate
```

### 6. Créer un superutilisateur

Crée un compte administrateur pour accéder à l'interface d'administration Django :

```
python manage.py createsuperuser
```

Suis les instructions pour entrer un nom d'utilisateur, un email et un mot de passe.

### 7. Lancer le serveur de développement

Démarre le serveur Django :

```
python manage.py runserver
```

Le serveur sera accessible à l'adresse : [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Utilisation de l'API

L'API est accessible via les endpoints suivants :

### 1. **Utilisateurs**

- **Liste des utilisateurs** : `GET /api/users/`
    
- **Créer un utilisateur** : `POST /api/users/`
    
- **Détails d'un utilisateur** : `GET /api/users/{id}/`
    

### 2. **Exercices**

- **Liste des exercices** : `GET /api/exercises/`
    
- **Créer un exercice** : `POST /api/exercises/`
    
- **Détails d'un exercice** : `GET /api/exercises/{id}/`
    

### 3. **Soumissions**

- **Liste des soumissions** : `GET /api/submissions/`
    
- **Créer une soumission** : `POST /api/submissions/`
    
- **Détails d'une soumission** : `GET /api/submissions/{id}/`
    

---

## Frontend (Angular)

### 1. Installer les dépendances Node.js

Ouvre un terminal dans le dossier `frontend` (à créer) et installe les dépendances :

```
cd frontend
npm install
```

### 2. Lancer le serveur de développement Angular

Démarre le serveur Angular :

```
ng serve
```

Le frontend sera accessible à l'adresse : [http://localhost:4200/](http://localhost:4200/).

---

## Contribution

1. **Créer une nouvelle branche** :

```
git checkout -b nom_de_la_branche
```

2. **Faire des modifications** et les commit :

```
git add .
git commit -m "Description des modifications"
```

3. **Pousser la branche sur GitHub** :

```
git push origin nom_de_la_branche
```

4. **Ouvrir une Pull Request (PR)** sur GitHub pour fusionner les modifications.

---

## Auteurs

- [Abdoulaye LAH](https://github.com/layelah)

