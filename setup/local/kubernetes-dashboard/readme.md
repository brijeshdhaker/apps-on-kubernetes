
#
# Install kubernetes-dashboard
#

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
or
kubectl -n kubernetes-dashboard apply -f setup/local/dashboard/kubernetes-dashboard.yaml

#
## Generate Admin User
#
kubectl -n kubernetes-dashboard apply -f setup/local/dashboard/admin-user-rbac.yaml

#
# Generate Token
#
kubectl -n kubernetes-dashboard create token admin-user

