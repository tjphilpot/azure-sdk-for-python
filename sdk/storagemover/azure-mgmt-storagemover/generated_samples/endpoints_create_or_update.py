# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.storagemover import StorageMoverMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storagemover
# USAGE
    python endpoints_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageMoverMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="11111111-2222-3333-4444-555555555555",
    )

    response = client.endpoints.create_or_update(
        resource_group_name="examples-rg",
        storage_mover_name="examples-storageMoverName",
        endpoint_name="examples-endpointName",
        endpoint={
            "properties": {
                "blobContainerName": "examples-blobContainerName",
                "description": "Example Storage Container Endpoint Description",
                "endpointType": "AzureStorageBlobContainer",
                "storageAccountResourceId": "/subscriptions/11111111-2222-3333-4444-555555555555/resourceGroups/examples-rg/providers/Microsoft.Storage/storageAccounts/examples-storageAccountName/",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/storagemover/resource-manager/Microsoft.StorageMover/preview/2022-07-01-preview/examples/Endpoints_CreateOrUpdate.json
if __name__ == "__main__":
    main()
