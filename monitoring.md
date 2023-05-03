#
# Monitor Kubernetes API Server
#
https://k8c1m0:6443/metrics

$ curl --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://kuberntes.default.svc/api
$ curl --cacert /etc/kubernetes/pki/ca.crt -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://kuberntes.default.svc/api

cat /etc/kubernetes/admin.conf
## extract keys from admin.conf
 client-crt.dhaker <client-certificate-data>
 client-key.dhaker <client-key-data>
 cat client-crt.dhaker | base64 -d  > client.crt
 cat client-key.dhaker | base64 -d  > client.key

$ curl --cacert /etc/kubernetes/pki/ca.crt --cert /root/client.crt --key /root/client.key https://k8c1m0:6443/metrics



#
# Monitor kubelet 
#
https://k8c1m0:10250/metrics

$ curl -k --cert /etc/kubernetes/pki/apiserver-kubelet-client.crt --key /etc/kubernetes/pki/apiserver-kubelet-client.key https://k8c1m0:10250/metrics
$ curl --cacert /etc/kubernetes/pki/ca.crt --cert /etc/kubernetes/pki/apiserver-kubelet-client.crt --key /etc/kubernetes/pki/apiserver-kubelet-client.key https://k8c1m0:10250/metrics


#
# Monitor etcd
# The official port for etcd client requests, the same one that you need to get access to the /metrics endpoint, is 2379
https://k8c1m0:2379

$ curl --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key https://k8c1m0:2379/metrics

$ ETCDCTL_API=3 etcdctl \
--endpoints k8c1m0:2379,k8c1s1:2379,k8c1s2:2379 \
--cert=/etc/kubernetes/pki/etcd/server.crt \
--key=/etc/kubernetes/pki/etcd/server.key \
--cacert=/etc/kubernetes/pki/etcd/ca.crt \
endpoint status --write-out=table

$ ETCDCTL_API=3 etcdctl \
--endpoints k8c1m0:2379 \
--cert=/etc/kubernetes/pki/etcd/server.crt \
--key=/etc/kubernetes/pki/etcd/server.key \
--cacert=/etc/kubernetes/pki/etcd/ca.crt \
get / --prefix --keys-only

--trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt
--cert-file=/etc/kubernetes/pki/etcd/server.crt
--key-file=/etc/kubernetes/pki/etcd/server.key



#
# Monitor Kubernetes Controller Manager
# https://127.0.0.1:10257/metrics
# https://k8c1m0:10257/metrics

$ curl -k -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://localhost:10257/metrics

$ curl --cacert /etc/kubernetes/pki/ca.crt -H "Authorization: Bearer $(cat /etc/kubernetes/pki/sa.key)" https://localhost:10257/metrics
$ curl -k --cacert /etc/kubernetes/pki/ca.crt --cert /etc/kubernetes/pki/front-proxy-client.crt --key /etc/kubernetes/pki/front-proxy-client.key https://localhost:10257/metrics

$ curl -k --cacert /etc/kubernetes/pki/ca.crt --cert /root/client.crt --key /root/client.key https://localhost:10257/metrics

#
# Monitor kube-proxy
# https://127.0.0.1:10249/metrics
# https://k8c1m0:10249/metrics

curl http://127.0.0.1:10249/metrics

#
# Monitor CoreDNS
#

kubectl get ep kube-dns -n kube-system -o json |jq -r ".subsets"
curl http://172.16.182.140:9153/metrics


# kubectl get svc -n kube-system
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   129d
# kubectl exec -it my-pod -n default -- /bin/bash
# curl http://kube-dns.kube-system.svc:9153/metrics

