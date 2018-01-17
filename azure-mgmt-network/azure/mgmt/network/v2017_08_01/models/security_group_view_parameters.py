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


class SecurityGroupViewParameters(Model):
    """Parameters that define the VM to check security groups for.

    :param target_resource_id: ID of the target VM.
    :type target_resource_id: str
    """

    _validation = {
        'target_resource_id': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
    }

    def __init__(self, target_resource_id):
        super(SecurityGroupViewParameters, self).__init__()
        self.target_resource_id = target_resource_id
