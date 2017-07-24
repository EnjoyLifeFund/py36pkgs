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

from .sub_resource import SubResource


class ApplicationGatewayBackendAddressPool(SubResource):
    """Backend Address Pool of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param backend_ip_configurations: Collection of references to IPs defined
     in network interfaces.
    :type backend_ip_configurations: list of
     :class:`NetworkInterfaceIPConfiguration
     <azure.mgmt.network.v2016_12_01.models.NetworkInterfaceIPConfiguration>`
    :param backend_addresses: Backend addresses
    :type backend_addresses: list of :class:`ApplicationGatewayBackendAddress
     <azure.mgmt.network.v2016_12_01.models.ApplicationGatewayBackendAddress>`
    :param provisioning_state: Provisioning state of the backend address pool
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Resource that is unique within a resource group. This name
     can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'backend_ip_configurations': {'key': 'properties.backendIPConfigurations', 'type': '[NetworkInterfaceIPConfiguration]'},
        'backend_addresses': {'key': 'properties.backendAddresses', 'type': '[ApplicationGatewayBackendAddress]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, backend_ip_configurations=None, backend_addresses=None, provisioning_state=None, name=None, etag=None):
        super(ApplicationGatewayBackendAddressPool, self).__init__(id=id)
        self.backend_ip_configurations = backend_ip_configurations
        self.backend_addresses = backend_addresses
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
