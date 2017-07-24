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


class JobPipelineRunInformation(Model):
    """Run info for a specific job pipeline.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar run_id: the run identifier of an instance of pipeline executions (a
     GUID).
    :vartype run_id: str
    :ivar last_submit_time: the time this instance was last submitted.
    :vartype last_submit_time: datetime
    """

    _validation = {
        'run_id': {'readonly': True},
        'last_submit_time': {'readonly': True},
    }

    _attribute_map = {
        'run_id': {'key': 'runId', 'type': 'str'},
        'last_submit_time': {'key': 'lastSubmitTime', 'type': 'iso-8601'},
    }

    def __init__(self):
        self.run_id = None
        self.last_submit_time = None
