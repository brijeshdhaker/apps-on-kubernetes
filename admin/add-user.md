#
## Obtaining the service account token from the pod
#
/var/run/secrets/kubernetes.io/serviceaccount

#
## Connecting with the Kubernetes API server
#

https://k8s1m0:6443/

kubernetes.default



curl -v -GET --key /home/brijeshdhaker/cred/brijeshdhaker.key --cert /etc/kubernetes/pki/ca.crt https://192.168.122.95:6443

curl https://kubernetes.default.svc/api/v1/namespaces/XXX/pods?labelSelector=my-label%3Dyes --silent --header "Authorization: Bearer $TOKEN" --insecure

/api/v1/namespaces/engineering/pods
/api/v1/namespaces/engineering/pods

curl -v -GET --cacert /etc/kubernetes/pki/ca.crt --key brijeshdhaker.key --cert brijeshdhaker.crt https://192.168.122.95:6443/api/v1/namespaces

curl -v -GET --cacert /etc/kubernetes/pki/ca.crt https://192.168.122.95:6443/api/v1/namespaces

curl --cacert ca.crt -H "Authorization: Bearer {token}" https://kubernetes.default/api/v1/pod/namespaces/{namespace}


curl --cacert /home/brijeshdhaker/cred/ca.crt -H "Authorization: Bearer {token}" http://192.168.122.48:10249/metrics


eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5DZFY5VGVGTUR4SWNBbDJUbklablI4R3ZYUzdXUmFsNUcwb3BPcVpxM0EifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc1NDMzNDg4LCJpYXQiOjE2NzU0Mjk4ODgsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJrdWJlLXByb3h5IiwidWlkIjoiYTBlMTEyNDMtMTRiMy00NmRlLTg5NjEtMzE1YmNiNTM1NzhjIn19LCJuYmYiOjE2NzU0Mjk4ODgsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTprdWJlLXByb3h5In0.cT5rm_uIkf3Ila1Ya0Fc3TQ7YBPYsAQw5kwH2S0lmUOkyg_SkS1-JPWvqVNjR5-iAXpi-bBiSVcUMQ2X0o_uEFnxeO5WqsD29yOjmp8VodMB5JzlSk4q6bouMSfmnyHAxIgSjq8SsevrIhBNPTV1-amf-23cswy5DJvyVaWRKtZ8SawjluUKJ0g1v5d-XLk9pyZrH8_B98gNDZNQ8vPnCRklNvQw1pCrNyXj8qVnQodWD_c-Xo8hhZsOVAdl2BqxKcwDqhl40lq5B9P0HyuiLZ_FAREyS9qKOjxoBeSJqIbwA_8owwAXL7KD0BHdppSahYuJGoej54GaYuPGjzap7Q

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
## Using the service account token with kubectl
#

#
## Obtaining the service account token by using kubectl
#
1. Get information about your Kubernetes secret object. Secrets are used to store access credentials.
kubectl get secret --namespace={namespace}
2. 
2. Get details of the service account token.
   kubectl get secret default-token-2mfqv --namespace={namespace} -o yaml
3. 

#
#
#
/etc/kubernetes/kubelet.kubeconfig
#
#
#

### Rationale
#### The apiserver, by default, does not authenticate itself to the kubelet’s HTTPS endpoints. The requests from the apiserver are treated anonymously. You should set up certificate-based kubelet authentication to ensure that the apiserver authenticates itself to kubelets when submitting requests.


### Audit
#### Run the following command on the master node:

ps -ef | grep kube-apiserver

Verify that the --kubelet-client-certificate and --kubelet-client-key arguments exist and they are set as appropriate.


kube-apiserver \
    --advertise-address=192.168.122.95 \
    --allow-privileged=true \
    --authorization-mode=Node,RBAC \
    --client-ca-file=/etc/kubernetes/pki/ca.crt \
    --enable-admission-plugins=NodeRestriction \
    --enable-bootstrap-token-auth=true \
    --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt \
    --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt \
    --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key \
    --etcd-servers=https://127.0.0.1:2379 \
    --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt \
    --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key \
    --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname \
    --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt \
    --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key \
    --requestheader-allowed-names=front-proxy-client \
    --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt \
    --requestheader-extra-headers-prefix=X-Remote-Extra- \
    --requestheader-group-headers=X-Remote-Group \
    --requestheader-username-headers=X-Remote-User \
    --secure-port=6443 \
    --service-account-issuer=https://kubernetes.default.svc.cluster.local \
    --service-account-key-file=/etc/kubernetes/pki/sa.pub \
    --service-account-signing-key-file=/etc/kubernetes/pki/sa.key \
    --service-cluster-ip-range=172.28.0.0/16 \
    --tls-cert-file=/etc/kubernetes/pki/apiserver.crt \
    --tls-private-key-file=/etc/kubernetes/pki/apiserver.key


