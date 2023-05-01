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


http://k8c1m0:10255/metrics
http://k8c1m0:10255/metrics/cadvisor
http://k8c1m0:10255/metrics/probes

#
# Kubelet APIS
# Kubelet is instrumented and exposes the /metrics endpoint by default through the port 10250
#
https://k8c1m0:10250/metrics


#
# SSL HIT
#
export CACERT=/etc/kubernetes/pki/ca.crt
export TOKEN=`cat /var/run/secrets/kubernetes.io/serviceaccount/token`
export API_SERVER=$(kubectl config view | grep server | cut -f 2- -d ":" | tr -d " ")
export NODE_NAME=k8c1m0
curl -k -v -GET --cacert ${CACERT} --header "Authorization: Bearer $TOKEN"  ${API_SERVER}/api/v1/nodes/$NODE_NAME/proxy/containerLogs/kube-system/coredns-1234567890-abcde/coredns

#
# kubelet : get secure metrics & logs
#

export TOKEN=`cat /var/run/secrets/kubernetes.io/serviceaccount/token`
export APISERVER=https://kubernetes.default.svc.cluster.local
curl -k --header "Authorization: Bearer $TOKEN"  https://$NODE_NAME:10250/metrics
curl -k --header "Authorization: Bearer $TOKEN"  $APISERVER/api/v1/nodes/${NODE_NAME}/proxy/metrics

## In secure port
curl http://$NODE_NAME:10255/metrics/cadvisor

#
# Access API Server from outside
#
export SERVICE_ACCOUNT=node-admin
export NAMESPACE=sys-admin
export NODE_NAME=k8c1m0
export APISERVER=$(kubectl config view | grep server | cut -f 2- -d ":" | tr -d " ")
export TOKEN=`kubectl -n ${NAMESPACE} create token ${SERVICE_ACCOUNT}`

curl -k --header "Authorization: Bearer $TOKEN"  $APISERVER/api/v1/nodes/${NODE_NAME}/proxy/metrics

curl -k --header "Authorization: Bearer ${TOKEN}"  https://${NODE_NAME}:10250/metrics



#
# Kubelet APIs
#
curl -k --header "Authorization: Bearer $TOKEN"  https://kubernetes/api/v1/nodes/$NODE_NAME/proxy/configz
curl -k --header "Authorization: Bearer $TOKEN"  https://kubernetes/api/v1/nodes/$NODE_NAME/proxy/logs/
curl -k --header "Authorization: Bearer $TOKEN"  https://kubernetes/api/v1/nodes/$NODE_NAME/proxy/logs/auth.log
curl -k --header "Authorization: Bearer $TOKEN"  https://kubernetes/api/v1/nodes/$NODE_NAME/proxy/containerLogs/kube-system/coredns-1234567890-abcde/coredns
curl -k --header "Authorization: Bearer $TOKEN"  https://kubernetes/api/v1/nodes/$NODE_NAME/proxy/runningpods/



curl -v -GET --cacert admin/user/ca.crt --key admin/user/brijeshdhaker.key --cert admin/user/brijeshdhaker.crt https://k8c1m0:6443/api/v1/namespaces
curl -GET --cacert admin/user/ca.crt --key admin/user/brijeshdhaker.key --cert admin/user/brijeshdhaker.crt https://k8c1m0:6443/api/v1/namespaces/engineering/pods/$HOSTNAME
curl -GET --cacert admin/user/ca.crt --key admin/user/brijeshdhaker.key --cert admin/user/brijeshdhaker.crt https://k8c1m0:6443/api/v1/nodes/$NODE_NAME/proxy/runningpods/