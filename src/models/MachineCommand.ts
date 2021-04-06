/**
 * FerryTix
 * This is the api for the FerryTix Passenger Ferry Ticketing System, that is both accessible to the vending machines and to other clients.
 *
 * OpenAPI spec version: 1.0.0
 * Contact: hendrik.lankers.hl@googlemail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * An order issued by an admin for a machine to perform an action
 */
export type MachineCommand = 'setSignalRed' | 'setSignalGreen' | 'stopVending' | 'startVending';