--client-ca-file=/etc/kubernetes/pki/ca.crt
--kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key \
-kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key \

### Remediation
#### Follow the Kubernetes documentation and set up the TLS connection between the apiserver and kubelets. Then, edit API server pod specification file /etc/kubernetes/manifests/kube-apiserver.yaml on the master node and set the kubelet client certificate and key parameters as below.

--kubelet-client-certificate=<path/to/client-certificate-file>
--kubelet-client-key=<path/to/client-key-file>

### Impact
#### You require TLS to be configured on apiserver as well as kubelets.

### Default value
#### By default, certificate-based kubelet authentication is not set.



/etc/kubernetes/manifests/kube-apiserver.yaml

#
# X509 Client Certs
#

1. Create a private key file 
   openssl genrsa -out brijeshdhaker.key 2048

2. Generate Singing Request
   openssl req -new -key brijeshdhaker.key -out brijeshdhaker.csr -subj "/CN=brijeshdhaker/O=system:masters"

   This would create a CSR for the username "brijeshdhaker", belonging to two groups, "Engineering" and "Admin".

3. Encode CSR into base64 string
   cat brijeshdhaker.csr | base64 | tr -d '\n'
   LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ2d6Q0NBV3NDQVFBd1BqRVdNQlFHQTFVRUF3d05ZbkpwYW1WemFHUm9ZV3RsY2pFVU1CSUdBMVVFQ2d3TApaVzVuYVc1bFpYSnBibWN4RGpBTUJnTlZCQW9NQldGa2JXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DCkFROEFNSUlCQ2dLQ0FRRUExazVSZDRWWHRWUittdkc2MGczQUxSc2EvcnBQVE9Pazk0Z0d3Um9kdU5jcStmbjEKUEN4RDVTa3FIaHlhbWhTeUowL1pQaDB4REtBeld1dVVwQk9Wa2R3N0d2Mk1iVTYybTZVajl4VkZZeUt3YXVIQwpBcTQ3eTY5ZllkeUNwemZZbWhUSHhwYlo3cDBJUjM1Q2I4NDcydmJ6RGhQQ09rRjM0bERkOUhDdU1sWnV5UXF1CmhudXpXbWFodkxXM2xEb0pSNnRMbUpnZHVrT3h3K0VZTWtETHptT01JZEpIeFh2eWFpYmhDQXRvNm1JVmlJdjcKU3lIOXp1MUJFLzBZcms4a0ZoeDZoM043aVdLMzVZY3dFTHNMRG16NkF4RGF0TmFpcVBYV0lLd0RqTG4vMGphYgorVVVxUXF1d1ZzdDMwcEhtRHRhNjV6MkxNbkVGWlhQQVQ3cS9Xd0lEQVFBQm9BQXdEUVlKS29aSWh2Y05BUUVMCkJRQURnZ0VCQUcwVm1KcU9XQU1lTTRSMjVPMy9tcXhwTXVaMVNIdnpxc0U1SnZOT0I0aldwME9WcXBhTmN1Z20Kc3VqdXh5UCtsUkoybEdwZTVoU09yOExoQ09UTlFnR2lhbEFaMTNJcFY0OXQyRjRYZ0RiQW5wYnhpMUl3REU0VwpRbWVlTXBxMlNoaTlFaW9wQzM3RTdrek1Md0d2eGpKQjBSdSt2Z0kreWRQdUwrWFd3QTFSUjZiUHBsNHJxdmNiCkx1UG9VaHBPMDBYSjV1Y0dDazBraHVndjZ2QzZQeTNCclIwblg2SWU2NU1NSUY1UEtLN1dvdkw5b3k2elg2RVcKN0V1VE9ROStCOHhKYWo4R014Snc2dmNvd2pXNk0xUFpZMW0vODNwUW51dlRJRnRudEcwbEVwWjc4RUVtVk1idwpOTVZoaittVzRCNGRkZVpkNXV4NTlVTmRQdjFpdVlRPQotLS0tLUVORCBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0K

4. Submit CSR Request
   kubectl apply -f admin/user/brijeshdhaker-csr.yaml

5. Admin will approve CSR 
    kubectl certificate approve brijeshdhaker-csr

6. kubectl get csr brijeshdhaker-csr -o json

7. kubectl get csr brijeshdhaker-csr -o jsonpath={.status.certificate} | base64 --decode > brijeshdhaker.crt

8. kubectl config set-credentials brijeshdhaker  --client-certificate=brijeshdhaker.crt --client-key=brijeshdhaker.key

9. kubectl config view

10. kubectl auth can-i list pods --namespace kube-system
 
11. kubectl auth can-i list pods --namespace kube-system --as brijesdhaker

## Authorization 


sudo netstat -tulpn | grep LISTEN