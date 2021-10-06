import datetime
import typing

from kubernetes.client.models.admissionregistration_v1_webhook_client_config import (
    AdmissionregistrationV1WebhookClientConfig,
    AdmissionregistrationV1WebhookClientConfigDict)
from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1_rule_with_operations import (
    V1RuleWithOperations, V1RuleWithOperationsDict)

class V1ValidatingWebhook:
    admission_review_versions: typing.List[str]
    client_config: AdmissionregistrationV1WebhookClientConfig
    failure_policy: typing.Optional[str]
    match_policy: typing.Optional[str]
    name: str
    namespace_selector: typing.Optional[V1LabelSelector]
    object_selector: typing.Optional[V1LabelSelector]
    rules: typing.Optional[typing.List[V1RuleWithOperations]]
    side_effects: str
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        admission_review_versions: typing.List[str],
        client_config: AdmissionregistrationV1WebhookClientConfig,
        failure_policy: typing.Optional[str] = ...,
        match_policy: typing.Optional[str] = ...,
        name: str,
        namespace_selector: typing.Optional[V1LabelSelector] = ...,
        object_selector: typing.Optional[V1LabelSelector] = ...,
        rules: typing.Optional[typing.List[V1RuleWithOperations]] = ...,
        side_effects: str,
        timeout_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1ValidatingWebhookDict: ...

class V1ValidatingWebhookDict(typing.TypedDict, total=False):
    admissionReviewVersions: typing.List[str]
    clientConfig: AdmissionregistrationV1WebhookClientConfigDict
    failurePolicy: typing.Optional[str]
    matchPolicy: typing.Optional[str]
    name: str
    namespaceSelector: typing.Optional[V1LabelSelectorDict]
    objectSelector: typing.Optional[V1LabelSelectorDict]
    rules: typing.Optional[typing.List[V1RuleWithOperationsDict]]
    sideEffects: str
    timeoutSeconds: typing.Optional[int]
