import datetime
import typing

from kubernetes.client.models.v1_aws_elastic_block_store_volume_source import (
    V1AWSElasticBlockStoreVolumeSource, V1AWSElasticBlockStoreVolumeSourceDict)
from kubernetes.client.models.v1_azure_disk_volume_source import (
    V1AzureDiskVolumeSource, V1AzureDiskVolumeSourceDict)
from kubernetes.client.models.v1_azure_file_persistent_volume_source import (
    V1AzureFilePersistentVolumeSource, V1AzureFilePersistentVolumeSourceDict)
from kubernetes.client.models.v1_ceph_fs_persistent_volume_source import (
    V1CephFSPersistentVolumeSource, V1CephFSPersistentVolumeSourceDict)
from kubernetes.client.models.v1_cinder_persistent_volume_source import (
    V1CinderPersistentVolumeSource, V1CinderPersistentVolumeSourceDict)
from kubernetes.client.models.v1_csi_persistent_volume_source import (
    V1CSIPersistentVolumeSource, V1CSIPersistentVolumeSourceDict)
from kubernetes.client.models.v1_fc_volume_source import (V1FCVolumeSource,
                                                          V1FCVolumeSourceDict)
from kubernetes.client.models.v1_flex_persistent_volume_source import (
    V1FlexPersistentVolumeSource, V1FlexPersistentVolumeSourceDict)
from kubernetes.client.models.v1_flocker_volume_source import (
    V1FlockerVolumeSource, V1FlockerVolumeSourceDict)
from kubernetes.client.models.v1_gce_persistent_disk_volume_source import (
    V1GCEPersistentDiskVolumeSource, V1GCEPersistentDiskVolumeSourceDict)
from kubernetes.client.models.v1_glusterfs_persistent_volume_source import (
    V1GlusterfsPersistentVolumeSource, V1GlusterfsPersistentVolumeSourceDict)
from kubernetes.client.models.v1_host_path_volume_source import (
    V1HostPathVolumeSource, V1HostPathVolumeSourceDict)
from kubernetes.client.models.v1_iscsi_persistent_volume_source import (
    V1ISCSIPersistentVolumeSource, V1ISCSIPersistentVolumeSourceDict)
from kubernetes.client.models.v1_local_volume_source import (
    V1LocalVolumeSource, V1LocalVolumeSourceDict)
from kubernetes.client.models.v1_nfs_volume_source import (
    V1NFSVolumeSource, V1NFSVolumeSourceDict)
from kubernetes.client.models.v1_object_reference import (
    V1ObjectReference, V1ObjectReferenceDict)
from kubernetes.client.models.v1_photon_persistent_disk_volume_source import (
    V1PhotonPersistentDiskVolumeSource, V1PhotonPersistentDiskVolumeSourceDict)
from kubernetes.client.models.v1_portworx_volume_source import (
    V1PortworxVolumeSource, V1PortworxVolumeSourceDict)
from kubernetes.client.models.v1_quobyte_volume_source import (
    V1QuobyteVolumeSource, V1QuobyteVolumeSourceDict)
from kubernetes.client.models.v1_rbd_persistent_volume_source import (
    V1RBDPersistentVolumeSource, V1RBDPersistentVolumeSourceDict)
from kubernetes.client.models.v1_scale_io_persistent_volume_source import (
    V1ScaleIOPersistentVolumeSource, V1ScaleIOPersistentVolumeSourceDict)
from kubernetes.client.models.v1_storage_os_persistent_volume_source import (
    V1StorageOSPersistentVolumeSource, V1StorageOSPersistentVolumeSourceDict)
from kubernetes.client.models.v1_volume_node_affinity import (
    V1VolumeNodeAffinity, V1VolumeNodeAffinityDict)
from kubernetes.client.models.v1_vsphere_virtual_disk_volume_source import (
    V1VsphereVirtualDiskVolumeSource, V1VsphereVirtualDiskVolumeSourceDict)

