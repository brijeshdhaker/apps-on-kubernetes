#
# kubeadm init
#

/var/lib/kubelet/config.yaml
-n kube-system cm kubelet-config

/etc/kubernetes/kubelet.conf
/var/lib/kubelet/kubeadm-flags.env

systemctl daemon-reload && systemctl restart kubelet

#
# kubeadm join:q!
#

/var/lib/kubelet/config.yaml

/etc/kubernetes/bootstrap-kubelet.conf


http://192.168.122.95:10255/metrics
http://192.168.122.95:10255/metrics/cadvisor
http://192.168.122.95:10255/metrics/probes

curl -k --header "Authorization: Bearer $TOKEN"  https://kubernetes/api/v1/nodes/$NODE_NAME/proxy/configz