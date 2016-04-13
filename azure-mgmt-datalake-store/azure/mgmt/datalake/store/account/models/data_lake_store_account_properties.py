# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataLakeStoreAccountProperties(Model):
    """
    Data Lake Store account properties information

    :param provisioning_state: Gets the status of the Data Lake Store account
     while being provisioned. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming',
     'Deleting', 'Deleted'
    :type provisioning_state: str
    :param state: Gets the status of the Data Lake Store account after
     provisioning has completed. Possible values include: 'active',
     'suspended'
    :type state: str
    :param creation_time: Gets the account creation time.
    :type creation_time: datetime
    :param last_modified_time: Gets the account last modified time.
    :type last_modified_time: datetime
    :param endpoint: Gets or sets the gateway host.
    :type endpoint: str
    :param default_group: Gets or sets the default owner group for all new
     folders and files created in the Data Lake Store account.
    :type default_group: str
    """ 

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'DataLakeStoreAccountStatus'},
        'state': {'key': 'state', 'type': 'DataLakeStoreAccountState'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'default_group': {'key': 'defaultGroup', 'type': 'str'},
    }

    def __init__(self, provisioning_state=None, state=None, creation_time=None, last_modified_time=None, endpoint=None, default_group=None):
        self.provisioning_state = provisioning_state
        self.state = state
        self.creation_time = creation_time
        self.last_modified_time = last_modified_time
        self.endpoint = endpoint
        self.default_group = default_group
