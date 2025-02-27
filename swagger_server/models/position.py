# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.fare import Fare  # noqa: F401,E501
from swagger_server import util


class Position(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, fare: Fare=None, count: int=None):  # noqa: E501
        """Position - a model defined in Swagger

        :param fare: The fare of this Position.  # noqa: E501
        :type fare: Fare
        :param count: The count of this Position.  # noqa: E501
        :type count: int
        """
        self.swagger_types = {
            'fare': Fare,
            'count': int
        }

        self.attribute_map = {
            'fare': 'fare',
            'count': 'count'
        }
        self._fare = fare
        self._count = count

    @classmethod
    def from_dict(cls, dikt) -> 'Position':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Position of this Position.  # noqa: E501
        :rtype: Position
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fare(self) -> Fare:
        """Gets the fare of this Position.


        :return: The fare of this Position.
        :rtype: Fare
        """
        return self._fare

    @fare.setter
    def fare(self, fare: Fare):
        """Sets the fare of this Position.


        :param fare: The fare of this Position.
        :type fare: Fare
        """

        self._fare = fare

    @property
    def count(self) -> int:
        """Gets the count of this Position.


        :return: The count of this Position.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this Position.


        :param count: The count of this Position.
        :type count: int
        """

        self._count = count
