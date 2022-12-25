## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Se connecter avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Configuration requise

Compte utilisateur à créer pour chaque outil suivant :

- GitHub
- CircleCI
- Docker Hub
- Heroku
- Sentry

#### Installer Docker Desktop ou Docker Engine for Linux :

- `https://docs.docker.com/engine/install`

### Docker

Création du dépôt dans Docker

- ...

### Heroku

Création de l'application depuis le site

- Se connecter à / se créer un compte sur Heroku
- Aller dans `Create` > `A new app` puis configurer l'application et la pipeline associée
- Cliquer sur `Open app`

### Mise en place du pipeline Circle CI

Liaison du projet à CircleCI

- Se connecter à / se créer un compte sur CircleCI
- Relier votre compte CircleCI à votre compte GitHub
- Aller dans `Projects` > Choisissez votre projet GitHub > `Set Up Project` puis choisir l'option préférée "Fastest: Use the .circleci/config.yml in my repo", "Faster: Commit a starter CI pipeline to a new branch" ou "Fast: Take me to a config.yml template that I can edit"
- Retournez ensuite sur `Dashboard`

#### Ajout de variables d'environnement

Cliquez sur `Project Settings` > `Environment Variables` > `Add Environment Variables`

| Nom                | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| IMAGE_NAME         | Le nom de l’image Dockerhub                                                                       |
| HEROKU_APP_NAME    | Nom de votre appli dans Heroku                                                                    |
| HEROKU_TOKEN       | Token d'identification Heroku `heroku auth:token`                                                 |
| DOCKERHUB_USERNAME | Votre identifiant Dockerhub                                                                       |
| DOCKERHUB_PASS     | Votre mot de passe ou token Dockerhub https://hub.docker.com/settings/security > New access token |

Déploiement Effectué à chaque mise à jour du projet GitHub depuis un IDE ou le Terminal (`git add <file> git commit -m "<comment>" git push -u origin`).

Retourner sur son compte CircleCI pour voir les "jobs" du pipeline s'activer :

- `build_and_test` monte et effectue les tests du bon fonctionnement de l'appli, via Pytest
- `docker-build-and-push` envoie l'image du projet sur docker hub (uniquement branche main)
- `deploy_heroku` envoie le projet sur heroku et le déploie (uniquement branche main)

### Récupération du projet en local

- Ouvrir Docker Desktop
- Commande pour simultanément récupérer l'image en localement, lancer le conteneur Docker avec le fichier des variables d'environnement locales et enfin nettoyer/supprimer le conteneur : `docker run -it -p 8000:8000 --rm <docker_username>/oc-lettings-456:latest`
- Testez le site dans votre navigateur : `http://127.0.0.1:8000/`
