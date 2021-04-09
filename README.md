# backend
Backend for the Ferry Tix application.

## Docker-Compose
Zum Ausführen der Docker-Compose muss im Root-Verzeichnis eine `.env`Datei angelegt werden mit den folgenden Einträgen:
* APP_PORT | Der Port, unter dem die API erreichbar ist.
* APP_SSL_CERTIFICATE | Pfad zum SSL Cert
* APP_SSL_KEY | Pfad zum SSL Key
* APP_MODE | Muss für '**PROD**' Modus damit gesetzt werden
* MONGODB_DATABASE | MongoDB Database, die erzeugt wird
* MONGODB_USERNAME | MongoDB Username
* MONGODB_PASSWORD | MongoDB Password
* MONGODB_PORT | Der Port, unter dem die MongoDB erreichbar ist.
* SECRET | Der API Key

