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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ApplicationsOperations(object):
    """ApplicationsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: Client API version. Constant value: "1.6".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "1.6"

        self.config = config

    def create(
            self, parameters, custom_headers=None, raw=False, **operation_config):
        """Create a new application.

        :param parameters: The parameters for creating an application.
        :type parameters: :class:`ApplicationCreateParameters
         <azure.graphrbac.models.ApplicationCreateParameters>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: :class:`Application <azure.graphrbac.models.Application>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: :class:`Application <azure.graphrbac.models.Application>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = '/{tenantID}/applications'
        path_format_arguments = {
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ApplicationCreateParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [201]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Application', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def list(
            self, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists applications by filter parameters.

        :param filter: The filters to apply to the operation.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`Application
         <azure.graphrbac.models.Application>`
        :rtype: :class:`ApplicationPaged
         <azure.graphrbac.models.ApplicationPaged>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/{tenantID}/applications'
                path_format_arguments = {
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ApplicationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ApplicationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def delete(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Delete an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = '/{tenantID}/applications/{applicationObjectId}'
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Get an application by object ID.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: :class:`Application <azure.graphrbac.models.Application>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: :class:`Application <azure.graphrbac.models.Application>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = '/{tenantID}/applications/{applicationObjectId}'
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Application', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def patch(
            self, application_object_id, parameters, custom_headers=None, raw=False, **operation_config):
        """Update an existing application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param parameters: Parameters to update an existing application.
        :type parameters: :class:`ApplicationUpdateParameters
         <azure.graphrbac.models.ApplicationUpdateParameters>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = '/{tenantID}/applications/{applicationObjectId}'
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ApplicationUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list_key_credentials(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Get the keyCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`KeyCredential
         <azure.graphrbac.models.KeyCredential>`
        :rtype: :class:`KeyCredentialPaged
         <azure.graphrbac.models.KeyCredentialPaged>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/{tenantID}/applications/{applicationObjectId}/keyCredentials'
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.KeyCredentialPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.KeyCredentialPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def update_key_credentials(
            self, application_object_id, value, custom_headers=None, raw=False, **operation_config):
        """Update the keyCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param value: A collection of KeyCredentials.
        :type value: list of :class:`KeyCredential
         <azure.graphrbac.models.KeyCredential>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.KeyCredentialsUpdateParameters(value=value)

        # Construct URL
        url = '/{tenantID}/applications/{applicationObjectId}/keyCredentials'
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'KeyCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list_password_credentials(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Get the passwordCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`PasswordCredential
         <azure.graphrbac.models.PasswordCredential>`
        :rtype: :class:`PasswordCredentialPaged
         <azure.graphrbac.models.PasswordCredentialPaged>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/{tenantID}/applications/{applicationObjectId}/passwordCredentials'
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.PasswordCredentialPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.PasswordCredentialPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def update_password_credentials(
            self, application_object_id, value, custom_headers=None, raw=False, **operation_config):
        """Update passwordCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param value: A collection of PasswordCredentials.
        :type value: list of :class:`PasswordCredential
         <azure.graphrbac.models.PasswordCredential>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.PasswordCredentialsUpdateParameters(value=value)

        # Construct URL
        url = '/{tenantID}/applications/{applicationObjectId}/passwordCredentials'
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'PasswordCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
