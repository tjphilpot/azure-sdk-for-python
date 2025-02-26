# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._configuration_operations import build_get_request, build_patch_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConfigurationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.eventhub.v2021_11_01.aio.EventHubManagementClient`'s
        :attr:`configuration` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: _models.ClusterQuotaConfigurationProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.ClusterQuotaConfigurationProperties]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource. Required.
        :type parameters: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterQuotaConfigurationProperties or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.ClusterQuotaConfigurationProperties]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterQuotaConfigurationProperties or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: Union[_models.ClusterQuotaConfigurationProperties, IO],
        **kwargs: Any
    ) -> Optional[_models.ClusterQuotaConfigurationProperties]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource. Is either a
         ClusterQuotaConfigurationProperties type or a IO type. Required.
        :type parameters: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterQuotaConfigurationProperties or None or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-11-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.ClusterQuotaConfigurationProperties]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ClusterQuotaConfigurationProperties")

        request = build_patch_request(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.patch.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("ClusterQuotaConfigurationProperties", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ClusterQuotaConfigurationProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}/quotaConfiguration/default"
    }

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, cluster_name: str, **kwargs: Any
    ) -> _models.ClusterQuotaConfigurationProperties:
        """Get all Event Hubs Cluster settings - a collection of key/value pairs which represent the
        quotas and settings imposed on the cluster.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster. Required.
        :type cluster_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterQuotaConfigurationProperties or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_11_01.models.ClusterQuotaConfigurationProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-11-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))
        cls: ClsType[_models.ClusterQuotaConfigurationProperties] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ClusterQuotaConfigurationProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}/quotaConfiguration/default"
    }
