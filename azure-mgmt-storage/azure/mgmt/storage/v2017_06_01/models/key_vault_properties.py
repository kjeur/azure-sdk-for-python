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


class KeyVaultProperties(Model):
    """Properties of key vault.

    :param key_name: The name of KeyVault key.
    :type key_name: str
    :param key_version: The version of KeyVault key.
    :type key_version: str
    :param key_vault_uri: The Uri of KeyVault.
    :type key_vault_uri: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyname', 'type': 'str'},
        'key_version': {'key': 'keyversion', 'type': 'str'},
        'key_vault_uri': {'key': 'keyvaulturi', 'type': 'str'},
    }

    def __init__(self, key_name=None, key_version=None, key_vault_uri=None):
        super(KeyVaultProperties, self).__init__()
        self.key_name = key_name
        self.key_version = key_version
        self.key_vault_uri = key_vault_uri
