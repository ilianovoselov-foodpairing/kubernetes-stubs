import typing

from kubernetes.client.api_client import ApiClient
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1_local_subject_access_review import \
    V1LocalSubjectAccessReview
from kubernetes.client.models.v1_self_subject_access_review import \
    V1SelfSubjectAccessReview
from kubernetes.client.models.v1_self_subject_rules_review import \
    V1SelfSubjectRulesReview
from kubernetes.client.models.v1_subject_access_review import \
    V1SubjectAccessReview

class AuthorizationV1Api:
    def __init__(self, api_client: typing.Optional[ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> V1APIResourceList: ...
    def create_namespaced_local_subject_access_review(
        self,
        namespace: str,
        body: V1LocalSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1LocalSubjectAccessReview: ...
    def create_self_subject_access_review(
        self,
        body: V1SelfSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1SelfSubjectAccessReview: ...
    def create_self_subject_rules_review(
        self,
        body: V1SelfSubjectRulesReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1SelfSubjectRulesReview: ...
    def create_subject_access_review(
        self,
        body: V1SubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> V1SubjectAccessReview: ...
