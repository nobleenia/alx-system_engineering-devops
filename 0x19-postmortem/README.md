# Web Service Outage - 503 Service Unavailable errors (March 15, 2023)
![Is Postmortem a joke or a scare to you?](images/images-postmortem.gif "Is Postmortem a Joke To You")

## Issue Summary
- **Duration**: On March 15th, from 10:00 AM to 12:45 PM UTC, our primary web service experienced a significant outage affecting approximately 65% of our user base.
- **Impact**: During this period, users encountered 503 Service Unavailable errors when trying to access our platform, leading to a complete inability to use our service.
- **Root Cause**: The root cause of the outage was identified as an unintentional misconfiguration in our load balancer settings, which led to an overload of requests to a single server instance.

## Timeline

- **10:00 AM UTC**: The issue was first detected when monitoring alerts for high response times and error rates were triggered.
- **10:05 AM UTC**: Initial investigation by the on-call engineer suggested a spike in traffic, but further analysis showed traffic levels were normal.
- **10:20 AM UTC**: Customer support reported a significant increase in user complaints about accessing the service.
- **10:30 AM UTC**: Misleading path: Investigated potential DDoS attack but found no evidence supporting this theory.
- **10:45 AM UTC**: The issue was escalated to the senior infrastructure team for deeper analysis.
- **11:00 AM UTC**: Identified the root cause as a misconfiguration in the load balancer, which wasn't distributing traffic evenly across servers.
- **11:30 AM UTC**: Efforts to manually redistribute traffic were only temporarily successful; the decision was made to roll back recent changes to the load balancer configuration.
- **12:00 PM UTC**: After rollback, traffic began to distribute normally across all server instances.
- **12:45 PM UTC**: Monitoring confirmed the service was fully operational, and the incident was declared resolved.

## Root Cause and Resolution

- **Root Cause**: The outage was caused by a recent update to our load balancer configuration intended to improve traffic handling. Unfortunately, this update contained an error in the weight distribution algorithm, causing most requests to be routed to a single server, overwhelming it, and leading to service failures.
- **Resolution**: The resolution involved rolling back the load balancer configuration to its previous state, which immediately restored normal service distribution and operation.

## Corrective and Preventative Measures

To prevent similar incidents in the future, we have identified several improvements and specific tasks:

1. **Review and update change management procedures** for critical infrastructure settings, ensuring any changes are reviewed by at least two senior engineers before deployment.
2. **Implement a canary release process** for configuration changes, allowing us to monitor the impact on a small portion of the traffic before full deployment.
3. **Enhance load balancer monitoring** to include detailed metrics on traffic distribution across server instances, alerting if an imbalance is detected.
4. **Develop a rollback procedure** for immediate reversion of configuration changes in the event of unexpected service degradation.
5. **Conduct a thorough review of recent changes** to the load balancer settings to understand why the misconfiguration was not caught in testing, leading to the update of our testing procedures to cover such scenarios.
6. **Schedule regular training sessions** for the engineering team on the latest best practices in configuration management and incident response.

## Conclusion

These measures will be implemented to strengthen our system's resilience, improve our response to incidents, and ensure such outages do not recur, maintaining the trust and reliability our users expect from our service.

![Now We Can Rest In Peace!](images/VMFIOyVQV7uWyCUOQdwF--1--t8rh6.jpg "Now We Can Rest In Peace")