# api-crud

## Description du projet

Ce projet est une API CRUD avec authentification OAuth2, permettant de gérer des produits. Les opérations disponibles incluent :
- Lister les produits
- Consulter un produit spécifique
- Ajouter un produit
- Modifier un produit
- Supprimer un produit

L'API utilise FastAPI pour la gestion des routes et SQLModel pour l'interaction avec la base de données.

## Installation et utilisation

### Prérequis

Assurez-vous d'avoir Python 3.8+ installé sur votre machine.

### Installation

1. Clonez le dépôt :
    ```sh
    git clone <git@github.com:Jakimpact/api-crud.git>
    cd <api-crud>
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

Créez un fichier `.env` à la racine du projet et définissez les variables suivantes :

USER="your_username"
PASSWORD="your_password"
SERVER_NAME="your_sql_server"
BDD_NAME="your_bbd_name"
PORT=1433
SECRET_KEY="your_secret_key"
ALGORITHM="your_algorithm"

### Lancer le projet

Pour démarrer le serveur FastAPI, exécutez la commande suivante :
```sh
fastapi endpoints.py
```

## Routes de l'API

- **GET /** : Retourne un message de bienvenue.
- **POST /token** : Authentifie un utilisateur et retourne un token d'accès.
- **GET /products** : Liste tous les produits *(nécessite une authentification)*.
- **GET /products/{product_id}** : Retourne les détails d'un produit spécifique *(nécessite une authentification)*.
- **POST /products** : Ajoute un nouveau produit *(nécessite une authentification)*.
- **PUT /products/{product_id}** : Modifie un produit existant *(nécessite une authentification)*.
- **DELETE /products/{product_id}** : Supprime un produit *(nécessite une authentification)*.

---

## Utilisation de SQLModel

Le projet utilise **SQLModel** pour interagir avec la base de données.  
Les modèles sont définis dans le fichier `models.py`.  
La connexion à la base de données est gérée dans le fichier `connect_db.py`.

---

## Authentification

L'authentification est gérée via **OAuth2 avec mot de passe**.  
Les fonctions d'authentification sont définies dans le fichier `generate_auth.py`.  
Les utilisateurs sont stockés dans une base de données fictive `users_db`.

Pour obtenir un token d'accès, envoyez une requête **POST** à `/token` avec les informations d'identification de l'utilisateur.  
Utilisez ce token pour accéder aux routes protégées de l'API.