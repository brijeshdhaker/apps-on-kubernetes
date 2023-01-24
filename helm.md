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

$ helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
$ helm install spark-operator spark-operator/spark-operator --namespace spark-operator --create-namespace
$ helm status --namespace spark-operator spark-operator



#
# Metallb
#
helm repo add metallb https://metallb.github.io/metallb
helm install metallb metallb/metallb
helm install metallb metallb/metallb -f values.yaml