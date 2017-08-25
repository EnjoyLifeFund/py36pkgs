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

from .resource_update import ResourceUpdate


class SnapshotUpdate(ResourceUpdate):
    """Snapshot update resource.

    :param tags: Resource tags
    :type tags: dict
    :param account_type: the storage account type of the disk. Possible values
     include: 'Standard_LRS', 'Premium_LRS'
    :type account_type: str or :class:`StorageAccountTypes
     <azure.mgmt.compute.compute.v2016_04_30_preview.models.StorageAccountTypes>`
    :param os_type: the Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or :class:`OperatingSystemTypes
     <azure.mgmt.compute.compute.v2016_04_30_preview.models.OperatingSystemTypes>`
    :param creation_data: disk source information. CreationData information
     cannot be changed after the disk has been created.
    :type creation_data: :class:`CreationData
     <azure.mgmt.compute.compute.v2016_04_30_preview.models.CreationData>`
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings: Encryption settings for disk or snapshot
    :type encryption_settings: :class:`EncryptionSettings
     <azure.mgmt.compute.compute.v2016_04_30_preview.models.EncryptionSettings>`
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'StorageAccountTypes'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'creation_data': {'key': 'properties.creationData', 'type': 'CreationData'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings': {'key': 'properties.encryptionSettings', 'type': 'EncryptionSettings'},
    }

    def __init__(self, tags=None, account_type=None, os_type=None, creation_data=None, disk_size_gb=None, encryption_settings=None):
        super(SnapshotUpdate, self).__init__(tags=tags)
        self.account_type = account_type
        self.os_type = os_type
        self.creation_data = creation_data
        self.disk_size_gb = disk_size_gb
        self.encryption_settings = encryption_settings
