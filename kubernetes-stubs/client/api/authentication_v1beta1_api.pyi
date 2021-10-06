import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1beta1_token_review import V1beta1TokenReview

class AuthenticationV1beta1Api:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> V1APIResourceList: ...
    def create_token_review(
        self,
        body: V1beta1TokenReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1beta1TokenReview: ...
