#
# Helm Commands
#

helm repo add <repo-name> <repo-url>
helm repo list

## List Releases : See what has been released using Helm
helm list

# Helm 3
helm install [RELEASE_NAME] prometheus-community/prometheus

## List deployment yamls
### To Yaml
helm template apache-ariflow apache-airflow/airflow

### To Dir
helm template apache-ariflow apache-airflow/airflow --version 1.5.0 --output-dir ./

## Uninstall
helm uninstall mysql-1612624192

## Help
helm get -h




#
# Apache Airflow
#

helm repo add apache-airflow https://airflow.apache.org/
helm repo update apache-airflow --namespace apache-airflow
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace
helm delete airflow --namespace airflow

helm install apache-airflow apache-airflow/airflow --version 1.5.0

helm install apache-airflow apache-airflow/airflow --version 1.7.0 --namespace apache-airflow
helm template apache-ariflow apache-airflow/airflow --version 1.5.0 --output-dir ./


https://raw.githubusercontent.com/apache/airflow/constraints-2.2.4/constraints-3.8.txt


helm template apache-ariflow apache-airflow/airflow --version 1.5.0 --output-dir ./
helm template ./airflow-1.6.0.tgz --output-dir ./


helm install apache-ariflow apache-airflow/airflow --namespace apache-airflow --version 1.5.0 --dry-run > apache-airflow-install.yaml

#
# Spark Operator
#
$ helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
$ helm install spark-operator spark-operator/spark-operator \
    --create-namespace \
    --namespace spark-operator \
    --set webhook.enable=true \
    --set webhook.port=443 \
    --set metrics.enable=true

$ helm status --namespace spark-operator spark-operator

## Uninstall 
$ helm uninstall spark-operator --namespace spark-operator

#
# NFS Subdir External Provisioner
#
$ helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
$ helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
--set nfs.server=192.168.122.1 \
--set nfs.path=/mnt/nfs-share

#
# NFS Server Provisioner
#
$ helm repo add nfs-ganesha-server-and-external-provisioner https://kubernetes-sigs.github.io/nfs-ganesha-server-and-external-provisioner/
$ helm install nfs-server-provisioner nfs-ganesha-server-and-external-provisioner/nfs-server-provisioner
$ helm delete nfs-server-provisioner


#
# Add the Prometheus Charts Repository
#
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo update

# Install Prometheus:
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace --dry-run
helm uninstall prometheus


# 
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --dry-run
helm uninstall kube-prometheus-stack


#
# kube-prometheus-stack
#
helm install prometheus-adapter prometheus-community/prometheus-adapter --namespace monitoring --create-namespace
helm install pushgateway prometheus-community/prometheus-pushgateway --namespace monitoring --create-namespace --dry-run
helm template prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --dry-run --output-dir ./prometheus-out


helm repo add stable https://charts.helm.sh/stable



#
#
#
kubectl --namespace monitoring port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090
kubectl --namespace monitoring port-forward svc/prometheus-operator-kube-p-alertmanager 9093
kubectl --namespace monitoring port-forward svc/prometheus-grafana 3000:3000
admin / prom-operator


#
# Metallb
#
helm repo add metallb https://metallb.github.io/metallb
helm install metallb metallb/metallb --namespace metallb-system --create-namespace --version 0.13.7

kubectl -n metallb-system  apply -f setup/local/metallb-system/address-pool.yaml

#
# Copy /tmp/foo from a remote pod to /tmp/bar locally
#

kubectl cp spark-operator/spark-operator-6475f9d6f6-w2rvk:/usr/bin/curl ./curl


#
# Obtaining the service account token by using kubectl
#
kubectl get secret --namespace=apache-airflow
kubectl get secret airflow-secrets --namespace=apache-airflow -o yaml


#
# Grafana Dashboards
#
git clone https://github.com/dotdc/grafana-dashboards-kubernetes.git
cd grafana-dashboards-kubernetes


#
# InfluxDb
#
helm repo add influxdata https://helm.influxdata.com/
helm repo update
helm install influxdb influxdata/influxdb --namespace influxdb --create-namespace
helm uninstall influxdb --namespace influxdb

#
# Metrics-server
#
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm upgrade --install metrics-server metrics-server/metrics-server
helm uninstall metrics-server --namespace default