class V1PersistentVolumeSpec:
    access_modes: typing.Optional[typing.List[str]]
    aws_elastic_block_store: typing.Optional[V1AWSElasticBlockStoreVolumeSource]
    azure_disk: typing.Optional[V1AzureDiskVolumeSource]
    azure_file: typing.Optional[V1AzureFilePersistentVolumeSource]
    capacity: typing.Optional[typing.Dict[str, str]]
    cephfs: typing.Optional[V1CephFSPersistentVolumeSource]
    cinder: typing.Optional[V1CinderPersistentVolumeSource]
    claim_ref: typing.Optional[V1ObjectReference]
    csi: typing.Optional[V1CSIPersistentVolumeSource]
    fc: typing.Optional[V1FCVolumeSource]
    flex_volume: typing.Optional[V1FlexPersistentVolumeSource]
    flocker: typing.Optional[V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[V1GCEPersistentDiskVolumeSource]
    glusterfs: typing.Optional[V1GlusterfsPersistentVolumeSource]
    host_path: typing.Optional[V1HostPathVolumeSource]
    iscsi: typing.Optional[V1ISCSIPersistentVolumeSource]
    local: typing.Optional[V1LocalVolumeSource]
    mount_options: typing.Optional[typing.List[str]]
    nfs: typing.Optional[V1NFSVolumeSource]
    node_affinity: typing.Optional[V1VolumeNodeAffinity]
    persistent_volume_reclaim_policy: typing.Optional[str]
    photon_persistent_disk: typing.Optional[V1PhotonPersistentDiskVolumeSource]
    portworx_volume: typing.Optional[V1PortworxVolumeSource]
    quobyte: typing.Optional[V1QuobyteVolumeSource]
    rbd: typing.Optional[V1RBDPersistentVolumeSource]
    scale_io: typing.Optional[V1ScaleIOPersistentVolumeSource]
    storage_class_name: typing.Optional[str]
    storageos: typing.Optional[V1StorageOSPersistentVolumeSource]
    volume_mode: typing.Optional[str]
    vsphere_volume: typing.Optional[V1VsphereVirtualDiskVolumeSource]
    def __init__(
        self,
        *,
        access_modes: typing.Optional[typing.List[str]] = ...,
        aws_elastic_block_store: typing.Optional[
            V1AWSElasticBlockStoreVolumeSource
        ] = ...,
        azure_disk: typing.Optional[V1AzureDiskVolumeSource] = ...,
        azure_file: typing.Optional[V1AzureFilePersistentVolumeSource] = ...,
        capacity: typing.Optional[typing.Dict[str, str]] = ...,
        cephfs: typing.Optional[V1CephFSPersistentVolumeSource] = ...,
        cinder: typing.Optional[V1CinderPersistentVolumeSource] = ...,
        claim_ref: typing.Optional[V1ObjectReference] = ...,
        csi: typing.Optional[V1CSIPersistentVolumeSource] = ...,
        fc: typing.Optional[V1FCVolumeSource] = ...,
        flex_volume: typing.Optional[V1FlexPersistentVolumeSource] = ...,
        flocker: typing.Optional[V1FlockerVolumeSource] = ...,
        gce_persistent_disk: typing.Optional[V1GCEPersistentDiskVolumeSource] = ...,
        glusterfs: typing.Optional[V1GlusterfsPersistentVolumeSource] = ...,
        host_path: typing.Optional[V1HostPathVolumeSource] = ...,
        iscsi: typing.Optional[V1ISCSIPersistentVolumeSource] = ...,
        local: typing.Optional[V1LocalVolumeSource] = ...,
        mount_options: typing.Optional[typing.List[str]] = ...,
        nfs: typing.Optional[V1NFSVolumeSource] = ...,
        node_affinity: typing.Optional[V1VolumeNodeAffinity] = ...,
        persistent_volume_reclaim_policy: typing.Optional[str] = ...,
        photon_persistent_disk: typing.Optional[
            V1PhotonPersistentDiskVolumeSource
        ] = ...,
        portworx_volume: typing.Optional[V1PortworxVolumeSource] = ...,
        quobyte: typing.Optional[V1QuobyteVolumeSource] = ...,
        rbd: typing.Optional[V1RBDPersistentVolumeSource] = ...,
        scale_io: typing.Optional[V1ScaleIOPersistentVolumeSource] = ...,
        storage_class_name: typing.Optional[str] = ...,
        storageos: typing.Optional[V1StorageOSPersistentVolumeSource] = ...,
        volume_mode: typing.Optional[str] = ...,
        vsphere_volume: typing.Optional[V1VsphereVirtualDiskVolumeSource] = ...
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeSpecDict: ...

class V1PersistentVolumeSpecDict(typing.TypedDict, total=False):
    accessModes: typing.Optional[typing.List[str]]
    awsElasticBlockStore: typing.Optional[V1AWSElasticBlockStoreVolumeSourceDict]
    azureDisk: typing.Optional[V1AzureDiskVolumeSourceDict]
    azureFile: typing.Optional[V1AzureFilePersistentVolumeSourceDict]
    capacity: typing.Optional[typing.Dict[str, str]]
    cephfs: typing.Optional[V1CephFSPersistentVolumeSourceDict]
    cinder: typing.Optional[V1CinderPersistentVolumeSourceDict]
    claimRef: typing.Optional[V1ObjectReferenceDict]
    csi: typing.Optional[V1CSIPersistentVolumeSourceDict]
    fc: typing.Optional[V1FCVolumeSourceDict]
    flexVolume: typing.Optional[V1FlexPersistentVolumeSourceDict]
    flocker: typing.Optional[V1FlockerVolumeSourceDict]
    gcePersistentDisk: typing.Optional[V1GCEPersistentDiskVolumeSourceDict]
    glusterfs: typing.Optional[V1GlusterfsPersistentVolumeSourceDict]
    hostPath: typing.Optional[V1HostPathVolumeSourceDict]
    iscsi: typing.Optional[V1ISCSIPersistentVolumeSourceDict]
    local: typing.Optional[V1LocalVolumeSourceDict]
    mountOptions: typing.Optional[typing.List[str]]
    nfs: typing.Optional[V1NFSVolumeSourceDict]
    nodeAffinity: typing.Optional[V1VolumeNodeAffinityDict]
    persistentVolumeReclaimPolicy: typing.Optional[str]
    photonPersistentDisk: typing.Optional[V1PhotonPersistentDiskVolumeSourceDict]
    portworxVolume: typing.Optional[V1PortworxVolumeSourceDict]
    quobyte: typing.Optional[V1QuobyteVolumeSourceDict]
    rbd: typing.Optional[V1RBDPersistentVolumeSourceDict]
    scaleIO: typing.Optional[V1ScaleIOPersistentVolumeSourceDict]
    storageClassName: typing.Optional[str]
    storageos: typing.Optional[V1StorageOSPersistentVolumeSourceDict]
    volumeMode: typing.Optional[str]
    vsphereVolume: typing.Optional[V1VsphereVirtualDiskVolumeSourceDict]
