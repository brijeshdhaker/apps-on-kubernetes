from __future__ import annotations

"""
This is an example DAG which uses SparkKubernetesOperator and SparkKubernetesSensor.
In this example, we create two tasks which execute sequentially.
The first task is to submit sparkApplication on Kubernetes cluster(the example uses spark-pi application).
and the second task is to check the final state of the sparkApplication that submitted in the first state.
Spark-on-k8s operator is required to be already installed on Kubernetes
https://github.com/GoogleCloudPlatform/spark-on-k8s-operator
"""

import os
from datetime import datetime, timedelta

# [START import_module]
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor

# [END import_module]


# [START instantiate_dag]


ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "spark_pi"

with DAG(
        DAG_ID,
        default_args={"max_active_runs": 1},
        description="submit spark-pi as sparkApplication on kubernetes",
        schedule=timedelta(days=1),
        start_date=datetime(2021, 1, 1),
        catchup=False,
) as dag:
    # [START SparkKubernetesOperator_DAG]
    t1 = SparkKubernetesOperator(
        task_id="spark_pi_submit",
        namespace="apache-airflow",
        application_file="example_spark_kubernetes_spark_pi.yaml",
        do_xcom_push=True,
        dag=dag,
    )

    t2 = SparkKubernetesSensor(
        task_id="spark_pi_monitor",
        namespace="apache-airflow",
        application_name="{{ task_instance.xcom_pull(task_ids='spark_pi_submit')['metadata']['name'] }}",
        dag=dag,
    )
    t1 >> t2

    # [END SparkKubernetesOperator_DAG]
    ### from tests.system.utils.watcher import watcher

    # This test needs watcher in order to properly mark success/failure
    # when "tearDown" task with trigger rule is part of the DAG

    ### list(dag.tasks) >> watcher()

### from tests.system.utils import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
### test_run = get_test_run(dag)
