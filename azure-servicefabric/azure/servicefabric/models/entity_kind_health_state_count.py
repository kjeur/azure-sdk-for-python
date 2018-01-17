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


class EntityKindHealthStateCount(Model):
    """Represents health state count for entities of the specified entity kind.

    :param entity_kind: Possible values include: 'Invalid', 'Node',
     'Partition', 'Service', 'Application', 'Replica', 'DeployedApplication',
     'DeployedServicePackage', 'Cluster'
    :type entity_kind: str or ~azure.servicefabric.models.enum
    :param health_state_count:
    :type health_state_count: ~azure.servicefabric.models.HealthStateCount
    """

    _attribute_map = {
        'entity_kind': {'key': 'EntityKind', 'type': 'str'},
        'health_state_count': {'key': 'HealthStateCount', 'type': 'HealthStateCount'},
    }

    def __init__(self, entity_kind=None, health_state_count=None):
        super(EntityKindHealthStateCount, self).__init__()
        self.entity_kind = entity_kind
        self.health_state_count = health_state_count
