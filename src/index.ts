const config = require('./config');
const logger = require('./logger');
const ExpressServer = require('./expressServer');
const db = require('./utils/database')

const mongoose = require('mongoose');
mongoose.connect(config.DB_URL, { useNewUrlParser: true, useUnifiedTopology: true })

const launchServer = async () => {
    try {
        this.expressServer = new ExpressServer(config.URL_PORT, config.OPENAPI_YAML);
        this.expressServer.launch();
        logger.info('Express server running');
    } catch (error) {
        logger.error('Express Server failure', error.message);
        await this.close();
    }
};

launchServer().catch(e => logger.error(e));

