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


class ApplicationUpgradeUpdateDescription(Model):
    """Describes the parameters for updating an ongoing application upgrade.

    :param name:
    :type name: str
    :param upgrade_kind: Possible values include: 'Invalid', 'Rolling'.
     Default value: "Rolling" .
    :type upgrade_kind: str
    :param application_health_policy:
    :type application_health_policy: :class:`ApplicationHealthPolicy
     <azure.servicefabric.models.ApplicationHealthPolicy>`
    :param update_description:
    :type update_description: :class:`RollingUpgradeUpdateDescription
     <azure.servicefabric.models.RollingUpgradeUpdateDescription>`
    """ 

    _validation = {
        'name': {'required': True},
        'upgrade_kind': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'upgrade_kind': {'key': 'UpgradeKind', 'type': 'str'},
        'application_health_policy': {'key': 'ApplicationHealthPolicy', 'type': 'ApplicationHealthPolicy'},
        'update_description': {'key': 'UpdateDescription', 'type': 'RollingUpgradeUpdateDescription'},
    }

    def __init__(self, name, upgrade_kind="Rolling", application_health_policy=None, update_description=None):
        self.name = name
        self.upgrade_kind = upgrade_kind
        self.application_health_policy = application_health_policy
        self.update_description = update_description
