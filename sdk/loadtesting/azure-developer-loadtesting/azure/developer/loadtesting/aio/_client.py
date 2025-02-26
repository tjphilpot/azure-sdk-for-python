# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core.credentials_async import AsyncTokenCredential
from azure.core import AsyncPipelineClient
from azure.core.rest import HttpRequest, AsyncHttpResponse

from .._generated.aio._configuration import LoadTestingClientConfiguration
from .._generated._serialization import Deserializer, Serializer
from .._generated.aio.operations import AdministrationOperations, TestRunOperations

class _BaseClient:  # pylint: disable=client-accepts-api-version-keyword
    """These APIs allow end users to create, view and run load tests using Azure Load Test Service.

    :ivar administration: AdministrationOperations operations
    :vartype administration: azure.developer.loadtesting.aio.operations.AdministrationOperations
    :ivar test_run: TestRunOperations operations
    :vartype test_run: azure.developer.loadtesting.aio.operations.TestRunOperations
    :param endpoint: URL to perform data plane API operations on the resource. Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. Default value is "2022-11-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, endpoint: str, credential: "AsyncTokenCredential", **kwargs: Any) -> None:
        _endpoint = "https://{Endpoint}"
        self._config = LoadTestingClientConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        super().__init__(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)


class LoadAdministrationClient(_BaseClient, AdministrationOperations):  # pylint: disable=client-accepts-api-version-keyword
    """These APIs allow end users to create, view and run load tests using Azure Load Test Service.

    :param endpoint: URL to perform data plane API operations on the resource. Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. Default value is "2022-11-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    async def __aenter__(self) -> "AdministrationClient":
        await self._client.__aenter__()
        return self

class LoadTestRunClient(_BaseClient, TestRunOperations):  # pylint: disable=client-accepts-api-version-keyword
    """These APIs allow end users to create, view and run load tests using Azure Load Test Service.

    :param endpoint: URL to perform data plane API operations on the resource. Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. Default value is "2022-11-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    async def __aenter__(self) -> "TestRunClient":
        await self._client.__aenter__()
        return self
