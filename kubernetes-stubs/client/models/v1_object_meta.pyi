import datetime
import typing

import kubernetes.client

class V1ObjectMeta:
    annotations: typing.Optional[typing.Dict[str, str]]
    cluster_name: typing.Optional[str]
    creation_timestamp: typing.Optional[datetime.datetime]
    deletion_grace_period_seconds: typing.Optional[int]
    deletion_timestamp: typing.Optional[datetime.datetime]
    finalizers: typing.Optional[typing.List[str]]
    generate_name: typing.Optional[str]
    generation: typing.Optional[int]
    labels: typing.Optional[typing.Dict[str, str]]
    managed_fields: typing.Optional[typing.List[kubernetes.client.V1ManagedFieldsEntry]]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    owner_references: typing.Optional[typing.List[kubernetes.client.V1OwnerReference]]
    resource_version: typing.Optional[str]
    self_link: typing.Optional[str]
    uid: typing.Optional[str]
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Dict[str, str]] = ...,
        cluster_name: typing.Optional[str] = ...,
        creation_timestamp: typing.Optional[datetime.datetime] = ...,
        deletion_grace_period_seconds: typing.Optional[int] = ...,
        deletion_timestamp: typing.Optional[datetime.datetime] = ...,
        finalizers: typing.Optional[typing.List[str]] = ...,
        generate_name: typing.Optional[str] = ...,
        generation: typing.Optional[int] = ...,
        labels: typing.Optional[typing.Dict[str, str]] = ...,
        managed_fields: typing.Optional[
            typing.List[kubernetes.client.V1ManagedFieldsEntry]
        ] = ...,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        owner_references: typing.Optional[
            typing.List[kubernetes.client.V1OwnerReference]
        ] = ...,
        resource_version: typing.Optional[str] = ...,
        self_link: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1ObjectMetaDict: ...

class V1ObjectMetaDict(typing.TypedDict, total=False):
    annotations: typing.Optional[typing.Dict[str, str]]
    clusterName: typing.Optional[str]
    creationTimestamp: typing.Optional[datetime.datetime]
    deletionGracePeriodSeconds: typing.Optional[int]
    deletionTimestamp: typing.Optional[datetime.datetime]
    finalizers: typing.Optional[typing.List[str]]
    generateName: typing.Optional[str]
    generation: typing.Optional[int]
    labels: typing.Optional[typing.Dict[str, str]]
    managedFields: typing.Optional[
        typing.List[kubernetes.client.V1ManagedFieldsEntryDict]
    ]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    ownerReferences: typing.Optional[
        typing.List[kubernetes.client.V1OwnerReferenceDict]
    ]
    resourceVersion: typing.Optional[str]
    selfLink: typing.Optional[str]
    uid: typing.Optional[str]
