# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.faehr_card import FaehrCard  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.machine_command import MachineCommand  # noqa: E501
from swagger_server.models.machine_configuration import MachineConfiguration  # noqa: E501
from swagger_server.models.machine_status import MachineStatus  # noqa: E501
from swagger_server.models.top_up import TopUp  # noqa: E501
from swagger_server.models.vending_machine import VendingMachine  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_faehr_card_uuid_balance_get(self):
        """Test case for faehr_card_uuid_balance_get

        
        """
        response = self.client.open(
            '/faehrCard/{uuid}/balance'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_faehr_card_uuid_get(self):
        """Test case for faehr_card_uuid_get

        
        """
        response = self.client.open(
            '/faehrCard/{uuid}'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_faehr_card_uuid_topup_post(self):
        """Test case for faehr_card_uuid_topup_post

        
        """
        body = TopUp()
        response = self.client.open(
            '/faehrCard/{uuid}/topup'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_default_config_patch(self):
        """Test case for machines_default_config_patch

        
        """
        body = MachineConfiguration()
        response = self.client.open(
            '/machines/defaultConfig',
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_get(self):
        """Test case for machines_get

        
        """
        response = self.client.open(
            '/machines',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_uuid_commands_get(self):
        """Test case for machines_uuid_commands_get

        
        """
        response = self.client.open(
            '/machines/{uuid}/commands'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_uuid_commands_post(self):
        """Test case for machines_uuid_commands_post

        
        """
        body = MachineCommand()
        response = self.client.open(
            '/machines/{uuid}/commands'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_uuid_config_patch(self):
        """Test case for machines_uuid_config_patch

        
        """
        body = MachineConfiguration()
        response = self.client.open(
            '/machines/{uuid}/config'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_uuid_get(self):
        """Test case for machines_uuid_get

        
        """
        response = self.client.open(
            '/machines/{uuid}'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_uuid_status_get(self):
        """Test case for machines_uuid_status_get

        
        """
        response = self.client.open(
            '/machines/{uuid}/status'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_machines_uuid_status_patch(self):
        """Test case for machines_uuid_status_patch

        
        """
        body = MachineStatus()
        response = self.client.open(
            '/machines/{uuid}/status'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ticket_sales_uuid_invalidate_return_delete(self):
        """Test case for ticket_sales_uuid_invalidate_return_delete

        
        """
        response = self.client.open(
            '/ticketSales/{uuid}/invalidateReturn'.format(uuid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
