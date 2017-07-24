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


class HttpMessage(Model):
    """HTTP message.

    :param content: HTTP message content.
    :type content: object
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'object'},
    }

    def __init__(self, content=None):
        self.content = content
