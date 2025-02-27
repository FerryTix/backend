# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, balance: int=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param balance: The balance of this InlineResponse200.  # noqa: E501
        :type balance: int
        """
        self.swagger_types = {
            'balance': int
        }

        self.attribute_map = {
            'balance': 'balance'
        }
        self._balance = balance

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def balance(self) -> int:
        """Gets the balance of this InlineResponse200.


        :return: The balance of this InlineResponse200.
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance: int):
        """Sets the balance of this InlineResponse200.


        :param balance: The balance of this InlineResponse200.
        :type balance: int
        """

        self._balance = balance
