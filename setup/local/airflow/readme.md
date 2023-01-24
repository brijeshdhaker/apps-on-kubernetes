#
#
#

helm repo add apache-airflow https://airflow.apache.org/
helm repo update apache-airflow --namespace airflow

helm install apache-airflow apache-airflow/airflow --version 1.5.0

helm install apache-airflow apache-airflow/airflow --version 1.7.0 --namespace airflow

helm template apache-ariflow apache-airflow/airflow --version 1.5.0 --output-dir ./

https://raw.githubusercontent.com/apache/airflow/constraints-2.2.4/constraints-3.8.txt

```
NAME: apache-airflow
LAST DEPLOYED: Wed Dec 28 14:28:50 2022
NAMESPACE: airflow
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thank you for installing Apache Airflow 2.4.1!

Your release is named apache-airflow.
You can now access your dashboard(s) by executing the following command(s) and visiting the corresponding port at localhost in your browser:

Airflow Webserver:     kubectl port-forward svc/apache-airflow-webserver 8080:8080 --namespace airflow
Default Webserver (Airflow UI) Login credentials:
username: admin
password: admin
Default Postgres connection credentials:
username: postgres
password: postgres
port: 5432

You can get Fernet Key value by running the following:

    echo Fernet Key: $(kubectl get secret --namespace airflow apache-airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)

###########################################################
#  WARNING: You should set a static webserver secret key  #
###########################################################

You are using a dynamically generated webserver secret key, which can lead to
unnecessary restarts of your Airflow components.

Information on how to set a static webserver secret key can be found here:
https://airflow.apache.org/docs/helm-chart/stable/production-guide.html#webserver-secret-key
```

# For Airflow <1.10.14:
airflow create_user --username airflow --lastname airflow --firstname jon --email airflow@apache.org --role Admin --password airflow

# For Airflow >=2.0.0:
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
airflow users  create --role Admin --username airflow --email airflow --firstname airflow --lastname airflow --password airflow

mkdir airflow-yaml
cd airflow-yaml
helm -n airflow template apache-airflow --output-dir ./airflow-yaml /home/brijeshdhaker/.cache/helm/repository/airflow-1.7.0.tgz


kubectl apply -f postgres-service -n airflow
kubectl exec --stdin --tty {container_name} -- /bin/bash

sudo apt-get update
sudo apt-get install Python3.8
AIRFLOW_VERSION=2.2.4
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}
/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[postgres]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow db init

#
#
#

kubectl apply -f scheduler-serviceaccount.yaml -n airflow
kubectl apply -f pod-launcher-role.yaml -n airflow
kubectl apply -f pod-launcher-rolebinding.yaml -n airflow 

kubectl apply -f airflow-deployment.yaml -n airflow 

kubectl apply -f airflow-service.yaml -n airflow
kubectl describe service webserver-svc -n airflow 


#
#
#

helm upgrade apache-airflow apache-airflow/airflow \
--namespace airflow \
--set dags.persistence.enabled=true \
--set dags.persistence.existingClaim=airflow-dags-nfs-pvc \
--set dags.gitSync.enabled=false