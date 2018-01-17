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


class ApplicationGatewayFirewallRule(Model):
    """A web application firewall rule.

    :param rule_id: The identifier of the web application firewall rule.
    :type rule_id: int
    :param description: The description of the web application firewall rule.
    :type description: str
    """

    _validation = {
        'rule_id': {'required': True},
    }

    _attribute_map = {
        'rule_id': {'key': 'ruleId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, rule_id, description=None):
        super(ApplicationGatewayFirewallRule, self).__init__()
        self.rule_id = rule_id
        self.description = description
