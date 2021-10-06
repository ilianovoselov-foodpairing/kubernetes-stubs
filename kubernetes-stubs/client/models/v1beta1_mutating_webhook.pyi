import datetime
import typing

from kubernetes.client.models.admissionregistration_v1beta1_webhook_client_config import (
    AdmissionregistrationV1beta1WebhookClientConfig,
    AdmissionregistrationV1beta1WebhookClientConfigDict)
from kubernetes.client.models.v1_label_selector import (V1LabelSelector,
                                                        V1LabelSelectorDict)
from kubernetes.client.models.v1beta1_rule_with_operations import (
    V1beta1RuleWithOperations, V1beta1RuleWithOperationsDict)

class V1beta1MutatingWebhook:
    admission_review_versions: typing.Optional[typing.List[str]]
    client_config: AdmissionregistrationV1beta1WebhookClientConfig
    failure_policy: typing.Optional[str]
    match_policy: typing.Optional[str]
    name: str
    namespace_selector: typing.Optional[V1LabelSelector]
    object_selector: typing.Optional[V1LabelSelector]
    reinvocation_policy: typing.Optional[str]
    rules: typing.Optional[typing.List[V1beta1RuleWithOperations]]
    side_effects: typing.Optional[str]
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        admission_review_versions: typing.Optional[typing.List[str]] = ...,
        client_config: AdmissionregistrationV1beta1WebhookClientConfig,
        failure_policy: typing.Optional[str] = ...,
        match_policy: typing.Optional[str] = ...,
        name: str,
        namespace_selector: typing.Optional[V1LabelSelector] = ...,
        object_selector: typing.Optional[V1LabelSelector] = ...,
        reinvocation_policy: typing.Optional[str] = ...,
        rules: typing.Optional[typing.List[V1beta1RuleWithOperations]] = ...,
        side_effects: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1MutatingWebhookDict: ...

class V1beta1MutatingWebhookDict(typing.TypedDict, total=False):
    admissionReviewVersions: typing.Optional[typing.List[str]]
    clientConfig: AdmissionregistrationV1beta1WebhookClientConfigDict
    failurePolicy: typing.Optional[str]
    matchPolicy: typing.Optional[str]
    name: str
    namespaceSelector: typing.Optional[V1LabelSelectorDict]
    objectSelector: typing.Optional[V1LabelSelectorDict]
    reinvocationPolicy: typing.Optional[str]
    rules: typing.Optional[typing.List[V1beta1RuleWithOperationsDict]]
    sideEffects: typing.Optional[str]
    timeoutSeconds: typing.Optional[int]
