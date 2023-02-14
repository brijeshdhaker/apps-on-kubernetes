
# Use this if you started InfluxDB uising a docker image
docker exec -it influx /bin/bash

# Start the InfluxDB CLI
/usr/bin/influx


Supported InfluxQL queries
DELETE*
DROP MEASUREMENT*
EXPLAIN ANALYZE
SELECT (read-only)

SHOW DATABASES
_internal
graphite
sparkmeasure

SHOW RETENTION POLICIES [ON <database_name>]



SHOW SERIES ON graphite

SHOW SERIES ON [DATABASES] FROM [MEASUREMENTS] WHERE [<tag_key>] <operator> [ '<tag_value>' | <regular_expression>]] LIMIT [_clause] OFFSET [_clause]

SHOW SERIES ON graphite FROM "total.used" WHERE "applicationid" = 'spark-f1cf00be683343e9b0fcf6b46a72d902' LIMIT 20
SHOW SERIES ON graphite FROM "JVMHeapMemory" WHERE "applicationid" = 'spark-f1cf00be683343e9b0fcf6b46a72d902' LIMIT 20

// Returns all series in JVMHeapMemory that contain a timestamp in the last 2 days.
SHOW SERIES ON graphite FROM "JVMHeapMemory" WHERE time > now() - 2d

SHOW MEASUREMENTS
SHOW MEASUREMENTS [ON <database_name>] [WITH MEASUREMENT <operator> ['<measurement_name>' | <regular_expression>]] [WHERE <tag_key> <operator> ['<tag_value>' | <regular_expression>]] [LIMIT_clause] [OFFSET_clause]



SHOW TAG KEYS [ON <database_name>] [FROM_clause] [WHERE <tag_key> <operator> ['<tag_value>' | <regular_expression>]] [LIMIT_clause] [OFFSET_clause]
SHOW TAG KEYS
SHOW TAG KEYS ON "graphite" FROM "total.used"
SHOW TAG KEYS ON "graphite" FROM "total.used" LIMIT 1 OFFSET 1

SHOW TAG VALUES [ON <database_name>][FROM_clause] WITH KEY [ [<operator> "<tag_key>" | <regular_expression>] | [IN ("<tag_key1>","<tag_key2")]] [WHERE <tag_key> <operator> ['<tag_value>' | <regular_expression>]] [LIMIT_clause] [OFFSET_clause]
SHOW TAG VALUES
SHOW TAG VALUES WITH KEY = "applicationid"
SHOW TAG VALUES ON "graphite" WITH KEY IN ("applicationid","namespace") WHERE "randtag" =~ /./ LIMIT 3

SHOW FIELD KEYS [ON <database_name>] [FROM <measurement_name>]
SHOW FIELD KEYS ON "graphite" from "total.used"




> use sparkmeasure
executors_started
jobs_ended
jobs_started
stage_metrics
stages_ended
stages_started
task_metrics
tasks_ended
tasks_started


> show series
executors_started,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
executors_started,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
executors_started,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
executors_started,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
executors_started,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
executors_started,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
executors_started,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
jobs_ended,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
jobs_ended,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
jobs_ended,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
jobs_ended,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
jobs_ended,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
jobs_ended,applicationId=spark-a10e967102f04f7795b39df0b12de11c
jobs_ended,applicationId=spark-b7f7dfe85add42b2acb6bc34567c06ee
jobs_ended,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
jobs_ended,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
jobs_started,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
jobs_started,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
jobs_started,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
jobs_started,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
jobs_started,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
jobs_started,applicationId=spark-a10e967102f04f7795b39df0b12de11c
jobs_started,applicationId=spark-b7f7dfe85add42b2acb6bc34567c06ee
jobs_started,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
jobs_started,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
stage_metrics,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
stage_metrics,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
stage_metrics,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
stage_metrics,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
stage_metrics,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
stage_metrics,applicationId=spark-a10e967102f04f7795b39df0b12de11c
stage_metrics,applicationId=spark-b7f7dfe85add42b2acb6bc34567c06ee
stage_metrics,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
stage_metrics,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
stages_ended,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
stages_ended,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
stages_ended,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
stages_ended,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
stages_ended,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
stages_ended,applicationId=spark-a10e967102f04f7795b39df0b12de11c
stages_ended,applicationId=spark-b7f7dfe85add42b2acb6bc34567c06ee
stages_ended,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
stages_ended,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
stages_started,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
stages_started,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
stages_started,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
stages_started,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
stages_started,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
stages_started,applicationId=spark-a10e967102f04f7795b39df0b12de11c
stages_started,applicationId=spark-b7f7dfe85add42b2acb6bc34567c06ee
stages_started,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
stages_started,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
task_metrics,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
task_metrics,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
task_metrics,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
task_metrics,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
task_metrics,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
task_metrics,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
task_metrics,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
tasks_ended,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
tasks_ended,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
tasks_ended,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
tasks_ended,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
tasks_ended,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
tasks_ended,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
tasks_ended,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902
tasks_started,applicationId=spark-0812cea087df4cd09e7561cc3887d2a3
tasks_started,applicationId=spark-10e1eb7426fd4af0842a5336fe3e61d9
tasks_started,applicationId=spark-4740ae89f0024073828b557ab56fc6fe
tasks_started,applicationId=spark-7c9f8c4cf7d64bb58881a82f30ec4e44
tasks_started,applicationId=spark-94f09f8ec63b4fc29bb6f3d672f9284b
tasks_started,applicationId=spark-c44069f7411d46ca929483c6c1fd5b55
tasks_started,applicationId=spark-f1cf00be683343e9b0fcf6b46a72d902

> select * from queries_started


select * from /executors/

#
## List of the Task Metrics collected by InfluxDBSink
#
stageId
attemptNumber
failureReason
submissionTime
completionTime
executorRunTime
executorCpuTime
executorDeserializeCpuTime
executorDeserializeTime
jvmGCTime
memoryBytesSpilled
peakExecutionMemory
resultSerializationTime
resultSize
inputMetrics.bytesRead
inputMetrics.recordsRead
outputMetrics.bytesWritten
outputMetrics.recordsWritten
shuffleReadMetrics.totalBytesRead
shuffleReadMetrics.remoteBytesRead
shuffleReadMetrics.remoteBytesReadToDisk
shuffleReadMetrics.localBytesRead
shuffleReadMetrics.totalBlocksFetched
shuffleReadMetrics.localBlocksFetched
shuffleReadMetrics.remoteBlocksFetched
shuffleReadMetrics.recordsRead
shuffleReadMetrics.fetchWaitTime
shuffleWriteMetrics.bytesWritten
shuffleWriteMetrics.recordsWritten
shuffleWriteMetrics.writeTime