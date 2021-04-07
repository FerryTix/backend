import * as mongoose from 'mongoose';

const logger = require('../logger');
const config = require('../config');

class Database {
  private  _client;

  constructor() {
    this._client = mongoose.connect(config.DB_URL, { useNewUrlParser: true, useUnifiedTopology: true })
    this.testConnection();
  }

  private testConnection() {
    this._client.on('error', console.error.bind(console, 'connection error mongo db'))
    this._client.once('open', function () {
      console.log('Succesfull connected to database')
    })
  }

  get client() {
    return this._client;
  }
}

module.exports = Database;
