from unittest.mock import Mock, patch

import pytest

from azure.ai.ml._scope_dependent_operations import OperationScope
from azure.ai.ml.operations import VirtualClusterOperations


@pytest.fixture
def mock_credential() -> Mock:
    yield Mock()


@pytest.fixture
def mock_vc_operation(mock_workspace_scope: OperationScope, mock_credential) -> VirtualClusterOperations:
    yield VirtualClusterOperations(operation_scope=mock_workspace_scope, credentials=mock_credential)


@pytest.mark.unittest
@pytest.mark.virtual_cluster_test
class TestVCOperations:
    @patch("azure.ai.ml.operations._virtual_cluster_operations.get_virtual_clusters_from_subscriptions")
    def test_list(
        self,
        mock_function,
        mock_vc_operation: VirtualClusterOperations,
        mock_workspace_scope: OperationScope,
        mock_credential: Mock,
    ) -> None:
        dummy_vc_list = [
            {
                "id": "id1",
                "name": "name1",
            },
            {
                "id": "id2",
                "name": "name2",
            },
        ]

        mock_function.return_value = dummy_vc_list
        result = mock_vc_operation.list()

        assert dummy_vc_list == result
        mock_function.assert_called_once_with(mock_credential, subscription_list=None)

        dummy_sub_list = [mock_workspace_scope.subscription_id]
        result2 = mock_vc_operation.list(scope="subscription")
        assert dummy_vc_list == result2
        mock_function.assert_called_with(mock_credential, subscription_list=dummy_sub_list)

        assert mock_function.call_count == 2

    @patch("azure.ai.ml.operations._virtual_cluster_operations.get_virtual_cluster_by_id")
    def test_get(
        self,
        mock_function,
        mock_vc_operation: VirtualClusterOperations,
        mock_workspace_scope: OperationScope,
        mock_credential: Mock,
    ) -> None:
        dummy_vc = {
            "id": "id1",
            "name": "name1",
        }
        mock_function.return_value = dummy_vc

        result = mock_vc_operation.get("name1")
        assert dummy_vc == result

        mock_function.assert_called_once_with(
            name="name1",
            resource_group=mock_workspace_scope.resource_group_name,
            subscription_id=mock_workspace_scope.subscription_id,
            credential=mock_credential,
        )
