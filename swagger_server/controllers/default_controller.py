import connexion
import six

from swagger_server.models.faehr_card import FaehrCard  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.machine_command import MachineCommand  # noqa: E501
from swagger_server.models.machine_configuration import MachineConfiguration  # noqa: E501
from swagger_server.models.machine_status import MachineStatus  # noqa: E501
from swagger_server.models.ticket_sale import TicketSale  # noqa: E501
from swagger_server.models.top_up import TopUp  # noqa: E501
from swagger_server.models.vending_machine import VendingMachine  # noqa: E501
from swagger_server import util


def faehr_card_uuid_balance_get(uuid):  # noqa: E501
    """faehr_card_uuid_balance_get

    Return a FaehrCard&#x27;s balance. # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def faehr_card_uuid_get(uuid):  # noqa: E501
    """faehr_card_uuid_get

    Return full details on a single FaehrCard. # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: FaehrCard
    """
    return 'do some magic!'


def faehr_card_uuid_topup_post(body, uuid):  # noqa: E501
    """faehr_card_uuid_topup_post

    Top up a FaehrCard&#x27;s balance. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param uuid: 
    :type uuid: 

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = TopUp.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def machines_default_config_patch(body):  # noqa: E501
    """machines_default_config_patch

    Change the default configuration for all vending machines. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: MachineConfiguration
    """
    if connexion.request.is_json:
        body = MachineConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def machines_get():  # noqa: E501
    """machines_get

    list all active vending machines # noqa: E501


    :rtype: List[VendingMachine]
    """
    return 'do some magic!'


def machines_uuid_commands_get(uuid):  # noqa: E501
    """machines_uuid_commands_get

    Retrieve a command for a vending machine with the given id. May return after an undefined timeout # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: MachineCommand
    """
    return 'do some magic!'


def machines_uuid_commands_post(body, uuid):  # noqa: E501
    """machines_uuid_commands_post

    Execute a command on a single vending machine. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param uuid: 
    :type uuid: 

    :rtype: MachineStatus
    """
    if connexion.request.is_json:
        body = MachineCommand.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def machines_uuid_config_patch(body, uuid):  # noqa: E501
    """machines_uuid_config_patch

    Change the configuration of a vending machine. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param uuid: 
    :type uuid: 

    :rtype: MachineConfiguration
    """
    if connexion.request.is_json:
        body = MachineConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def machines_uuid_get(uuid):  # noqa: E501
    """machines_uuid_get

    returns a single vending machine # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: VendingMachine
    """
    return 'do some magic!'


def machines_uuid_status_get(uuid):  # noqa: E501
    """machines_uuid_status_get

    Returns a single vending machine&#x27;s status. # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: MachineStatus
    """
    return 'do some magic!'


def machines_uuid_status_patch(body, uuid):  # noqa: E501
    """machines_uuid_status_patch

    Update machine status manually. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param uuid: 
    :type uuid: 

    :rtype: MachineStatus
    """
    if connexion.request.is_json:
        body = MachineStatus.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ticket_sales_post(body):  # noqa: E501
    """ticket_sales_post

    Add a ticket sale. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TicketSale.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ticket_sales_uuid_invalidate_return_delete(uuid):  # noqa: E501
    """ticket_sales_uuid_invalidate_return_delete

    Invalidate a return ticket. # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: None
    """
    return 'do some magic!'
