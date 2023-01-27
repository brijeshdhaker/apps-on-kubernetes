#
# Apache Airflow
#

helm repo add apache-airflow https://airflow.apache.org/
helm repo update apache-airflow --namespace apache-airflow
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
--set sparkJobNamespace=default  --create-namespace
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
# kube-prometheus-stack
#
helm repo add prometheus https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus/kube-prometheus-stack --namespace prometheus --create-namespace --dry-run

#
# Helm Commands
#
helm repo list

#
# prometheus-operator
#
helm repo add prometheus https://github.com/helm/charts/tree/master/stable/prometheus-operator
helm install prometheus stable/prometheus-operator --namespace monitoring --dry-run


#
# Metallb
#
helm repo add metallb https://metallb.github.io/metallb
helm install metallb metallb/metallb --version 0.13.7 --namespace metallb-system --create-namespace

helm install metallb metallb/metallb -f values.yaml

#
# Copy /tmp/foo from a remote pod to /tmp/bar locally
#

kubectl cp spark-operator/spark-operator-6475f9d6f6-w2rvk:/usr/bin/curl ./curl