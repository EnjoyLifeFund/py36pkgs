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


class ServiceTypeHealthPolicy(Model):
    """Represents the health policy used to evaluate the health of services
    belonging to a service type.
    .

    :param max_percent_unhealthy_partitions_per_service: The maximum allowed
     percentage of unhealthy partitions per service. Allowed values are Byte
     values from zero to 100
     The percentage represents the maximum tolerated percentage of partitions
     that can be unhealthy before the service is considered in error.
     If the percentage is respected but there is at least one unhealthy
     partition, the health is evaluated as Warning.
     The percentage is calculated by dividing the number of unhealthy
     partitions over the total number of partitions in the service.
     The computation rounds up to tolerate one failure on small numbers of
     partitions. Default percentage is zero.
     . Default value: 0 .
    :type max_percent_unhealthy_partitions_per_service: int
    :param max_percent_unhealthy_replicas_per_partition: The maximum allowed
     percentage of unhealthy replicas per partition. Allowed values are Byte
     values from zero to 100.
     The percentage represents the maximum tolerated percentage of replicas
     that can be unhealthy before the partition is considered in error.
     If the percentage is respected but there is at least one unhealthy
     replica, the health is evaluated as Warning.
     The percentage is calculated by dividing the number of unhealthy replicas
     over the total number of replicas in the partition.
     The computation rounds up to tolerate one failure on small numbers of
     replicas. Default percentage is zero.
     . Default value: 0 .
    :type max_percent_unhealthy_replicas_per_partition: int
    :param max_percent_unhealthy_services: The maximum maximum allowed
     percentage of unhealthy services. Allowed values are Byte values from
     zero to 100.
     The percentage represents the maximum tolerated percentage of services
     that can be unhealthy before the application is considered in error.
     If the percentage is respected but there is at least one unhealthy
     service, the health is evaluated as Warning.
     This is calculated by dividing the number of unhealthy services of the
     specific service type over the total number of services of the specific
     service type.
     The computation rounds up to tolerate one failure on small numbers of
     services. Default percentage is zero.
     . Default value: 0 .
    :type max_percent_unhealthy_services: int
    """ 

    _attribute_map = {
        'max_percent_unhealthy_partitions_per_service': {'key': 'MaxPercentUnhealthyPartitionsPerService', 'type': 'int'},
        'max_percent_unhealthy_replicas_per_partition': {'key': 'MaxPercentUnhealthyReplicasPerPartition', 'type': 'int'},
        'max_percent_unhealthy_services': {'key': 'MaxPercentUnhealthyServices', 'type': 'int'},
    }

    def __init__(self, max_percent_unhealthy_partitions_per_service=0, max_percent_unhealthy_replicas_per_partition=0, max_percent_unhealthy_services=0):
        self.max_percent_unhealthy_partitions_per_service = max_percent_unhealthy_partitions_per_service
        self.max_percent_unhealthy_replicas_per_partition = max_percent_unhealthy_replicas_per_partition
        self.max_percent_unhealthy_services = max_percent_unhealthy_services
