import { MongoClient } from 'mongodb';
import * as assert from 'assert';

const logger = require('../logger');
const config = require('../config');

class Database {
  private readonly _client: MongoClient;

  constructor() {
    this._client = new MongoClient(config.DB_URL);
    this.connectionTest();
  }

  private connectionTest(): void {
    this._client.connect( function (err) {
      assert.equal(null, err);
      logger.info('Connected succesfully to mongodb');
    });
    this._client.close();
  }

  get client(): MongoClient {
    return this._client;
  }
}

module.exports = Database;
