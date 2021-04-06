/**
 * The DefaultController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic reoutes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/DefaultService');
const faehrCardUuidBalanceGET = async (request, response) => {
  await Controller.handleRequest(request, response, service.faehrCardUuidBalanceGET);
};

const faehrCardUuidGET = async (request, response) => {
  await Controller.handleRequest(request, response, service.faehrCardUuidGET);
};

const faehrCardUuidTopupPOST = async (request, response) => {
  await Controller.handleRequest(request, response, service.faehrCardUuidTopupPOST);
};

const machinesDefaultConfigPATCH = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesDefaultConfigPATCH);
};

const machinesGET = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesGET);
};

const machinesUuidCommandsGET = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidCommandsGET);
};

const machinesUuidCommandsPOST = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidCommandsPOST);
};

const machinesUuidConfigPATCH = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidConfigPATCH);
};

const machinesUuidGET = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidGET);
};

const machinesUuidReplacePaperRollPOST = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidReplacePaperRollPOST);
};

const machinesUuidStatusGET = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidStatusGET);
};

const machinesUuidStatusPATCH = async (request, response) => {
  await Controller.handleRequest(request, response, service.machinesUuidStatusPATCH);
};

const ticketSalesPOST = async (request, response) => {
  await Controller.handleRequest(request, response, service.ticketSalesPOST);
};

const ticketSalesUuidInvalidateReturnDELETE = async (request, response) => {
  await Controller.handleRequest(request, response, service.ticketSalesUuidInvalidateReturnDELETE);
};


module.exports = {
  faehrCardUuidBalanceGET,
  faehrCardUuidGET,
  faehrCardUuidTopupPOST,
  machinesDefaultConfigPATCH,
  machinesGET,
  machinesUuidCommandsGET,
  machinesUuidCommandsPOST,
  machinesUuidConfigPATCH,
  machinesUuidGET,
  machinesUuidReplacePaperRollPOST,
  machinesUuidStatusGET,
  machinesUuidStatusPATCH,
  ticketSalesPOST,
  ticketSalesUuidInvalidateReturnDELETE,
};
