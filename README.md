# 🎟️ TicketFlow — Backend (Django REST)

Ce dépôt contient le backend de l'application TicketFlow, une plateforme de gestion de tickets entre clients, agents et administrateurs.

## 🚀 Stack
- Python 3.12
- Django 5.2.3
- Django REST Framework
- PostgreSQL
- JWT (Simple JWT)

## 📦 Installation locale

### 1. Cloner le repo
```bash
git clone https://github.com/votre-utilisateur/ticketflow-backend.git
cd ticketflow-backend
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Créer le fichier `.env`
```env
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### 5. Appliquer les migrations
```bash
python manage.py migrate
```

### 6. Créer un superutilisateur (admin)
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur local
```bash
python manage.py runserver
```

## 📬 Endpoints principaux
- `/api/token/` → login (obtenir access/refresh)
- `/api/token/refresh/` → refresh token
- `/api/tickets/` → CRUD tickets
- `/api/tickets/<id>/messages/` → messages liés à un ticket
- `/admin/` → interface admin

## ✅ Tests

```bash
pytest core/tests/ --reuse-db -v
```

## 📤 Déploiement Render
- Le backend est hébergé sur Render : https://tickets-app-XXXX.onrender.com
- Les variables d'environnement sont configurées dans le dashboard Render
- `gunicorn` est utilisé comme serveur WSGI

## 📁 Arborescence
```
tickets_project/
├── users/         # Utilisateurs & rôles
├── core/          # Tickets, messages, entreprises
├── tests/         # Tests Pytest
├── .env           # Variables (local only)
├── requirements.txt
└── manage.py
```

## 🔐 Authentification
- Accès protégé via JWT
- Permissions personnalisées selon le rôle de l’utilisateur (client, agent, admin)

## ✨ À venir (V2)
- WebSockets pour notifications
- Dashboard statistiques
- Upload de fichiers
