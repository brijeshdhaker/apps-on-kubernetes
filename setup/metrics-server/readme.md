#
# https://github.com/kubernetes-sigs/metrics-server
#

#
#
#
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

#
#
#
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm upgrade --install metrics-server metrics-server/metrics-server

## Uninstall
$ helm uninstall metrics-server