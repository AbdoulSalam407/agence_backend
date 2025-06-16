agence_backend/
├── api/                        # Application Django (logique métier)
│   ├── __init__.py
│   ├── admin.py               # (optionnel) pour accéder à l'admin Django
│   ├── apps.py
│   ├── migrations/            # Fichiers de migration de la base de données
│   │   └── __init__.py
│   ├── models.py              # Définition des tables SQL (ORM)
│   ├── serializers.py         # Sérialisation des modèles pour l’API
│   ├── views.py               # Vues API (CRUD via DRF)
│   ├── urls.py                # Routes de l’application `api`
│   └── tests.py               # Tests unitaires (optionnel)
│
├── agence_backend/            # Réglages du projet Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Configuration (base de données, apps, etc.)
│   ├── urls.py                # Routes principales du projet (inclut api.urls)
│   └── wsgi.py
│
├── manage.py                  # Commande pour exécuter le projet Django
├── requirements.txt           # (optionnel) Dépendances à installer
└── README.md                  # Documentation du projet (optionnel)
# agence_backend
