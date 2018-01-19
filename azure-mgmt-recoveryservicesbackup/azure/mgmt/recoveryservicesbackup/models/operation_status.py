# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OperationStatus(Model):
    """Operation status.

    :param id: ID of the operation.
    :type id: str
    :param name: Name of the operation.
    :type name: str
    :param status: Operation status. Possible values include: 'Invalid',
     'InProgress', 'Succeeded', 'Failed', 'Canceled'
    :type status: str or
     ~azure.mgmt.recoveryservicesbackup.models.OperationStatusValues
    :param start_time: Operation start time. Format: ISO-8601.
    :type start_time: datetime
    :param end_time: Operation end time. Format: ISO-8601.
    :type end_time: datetime
    :param error: Error information related to this operation.
    :type error:
     ~azure.mgmt.recoveryservicesbackup.models.OperationStatusError
    :param properties: Additional information associated with this operation.
    :type properties:
     ~azure.mgmt.recoveryservicesbackup.models.OperationStatusExtendedInfo
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'OperationStatusError'},
        'properties': {'key': 'properties', 'type': 'OperationStatusExtendedInfo'},
    }

    def __init__(self, id=None, name=None, status=None, start_time=None, end_time=None, error=None, properties=None):
        super(OperationStatus, self).__init__()
        self.id = id
        self.name = name
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.error = error
        self.properties = properties
