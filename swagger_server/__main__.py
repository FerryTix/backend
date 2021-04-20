#!/usr/bin/env python3

import os
import connexion

from swagger_server import encoder
from swagger_server import database as db

APP_PORT = os.getenv('APP_PORT')
APP_SSL_CERTIFICATE = os.getenv('APP_SSL_CERTIFICATE')
APP_SSL_KEY = os.getenv('APP_SSL_KEY')
APP_MODE = os.getenv('APP_MODE')


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'FerryTix'}, pythonic_params=True)
    if APP_MODE == 'PROD':
        app.run(
            port=int(APP_PORT),
            ssl_context=(APP_SSL_CERTIFICATE, APP_SSL_KEY)
        )
    else:
        app.run(port=8090)


if __name__ == '__main__':
    main()
