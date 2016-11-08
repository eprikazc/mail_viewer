# Gmail Viewer

This demo app shows django integration with google OAuth2 and GMail APIs.
Developed with Ubuntu 16.04, Docker 1.12.3, Docker-Compose 1.9.0-rc1

## Installation
1. Install [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/):
2. Build and run

        sudo docker-compose build
        sudo docker-compose run web python manage.py migrate
        sudo docker-compose up
3. Edit /etc/hosts to resolve test1.com to localhost
4. Go to http://test1.com:8000/ in browser

## Configuring your own Google App
The app is preconfigured with Google API app. If you wish, you may configure your own google APIs app:

1. Create new project at https://console.developers.google.com/apis/dashboard. Next steps are done in the project.
2. Enable Google+ API and GMail API
3. Go to "Credentials" => "OAuth consent screen" and set email address and product name
4. Create credentials. Choose "OAuth Client ID" => "Web application" in the wizard. Add "http://test1.com:8000/complete/google-oauth2/ to authorized redirect URIs
5. View "Client ID" and "Client secret" - you will need to add them to our app configuration

Configure app to use your Google APIs App:
```
sudo su  # if you run docker as root user
export KEY="your google APIs app client ID"
export SECRET="your google APIs app client secret"
docker-compose up
```
