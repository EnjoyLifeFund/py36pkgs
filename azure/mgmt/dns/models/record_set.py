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


class RecordSet(Model):
    """Describes a DNS record set (a collection of DNS records with the same name
    and type).

    :param id: The ID of the record set.
    :type id: str
    :param name: The name of the record set.
    :type name: str
    :param type: The type of the record set.
    :type type: str
    :param etag: The etag of the record set.
    :type etag: str
    :param metadata: The metadata attached to the record set.
    :type metadata: dict
    :param ttl: The TTL (time-to-live) of the records in the record set.
    :type ttl: long
    :param arecords: The list of A records in the record set.
    :type arecords: list of :class:`ARecord <azure.mgmt.dns.models.ARecord>`
    :param aaaa_records: The list of AAAA records in the record set.
    :type aaaa_records: list of :class:`AaaaRecord
     <azure.mgmt.dns.models.AaaaRecord>`
    :param mx_records: The list of MX records in the record set.
    :type mx_records: list of :class:`MxRecord
     <azure.mgmt.dns.models.MxRecord>`
    :param ns_records: The list of NS records in the record set.
    :type ns_records: list of :class:`NsRecord
     <azure.mgmt.dns.models.NsRecord>`
    :param ptr_records: The list of PTR records in the record set.
    :type ptr_records: list of :class:`PtrRecord
     <azure.mgmt.dns.models.PtrRecord>`
    :param srv_records: The list of SRV records in the record set.
    :type srv_records: list of :class:`SrvRecord
     <azure.mgmt.dns.models.SrvRecord>`
    :param txt_records: The list of TXT records in the record set.
    :type txt_records: list of :class:`TxtRecord
     <azure.mgmt.dns.models.TxtRecord>`
    :param cname_record: The CNAME record in the  record set.
    :type cname_record: :class:`CnameRecord
     <azure.mgmt.dns.models.CnameRecord>`
    :param soa_record: The SOA record in the record set.
    :type soa_record: :class:`SoaRecord <azure.mgmt.dns.models.SoaRecord>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': '{str}'},
        'ttl': {'key': 'properties.TTL', 'type': 'long'},
        'arecords': {'key': 'properties.ARecords', 'type': '[ARecord]'},
        'aaaa_records': {'key': 'properties.AAAARecords', 'type': '[AaaaRecord]'},
        'mx_records': {'key': 'properties.MXRecords', 'type': '[MxRecord]'},
        'ns_records': {'key': 'properties.NSRecords', 'type': '[NsRecord]'},
        'ptr_records': {'key': 'properties.PTRRecords', 'type': '[PtrRecord]'},
        'srv_records': {'key': 'properties.SRVRecords', 'type': '[SrvRecord]'},
        'txt_records': {'key': 'properties.TXTRecords', 'type': '[TxtRecord]'},
        'cname_record': {'key': 'properties.CNAMERecord', 'type': 'CnameRecord'},
        'soa_record': {'key': 'properties.SOARecord', 'type': 'SoaRecord'},
    }

    def __init__(self, id=None, name=None, type=None, etag=None, metadata=None, ttl=None, arecords=None, aaaa_records=None, mx_records=None, ns_records=None, ptr_records=None, srv_records=None, txt_records=None, cname_record=None, soa_record=None):
        self.id = id
        self.name = name
        self.type = type
        self.etag = etag
        self.metadata = metadata
        self.ttl = ttl
        self.arecords = arecords
        self.aaaa_records = aaaa_records
        self.mx_records = mx_records
        self.ns_records = ns_records
        self.ptr_records = ptr_records
        self.srv_records = srv_records
        self.txt_records = txt_records
        self.cname_record = cname_record
        self.soa_record = soa_record