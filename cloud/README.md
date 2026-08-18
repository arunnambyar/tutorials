# ☁️ Cloud Tutorials Index

**Cloud computing** lets you rent compute, storage, networking, and managed services over the internet instead of buying and running your own data centers. You pay for what you use, scale up or down as demand changes, and focus on applications while the provider runs the underlying infrastructure.

The three major public clouds we cover are **AWS** (Amazon Web Services), **Azure** (Microsoft), and **GCP** (Google Cloud Platform). Each offers the same broad building blocks — identity, virtual networks, VMs, serverless, containers, storage, databases, messaging, APIs, and monitoring — under different product names and console experiences.

In these tutorials we **study each platform side by side** and **compare equivalent services**.



## On this page

- [M1 Foundations](#m1-foundations)
- [M2 Identity & access](#m2-identity--access)
- [M3 Networking](#m3-networking)
- [M4 Compute — VMs & autoscaling](#m4-compute--vms--autoscaling)
- [M5 Storage](#m5-storage)
- [M6 Data platforms](#m6-data-platforms)
- [M7 Serverless functions](#m7-serverless-functions)
- [M8 Containers & Kubernetes](#m8-containers--kubernetes)
- [M9 Message queues](#m9-message-queues)
- [M10 Message brokers & events](#m10-message-brokers--events)
- [M11 Scalable background jobs](#m11-scalable-background-jobs)
- [M12 API management](#m12-api-management)
- [M13 Observability](#m13-observability)
- [M14 Ops & IaC](#m14-ops--iac)

## Syllabus by concept

Each numbered item is a shared cloud concept (its own markdown page). Under it:

- **x.1** — equivalent AWS page (Previous / Next / Home / Cloud / Topic)
- **x.2** — equivalent Azure page
- **x.3** — equivalent GCP page

Reading order for each topic: **concept → AWS → Azure → GCP → next concept**.

---
## M1 Foundations

### 1. [What is the cloud / cloud model](./docs/1000_what_is_the_cloud.md)

1.1 AWS — [What is AWS?](./aws/docs/1000_what_is_aws.md)  
1.2 Azure — [What is Azure?](./azure/docs/1000_what_is_azure.md)  
1.3 GCP — [What is Google Cloud?](./gcp/docs/1000_what_is_gcp.md)  
1.4 Compare — [AWS · Azure · GCP at a glance](./docs/1005_aws_azure_gcp_at_a_glance.md)

### 2. [Accounts, subscriptions & projects](./docs/1010_accounts_subscriptions_projects.md)

2.1 AWS — [Accounts & Organizations](./aws/docs/1010_accounts_organizations.md)  
2.2 Azure — [Subscriptions & management groups](./azure/docs/1010_subscriptions_management_groups.md)  
2.3 GCP — [Organizations & folders](./gcp/docs/1010_orgs_folders.md)  
2.4 Setup — [First login & setup (overview)](./docs/1015_first_login_and_setup.md)  
2.5 AWS — [First login & setup](./aws/docs/1015_first_login_setup.md)  
2.6 Azure — [First login & setup](./azure/docs/1015_first_login_setup.md)  
2.7 GCP — [First login & setup](./gcp/docs/1015_first_login_setup.md)

### 3. [Regions & availability zones](./docs/1020_regions_availability_zones.md)

3.1 AWS — [Regions & AZs](./aws/docs/1020_regions_az.md)  
3.2 Azure — [Regions & AZs](./azure/docs/1020_regions_az.md)  
3.3 GCP — [Regions & zones](./gcp/docs/1030_regions_zones.md)

### 4. [Resource hierarchy](./docs/1030_resource_hierarchy.md)

4.1 AWS — [Resource hierarchy](./aws/docs/1030_resource_hierarchy.md)  
4.2 Azure — [Resource groups](./azure/docs/1030_resource_groups.md)  
4.3 GCP — [Resource hierarchy](./gcp/docs/1040_resource_hierarchy.md)

### 5. [Shared responsibility](./docs/1040_shared_responsibility.md)

5.1 AWS — [Shared responsibility](./aws/docs/1040_shared_responsibility.md)  
5.2 Azure — [Shared responsibility](./azure/docs/1040_shared_responsibility.md)  
5.3 GCP — [Shared responsibility](./gcp/docs/1050_shared_responsibility.md)


---

## M2 Identity & access

### 6. [Identity & access (users, roles, policies)](./docs/1100_identity_and_access.md)

6.1 AWS — [IAM](./aws/docs/1100_iam.md)  
6.2 Azure — [Microsoft Entra ID](./azure/docs/1100_entra_id.md)  
6.3 GCP — [IAM](./gcp/docs/1100_iam.md)


---

## M3 Networking

### 7. [Virtual networks](./docs/1200_virtual_networks.md)

7.1 AWS — [VPC](./aws/docs/1200_vpc.md)  
7.2 Azure — [VNet](./azure/docs/1200_vnet.md)  
7.3 GCP — [VPC](./gcp/docs/1200_vpc.md)

### 8. [Subnets & routing](./docs/1210_subnets_routing.md)

8.1 AWS — [Subnets & routing](./aws/docs/1210_subnets_routing.md)  
8.2 Azure — [Subnets & routing](./azure/docs/1210_subnets_routing.md)  
8.3 GCP — [Subnets & routes](./gcp/docs/1210_subnets_routes.md)

### 9. [Internet gateway & NAT](./docs/1220_internet_gateway_nat.md)

9.1 AWS — [IGW / NAT](./aws/docs/1220_igw_nat.md)  
9.2 Azure — [NAT Gateway](./azure/docs/1220_nat_gateway.md)  
9.3 GCP — [Cloud NAT](./gcp/docs/1220_cloud_nat.md)

### 10. [Network security controls](./docs/1230_network_security_controls.md)

10.1 AWS — [Security groups & NACLs](./aws/docs/1230_security_groups_nacls.md)  
10.2 Azure — [NSGs](./azure/docs/1230_nsgs.md)  
10.3 GCP — [Firewall rules](./gcp/docs/1230_firewall_rules.md)

### 11. [Peering & private service access](./docs/1240_peering_private_access.md)

11.1 AWS — [VPC peering / endpoints](./aws/docs/1240_peering_endpoints.md)  
11.2 Azure — [Peering / endpoints](./azure/docs/1240_peering_endpoints.md)  
11.3 GCP — [Peering / Private Google Access](./gcp/docs/1240_peering_private_access.md)

### 12. [Load balancing](./docs/1250_load_balancing.md)

12.1 AWS — [ALB / NLB](./aws/docs/1250_load_balancing.md)  
12.2 Azure — [Load Balancer](./azure/docs/1250_load_balancer.md)  
12.3 GCP — [Cloud Load Balancing](./gcp/docs/1250_load_balancing.md)

### 13. [DNS](./docs/1260_dns.md)

13.1 AWS — [Route 53](./aws/docs/1260_route53.md)  
13.2 Azure — [Azure DNS](./azure/docs/1270_azure_dns.md)  
13.3 GCP — [Cloud DNS](./gcp/docs/1260_cloud_dns.md)


---

## M4 Compute — VMs & autoscaling

### 14. [Virtual machines](./docs/1300_virtual_machines.md)

14.1 AWS — [EC2](./aws/docs/1300_ec2.md)  
14.2 Azure — [Virtual Machines](./azure/docs/1300_virtual_machines.md)  
14.3 GCP — [Compute Engine](./gcp/docs/1300_compute_engine.md)

### 15. [VM autoscaling](./docs/1320_vm_autoscaling.md)

15.1 AWS — [Auto Scaling groups](./aws/docs/1330_auto_scaling_groups.md)  
15.2 Azure — [Virtual Machine Scale Sets](./azure/docs/1320_vmss.md)  
15.3 GCP — [Managed Instance Groups](./gcp/docs/1320_managed_instance_groups.md)


---

## M5 Storage

### 16. [Object storage](./docs/1400_object_storage.md)

16.1 AWS — [S3](./aws/docs/1400_s3.md)  
16.2 Azure — [Blob Storage](./azure/docs/1400_blob_storage.md)  
16.3 GCP — [Cloud Storage](./gcp/docs/1400_cloud_storage.md)

### 17. [Block storage](./docs/1410_block_storage.md)

17.1 AWS — [EBS](./aws/docs/1410_ebs.md)  
17.2 Azure — [Managed disks](./azure/docs/1410_managed_disks.md)  
17.3 GCP — [Persistent Disk](./gcp/docs/1410_persistent_disk.md)

### 18. [File storage](./docs/1420_file_storage.md)

18.1 AWS — [EFS](./aws/docs/1420_efs.md)  
18.2 Azure — [Azure Files](./azure/docs/1420_azure_files.md)  
18.3 GCP — [Filestore](./gcp/docs/1420_filestore.md)

### 19. [Durability & backup](./docs/1430_durability_backup.md)

19.1 AWS — [Durability & backup](./aws/docs/1430_durability_backup.md)  
19.2 Azure — [Durability & backup](./azure/docs/1430_durability_backup.md)  
19.3 GCP — [Durability & backup](./gcp/docs/1430_durability_backup.md)


---

## M6 Data platforms

### 20. [Managed relational databases](./docs/1500_managed_relational_databases.md)

20.1 AWS — [RDS](./aws/docs/1500_rds.md)  
20.2 Azure — [Azure SQL / Database for PostgreSQL](./azure/docs/1500_azure_sql.md)  
20.3 GCP — [Cloud SQL](./gcp/docs/1500_cloud_sql.md)

### 21. [NoSQL / document & wide-column stores](./docs/1510_nosql_stores.md)

21.1 AWS — [DynamoDB](./aws/docs/1510_dynamodb.md)  
21.2 Azure — [Cosmos DB](./azure/docs/1510_cosmos_db.md)  
21.3 GCP — [Firestore / Bigtable](./gcp/docs/1510_firestore_bigtable.md)


---

## M7 Serverless functions

### 22. [Serverless functions](./docs/1600_serverless_functions.md)

22.1 AWS — [Lambda](./aws/docs/1600_lambda.md)  
22.2 Azure — [Azure Functions](./azure/docs/1600_functions.md)  
22.3 GCP — [Cloud Functions](./gcp/docs/1600_cloud_functions.md)


---

## M8 Containers & Kubernetes

### 23. [Container registries](./docs/1700_container_registries.md)

23.1 AWS — [ECR](./aws/docs/1700_ecr.md)  
23.2 Azure — [ACR](./azure/docs/1700_acr.md)  
23.3 GCP — [Artifact Registry](./gcp/docs/1700_artifact_registry.md)

### 24. [Managed containers (non-Kubernetes)](./docs/1710_managed_containers.md)

24.1 AWS — [ECS](./aws/docs/1710_ecs.md)  
24.2 Azure — [Container Apps](./azure/docs/1710_container_apps.md)  
24.3 GCP — [Cloud Run](./gcp/docs/1710_cloud_run.md)

### 25. [Managed Kubernetes](./docs/1720_managed_kubernetes.md)

25.1 AWS — [EKS](./aws/docs/1720_eks.md)  
25.2 Azure — [AKS](./azure/docs/1720_aks.md)  
25.3 GCP — [GKE](./gcp/docs/1720_gke.md)

### 26. [Cluster autoscaling](./docs/1730_cluster_autoscaling.md)

26.1 AWS — [Cluster autoscaling](./aws/docs/1730_cluster_autoscaling.md)  
26.2 Azure — [Cluster autoscaling](./azure/docs/1730_cluster_autoscaling.md)  
26.3 GCP — [Cluster autoscaling](./gcp/docs/1730_cluster_autoscaling.md)


---

## M9 Message queues

### 27. [Message queues](./docs/1800_message_queues.md)

27.1 AWS — [SQS](./aws/docs/1800_sqs.md)  
27.2 Azure — [Storage Queues](./azure/docs/1800_storage_queues.md)  
27.3 GCP — [Pub/Sub pull subscriptions](./gcp/docs/1800_pubsub_pull.md)


---

## M10 Message brokers & events

### 28. [Pub/sub topics & fan-out](./docs/1810_pubsub_fanout.md)

28.1 AWS — [SNS](./aws/docs/1810_sns.md)  
28.2 Azure — [Service Bus Topics](./azure/docs/1820_service_bus_topics.md)  
28.3 GCP — [Pub/Sub topics/push](./gcp/docs/1820_pubsub_topics.md)

### 29. [Managed message brokers (ActiveMQ / RabbitMQ / Kafka)](./docs/1820_managed_brokers.md)

29.1 AWS — [Amazon MQ](./aws/docs/1820_amazon_mq.md)  
29.2 Azure — [Event Hubs](./azure/docs/1830_event_hubs.md)  
29.3 GCP — [Managed Service for Apache Kafka](./gcp/docs/1830_managed_kafka.md)

### 30. [Event buses / event routing](./docs/1840_event_buses.md)

30.1 AWS — [EventBridge](./aws/docs/1840_eventbridge.md)  
30.2 Azure — [Event Grid](./azure/docs/1840_event_grid.md)  
30.3 GCP — [Eventarc](./gcp/docs/1840_eventarc.md)


---

## M11 Scalable background jobs

### 31. [Queue workers & background processing](./docs/1900_queue_workers.md)

31.1 AWS — [Queue workers](./aws/docs/1900_queue_workers.md)  
31.2 Azure — [Queue-triggered Functions / WebJobs](./azure/docs/1900_queue_workers.md)  
31.3 GCP — [Pub/Sub / Cloud Tasks workers](./gcp/docs/1900_queue_workers.md)

### 32. [Batch compute](./docs/1910_batch_compute.md)

32.1 AWS — [AWS Batch](./aws/docs/1910_aws_batch.md)  
32.2 Azure — [Azure Batch](./azure/docs/1910_azure_batch.md)  
32.3 GCP — [Cloud Batch](./gcp/docs/1910_cloud_batch.md)

### 33. [Workflows & durable orchestration](./docs/1920_workflows_orchestration.md)

33.1 AWS — [Step Functions](./aws/docs/1920_step_functions.md)  
33.2 Azure — [Durable Functions](./azure/docs/1920_durable_functions.md)  
33.3 GCP — [Cloud Run jobs](./gcp/docs/1920_cloud_run_jobs.md)

### 34. [Scheduled / cron jobs](./docs/1930_scheduled_jobs.md)

34.1 AWS — [Scheduled / cron jobs](./aws/docs/1930_scheduled_jobs.md)  
34.2 Azure — [Scheduled / cron jobs](./azure/docs/1940_scheduled_jobs.md)  
34.3 GCP — [Scheduled / cron jobs](./gcp/docs/1940_scheduled_jobs.md)


---

## M12 API management

### 35. [API management](./docs/2000_api_management.md)

35.1 AWS — [API Gateway](./aws/docs/2000_api_gateway.md)  
35.2 Azure — [Azure API Management](./azure/docs/2000_api_management.md)  
35.3 GCP — [API Gateway / Apigee](./gcp/docs/2000_api_gateway_apigee.md)


---

## M13 Observability

### 36. [Metrics, logs & alerts](./docs/2100_metrics_logs_alerts.md)

36.1 AWS — [CloudWatch](./aws/docs/2100_cloudwatch.md)  
36.2 Azure — [Azure Monitor](./azure/docs/2100_monitor.md)  
36.3 GCP — [Cloud Monitoring & Logging](./gcp/docs/2100_monitoring_logging.md)

### 37. [Application performance / tracing](./docs/2110_apm_tracing.md)

37.1 AWS — [X-Ray](./aws/docs/2110_xray.md)  
37.2 Azure — [Application Insights](./azure/docs/2110_application_insights.md)  
37.3 GCP — [Cloud Trace](./gcp/docs/2110_cloud_trace.md)


---

## M14 Ops & IaC

### 38. [Infrastructure as code](./docs/2200_infrastructure_as_code.md)

38.1 AWS — [CloudFormation & CDK](./aws/docs/2200_cloudformation_cdk.md)  
38.2 Azure — [Bicep / ARM / Terraform](./azure/docs/2200_bicep_arm_terraform.md)  
38.3 GCP — [Terraform / Deployment Manager](./gcp/docs/2200_terraform_deployment_manager.md)

### 39. [Cost & billing awareness](./docs/2210_cost_billing.md)

39.1 AWS — [Cost & billing](./aws/docs/2210_cost_billing.md)  
39.2 Azure — [Cost & billing](./azure/docs/2210_cost_billing.md)  
39.3 GCP — [Cost & billing](./gcp/docs/2210_cost_billing.md)

---

<p align="right">
    <a href="../README.md">Home</a>
</p>
