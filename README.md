

---

# **Plateforme intelligente d'évaluation automatisée des exercices de bases de données**

## **Description du projet**

Cette plateforme web permet aux professeurs de déposer des sujets d'exercices en bases de données et aux étudiants de soumettre leurs réponses sous forme de fichiers PDF. La plateforme utilise un moteur d'intelligence artificielle pour corriger automatiquement les exercices.

---

## **Technologies utilisées**

- **Backend** : Django (Python)
    
- **Frontend** : Angular
    
- **Base de données** : PostgreSQL
    
- **Stockage de fichiers** : Système de fichiers local
    
- **API** : Django REST Framework (DRF)
    
- **Gestion de version** : Git / GitHub
    

---

## **Guide d'installation et d'exécution en local**

### **Prérequis**

Avant de commencer, assure-toi d'avoir installé les outils suivants avec les versions exactes indiquées :

1. **Python 3.10+** : [Télécharger Python](https://www.python.org/downloads/)
    
2. **PostgreSQL** : [Télécharger PostgreSQL](https://www.postgresql.org/download/)
    
3. **Git** : [Télécharger Git](https://git-scm.com/downloads)
    
4. **Node.js v18.20.7** : [Télécharger Node.js](https://nodejs.org/)
    
5. **npm v9.9.4** (installé automatiquement avec Node.js)
    
6. **Angular CLI v16.2.16** (installé via npm)
    
7. **PgAdmin** (optionnel, pour gérer PostgreSQL) : [Télécharger PgAdmin](https://www.pgadmin.org/download/)
    

---

### **Étape 1 : Cloner le dépôt GitHub**

1. Ouvre un terminal (ou PowerShell sous Windows).
    
2. Clone le dépôt GitHub avec la commande suivante :

```
git clone https://github.com/layelah/ProjetSGBD.git
```

3. Déplace-toi dans le dossier du projet :

```
cd ProjetSGBD
```


---

### **Étape 2 : Configurer l'environnement virtuel**

1. Crée un environnement virtuel pour isoler les dépendances du projet :

```
cd backend
python -m venv .venv
```

2. Active l'environnement virtuel :
- **Sur Windows** :

```
.venv\Scripts\activate
```

- **Sur macOS/Linux** :

```
source .venv/bin/activate
```

**Note** : Si tout s'est bien passé, tu verras `(.venv)` apparaître avant ton invite de commande.

---

### **Étape 3 : Installer les dépendances Python**

1. Installe les packages nécessaires avec la commande suivante :

```
pip install -r requirements.txt
```

---

### **Étape 4 : Configurer la base de données PostgreSQL**

1. **Installer PostgreSQL** :
    
    - Si tu ne l'as pas déjà fait, installe PostgreSQL depuis [le site officiel](https://www.postgresql.org/download/).
        
    - Pendant l'installation, utilise le mot de passe `postgres` pour etre en accord avec le projet ou sinon si tu as mis un autre mot de passe va sur le dossier sgbd_core/settings.py et modifie le mot de passe du postgres pour mettre le tiens
        
2. **Créer la base de données** :
    
    - Ouvre PgAdmin ou un autre client PostgreSQL.
        
    - Crée une nouvelle base de données appelée `sgbd_platform`.
        

---

### **Étape 5 : Appliquer les migrations**

1. Applique les migrations pour créer les tables dans la base de données :

```
python manage.py migrate
```

---

### **Étape 6 : Créer un superutilisateur**

1. Crée un compte administrateur pour accéder à l'interface d'administration Django :

```
python manage.py createsuperuser
```

1. Suis les instructions pour entrer un nom d'utilisateur, un email et un mot de passe.

---

### **Étape 7 : Lancer le serveur Django**

1. Démarre le serveur de développement Django :

```
python manage.py runserver
```

1. Le serveur sera accessible à l'adresse : [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

### **Étape 8 : Installer et lancer le frontend Angular**

1. **Installer Node.js v18.20.7** :
    
    - Si tu ne l'as pas déjà fait, installe Node.js depuis [le site officiel](https://nodejs.org/).
        
    - Vérifie la version de Node.js avec :

```
node --version
```

Vérifie la version de npm avec :

```
npm --version
```

2. **Installer Angular CLI v16.2.16** :

- Installe Angular CLI globalement avec la commande suivante :

```
npm install -g @angular/cli@16.2.16
```

Vérifie la version d'Angular CLI avec :

```
ng version
```

3. Installer les dépendances Angular** :

- Ouvre un nouveau terminal dans le dossier `frontend` :

```
cd frontend
npm install
```

4. **Lancer le serveur Angular** :

- Démarre le serveur Angular avec la commande suivante :

```
ng serve
```

- Le frontend sera accessible à l'adresse : [http://localhost:4200/](http://localhost:4200/).

---

### **Étape 9 : Utiliser l'application**

1. **Backend (Django)** :
    
    - Accède à l'interface d'administration Django : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
        
    - Utilise les identifiants du superutilisateur que tu as créés pour te connecter.
        
2. **Frontend (Angular)** :
    
    - Accède à l'interface utilisateur : [http://localhost:4200/](http://localhost:4200/).
        
    - Explore les fonctionnalités de la plateforme.

---

### **Étape 10 : Tester l'API**

L'API est accessible via les endpoints suivants :

- **Exercices** :
    
    - Liste des exercices : `GET /api/exercises/`
        
    - Créer un exercice : `POST /api/exercises/`
        
- **Soumissions** :
    
    - Liste des soumissions : `GET /api/submissions/`
        
    - Créer une soumission : `POST /api/submissions/`

---

## **Auteurs**

- Abdoulaye LAH
    

---

### **Problèmes courants**

- Si tu rencontres des erreurs lors de l'installation des dépendances, assure-toi que les versions de Node.js, npm et Angular CLI correspondent exactement à celles indiquées.
    
- Si le serveur Django ne démarre pas, vérifie que la base de données est bien configurée dans le fichier `settings.py`
