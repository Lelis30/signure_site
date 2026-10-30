# SIGNURE — Django website

Proposition de site vitrine moderne pour SIGNURE.

## Démarrage

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/

Le formulaire de contact enregistre les demandes dans la base Django, consultables via /admin après création d'un superutilisateur (`python manage.py createsuperuser`). Configurez un SMTP et les paramètres de sécurité avant déploiement public.
