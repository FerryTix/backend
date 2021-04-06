/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Return a FaehrCard's balance.
*
* uuid UUID 
* returns inline_response_200
* */
const faehrCardUuidBalanceGET = ({ uuid }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Return full details on a single FaehrCard.
*
* uuid UUID 
* returns FaehrCard
* */
const faehrCardUuidGET = ({ uuid }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Top up a FaehrCard's balance.
*
* uuid UUID 
* topUp TopUp 
* returns inline_response_201
* */
const faehrCardUuidTopupPOST = ({ uuid, topUp }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
        topUp,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Change the default configuration for all vending machines.
*
* machineConfiguration MachineConfiguration 
* returns MachineConfiguration
* */
const machinesDefaultConfigPATCH = ({ machineConfiguration }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        machineConfiguration,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* list all active vending machines
*
* returns List
* */
const machinesGET = () => new Promise(
  async (resolve, reject) => {
    try {
        console.log('test')
      resolve(Service.successResponse({
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Retrieve a command for a vending machine with the given id. May return after an undefined timeout
*
* uuid UUID 
* returns MachineCommand
* */
const machinesUuidCommandsGET = ({ uuid }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Execute a command on a single vending machine.
*
* uuid UUID 
* body String 
* returns MachineStatus
* */
const machinesUuidCommandsPOST = ({ uuid, body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Change the configuration of a vending machine.
*
* uuid UUID 
* machineConfiguration MachineConfiguration 
* returns MachineConfiguration
* */
const machinesUuidConfigPATCH = ({ uuid, machineConfiguration }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
        machineConfiguration,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* returns a single vending machine
*
* uuid UUID 
* returns VendingMachine
* */
const machinesUuidGET = ({ uuid }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Replace receipt paper roll.
*
* uuid UUID 
* body Integer 
* returns MachineStatus
* */
const machinesUuidReplacePaperRollPOST = ({ uuid, body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Returns a single vending machine's status.
*
* uuid UUID 
* returns MachineStatus
* */
const machinesUuidStatusGET = ({ uuid }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Update machine status manually.
*
* uuid UUID 
* machineStatus MachineStatus 
* returns MachineStatus
* */
const machinesUuidStatusPATCH = ({ uuid, machineStatus }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
        machineStatus,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Add a ticket sale.
*
* ticketSale TicketSale 
* no response value expected for this operation
* */
const ticketSalesPOST = ({ ticketSale }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        ticketSale,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Invalidate a return ticket.
*
* uuid UUID 
* no response value expected for this operation
* */
const ticketSalesUuidInvalidateReturnDELETE = ({ uuid }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        uuid,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

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
