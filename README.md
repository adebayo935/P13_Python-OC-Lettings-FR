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
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Admin1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Développement Pipeline CI/CD

### Prérequis
- Un compte CircleCI
- Un compte Docker Hub
- un compte Heroku
- un compte Sentry

### macOS / Linux

#### Préparation
- si vous souhaitez modifier les fichiers "statics" localement, 
  - veuillez executer la commande suivante :
    `python manage.py collectstatic --noinput --clear`
  - et push sur le repo github les modifications avant le deploiement

#### Installation de Docker
- Installer docker sur votre machine local, si besoin
- creer un compte sur Docker Hub
- creer une clé API pour le workflow de CircleCI
- le fichier de préparation de la conteneurisation exist déjà (Dockerfile)

#### Installation de Heroku
- Installer Heroku sur votre machine local, si besoin
- creer un compte sur Heroku
- lier le au compte GitHub
- creer une clé API pour le workflow de CircleCI
- creer une application 'oc-lettings-p13'(HEROKU_APP_NAME)

#### Installation de Sentry
- creer un compte sur Sentry
- creer un projet Django
- Récupérer le DSN, il sera a rajouter à la variable d'environnement DSN_SENTRY

#### Création du pipeline CircleCI
- creer un compte CircleCI
- lier le au compte GitHub
- Creer un pipeline(projet) avec le bon repo
- Editer le fichier de configuration (.circleci/config.yml), 
si vous souhaitez faire des modifications au pipeline existant
- Dans les "settings" du projet, editer vos variables d'environnement
  - Name	Value	
    DEBUG	production	
    DOCKER_LOGIN	*votre nom de compte docker*	
    DOCKER_PASSWORD	*votre clé API Docker*	
    IMAGE_NAME *nom de l'image Docker*
    DSN_SENTRY	*le dsn donné par Sentry*	
    HEROKU_API_KEY	*votre clé API Heroku*		
    HEROKU_APP_NAME	*nom de l'application sur Heroku*
    SECRET_KEY	*clé secret de votre application Django*

#### Execution du pipeline CircleCI
- Chaque fois qu'un push est fait sur le repo GitHub, 
le pipeline va executer le 1er job du pipeline:
  - execution de l'app en environnement virtuel
  - execution des test `pytest` et `flake8`
  
- Si le job est réussi et qu'il s'agit de la branche Master
le pipeline va executer le job de conteneurisation sur Docker
  - création de deux images avec les tags: lastest et le “hash”  de commit CircleCI
  - push sur le repo de Docker Hub
  
- Si le job est réussi et qu'il s'agit de la branche Master
le pipeline va executer le déploiement sur Heroku
  - création des variables d'environnement
  - déploiement du conteneur docker (push & release)
  - le site sera ensuite disponible à l'adresse:
    `https://HEROKU_APP_NAME.herokuapp.com/`


##Surveillance de l’application et suivi des erreurs via Sentry
- le resultat de la surveillance se trouve  actuellement à l'adresse:
  `https://sentry.io/share/issue/05c1c9fe95734a9288ec7d294b918635/`
- l'URL déclenchant le test de surveillance est:
  `https://HEROKU_APP_NAME.herokuapp.com/sentry-debug`


## Déploiement local depuis Docker Hub
- définir les variables d'environnement: DSN_SENTRY, DEBUG= production, SECRET_KEY
- exécuter la commande:
  `docker run --pull always -d -p 8000:8000 DOCKER_LOGIN/IMAGE_NAME:latest`
- Aller sur `http://127.0.0.1:8000/` dans un navigateur.
- pour pouvoir arreter votre container docker
  - lister vos container actifs
    `docker ps`
  - recuperer le CONTAINER_ID  de celui qui a pour nom 
    `DOCKER_LOGIN/IMAGE_NAME:latest`
  - arreter le conteneur
    `docker stop CONTAINER_ID`
