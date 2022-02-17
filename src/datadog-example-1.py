from datadog import initialize, statsd
import os
import time

initialize(statsd_host=os.environ.get('DATADOG_AGENT'))

while(1):
    print('modifying metric')
    statsd.increment('example_metric.increment', tags=["environment:dev"])
    time.sleep(20)

