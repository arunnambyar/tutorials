# ☁️ Cloud Tutorials Index

**Cloud computing** lets you rent compute, storage, networking, and managed services over the internet instead of buying and running your own data centers. You pay for what you use, scale up or down as demand changes, and focus on applications while the provider runs the underlying infrastructure.

The three major public clouds we cover are **AWS** (Amazon Web Services), **Azure** (Microsoft), and **GCP** (Google Cloud Platform). Each offers the same broad building blocks — identity, virtual networks, VMs, serverless, containers, storage, databases, messaging, APIs, and monitoring — under different product names and console experiences.

In these tutorials we **study each platform side by side** and **compare equivalent services**, so the same syllabus (foundations → networking → compute → data → messaging → ops) maps cleanly across AWS, Azure, and GCP. Each provider has its own tree (`docs`, `code`, `static`, `tools`), same layout as Design Patterns.

---

## On this page

- [AWS](#aws)
- [Azure](#azure)
- [GCP](#gcp)

---

## AWS

[AWS Tutorials](./aws/README.md) · [Docs index](./aws/docs/index.md)

| Module | Topic |
|--------|--------|
| **M1** | [**Foundations**](./aws/docs/1000_foundations.md) — [cloud model](./aws/docs/1000_foundations.md); [accounts & organizations](./aws/docs/1010_accounts_organizations.md); [regions & AZs](./aws/docs/1020_regions_az.md); [resource hierarchy](./aws/docs/1030_resource_hierarchy.md); [shared responsibility](./aws/docs/1040_shared_responsibility.md) |
| **M2** | [**Identity & access**](./aws/docs/1100_iam.md) — [IAM users, groups, roles, policies](./aws/docs/1100_iam.md); least privilege; MFA; instance/service roles |
| **M3** | [**Networking**](./aws/docs/1200_vpc.md) — [VPC](./aws/docs/1200_vpc.md); [subnets & routing](./aws/docs/1210_subnets_routing.md); [IGW/NAT](./aws/docs/1220_igw_nat.md); [security groups & NACLs](./aws/docs/1230_security_groups_nacls.md); [VPC peering/endpoints](./aws/docs/1240_peering_endpoints.md); [ALB/NLB](./aws/docs/1250_load_balancing.md); [Route 53](./aws/docs/1260_route53.md) |
| **M4** | [**Compute — VMs & autoscaling**](./aws/docs/1300_ec2.md) — [EC2](./aws/docs/1300_ec2.md); [AMIs & instance types](./aws/docs/1310_amis_instance_types.md); [launch templates](./aws/docs/1320_launch_templates.md); [**Auto Scaling groups**](./aws/docs/1330_auto_scaling_groups.md) (policies, health checks, scheduled scaling) |
| **M5** | [**Storage**](./aws/docs/1400_s3.md) — [S3](./aws/docs/1400_s3.md) (tiers, lifecycle, versioning); [EBS](./aws/docs/1410_ebs.md); [EFS](./aws/docs/1420_efs.md); [durability & backup](./aws/docs/1430_durability_backup.md) |
| **M6** | [**Data platforms**](./aws/docs/1500_rds.md) — [RDS](./aws/docs/1500_rds.md) (engines, Multi-AZ, replicas); [DynamoDB](./aws/docs/1510_dynamodb.md) (keys, capacity, consistency) |
| **M7** | [**Serverless functions**](./aws/docs/1600_lambda.md) — [Lambda](./aws/docs/1600_lambda.md); triggers; packaging; concurrency; cold starts; IAM for functions |
| **M8** | [**Containers & Kubernetes**](./aws/docs/1720_eks.md) — [ECR](./aws/docs/1700_ecr.md); [ECS](./aws/docs/1710_ecs.md); [**EKS**](./aws/docs/1720_eks.md) (clusters, node groups, workloads, networking); [cluster autoscaling](./aws/docs/1730_cluster_autoscaling.md) |
| **M9** | [**Message queues**](./aws/docs/1800_sqs.md) — [**SQS**](./aws/docs/1800_sqs.md) (standard/FIFO); visibility timeout; DLQ; fan-out with queues |
| **M10** | [**Message brokers & events**](./aws/docs/1810_sns.md) — [**SNS**](./aws/docs/1810_sns.md); [**Amazon MQ**](./aws/docs/1820_amazon_mq.md) (ActiveMQ/RabbitMQ); [**MSK**](./aws/docs/1830_msk.md) (Kafka); [EventBridge](./aws/docs/1840_eventbridge.md) |
| **M11** | [**Scalable background jobs**](./aws/docs/1900_queue_workers.md) — [queue workers](./aws/docs/1900_queue_workers.md) (SQS + EC2/ECS/Lambda); [**AWS Batch**](./aws/docs/1910_aws_batch.md); [Step Functions](./aws/docs/1920_step_functions.md); [scheduled/cron jobs](./aws/docs/1930_scheduled_jobs.md) |
| **M12** | [**API management**](./aws/docs/2000_api_gateway.md) — [**API Gateway**](./aws/docs/2000_api_gateway.md) (REST/HTTP/WebSocket); auth; throttling; stages; integration with Lambda/HTTP |
| **M13** | [**Observability**](./aws/docs/2100_cloudwatch.md) — [CloudWatch](./aws/docs/2100_cloudwatch.md) metrics, logs, alarms; [**X-Ray**](./aws/docs/2110_xray.md) / application performance monitoring |
| **M14** | [**Ops & IaC**](./aws/docs/2200_cloudformation_cdk.md) — [CloudFormation & CDK](./aws/docs/2200_cloudformation_cdk.md); [cost & billing awareness](./aws/docs/2210_cost_billing.md) |

---

## Azure

[Azure Tutorials](./azure/README.md) · [Docs index](./azure/docs/index.md)

| Module | Topic |
|--------|--------|
| **M1** | [**Foundations**](./azure/docs/1000_foundations.md) — [cloud model](./azure/docs/1000_foundations.md); [subscriptions & management groups](./azure/docs/1010_subscriptions_management_groups.md); [regions & AZs](./azure/docs/1020_regions_az.md); [resource groups](./azure/docs/1030_resource_groups.md); [shared responsibility](./azure/docs/1040_shared_responsibility.md) |
| **M2** | [**Identity & access**](./azure/docs/1100_entra_id.md) — [Microsoft Entra ID](./azure/docs/1100_entra_id.md); users/apps; [RBAC](./azure/docs/1110_rbac.md); least privilege; MFA; [managed identities](./azure/docs/1120_managed_identities.md) |
| **M3** | [**Networking**](./azure/docs/1200_vnet.md) — [VNet](./azure/docs/1200_vnet.md); [subnets & routing](./azure/docs/1210_subnets_routing.md); [NAT Gateway](./azure/docs/1220_nat_gateway.md); [NSGs](./azure/docs/1230_nsgs.md); [peering/endpoints](./azure/docs/1240_peering_endpoints.md); [Load Balancer](./azure/docs/1250_load_balancer.md); [Application Gateway](./azure/docs/1260_application_gateway.md); [Azure DNS](./azure/docs/1270_azure_dns.md) |
| **M4** | [**Compute — VMs & autoscaling**](./azure/docs/1300_virtual_machines.md) — [Virtual Machines](./azure/docs/1300_virtual_machines.md); [images & sizes](./azure/docs/1310_images_sizes.md); [**Virtual Machine Scale Sets**](./azure/docs/1320_vmss.md) (autoscale rules, health, scheduled scaling) |
| **M5** | [**Storage**](./azure/docs/1400_blob_storage.md) — [Blob Storage](./azure/docs/1400_blob_storage.md) (tiers, lifecycle, versioning); [managed disks](./azure/docs/1410_managed_disks.md); [Azure Files](./azure/docs/1420_azure_files.md); [durability & backup](./azure/docs/1430_durability_backup.md) |
| **M6** | [**Data platforms**](./azure/docs/1500_azure_sql.md) — [Azure SQL / Database for PostgreSQL](./azure/docs/1500_azure_sql.md) (HA, replicas); [Cosmos DB](./azure/docs/1510_cosmos_db.md) (APIs, consistency) |
| **M7** | [**Serverless functions**](./azure/docs/1600_functions.md) — [**Azure Functions**](./azure/docs/1600_functions.md); triggers/bindings; hosting plans; cold starts; identity for functions |
| **M8** | [**Containers & Kubernetes**](./azure/docs/1720_aks.md) — [ACR](./azure/docs/1700_acr.md); [Container Apps](./azure/docs/1710_container_apps.md) (intro); [**AKS**](./azure/docs/1720_aks.md) (clusters, node pools, workloads, networking); [cluster autoscaling](./azure/docs/1730_cluster_autoscaling.md) |
| **M9** | [**Message queues**](./azure/docs/1800_storage_queues.md) — [**Storage Queues**](./azure/docs/1800_storage_queues.md); [**Service Bus Queues**](./azure/docs/1810_service_bus_queues.md); peek-lock; DLQ; competing consumers |
| **M10** | [**Message brokers & events**](./azure/docs/1820_service_bus_topics.md) — [**Service Bus Topics**](./azure/docs/1820_service_bus_topics.md); [**Event Hubs**](./azure/docs/1830_event_hubs.md) (Kafka-compatible); [**Event Grid**](./azure/docs/1840_event_grid.md) |
| **M11** | [**Scalable background jobs**](./azure/docs/1900_queue_workers.md) — [queue-triggered Functions / WebJobs](./azure/docs/1900_queue_workers.md); [**Azure Batch**](./azure/docs/1910_azure_batch.md); [Durable Functions](./azure/docs/1920_durable_functions.md); [Container Apps jobs](./azure/docs/1930_container_apps_jobs.md); [scheduled/cron jobs](./azure/docs/1940_scheduled_jobs.md) |
| **M12** | [**API management**](./azure/docs/2000_api_management.md) — [**Azure API Management**](./azure/docs/2000_api_management.md) (APIs, products, policies); auth; throttling; revisions; backend integration |
| **M13** | [**Observability**](./azure/docs/2100_monitor.md) — [Azure Monitor](./azure/docs/2100_monitor.md) metrics, logs, alerts; [**Application Insights**](./azure/docs/2110_application_insights.md) |
| **M14** | [**Ops & IaC**](./azure/docs/2200_bicep_arm_terraform.md) — [Bicep / ARM / Terraform](./azure/docs/2200_bicep_arm_terraform.md); [cost & billing awareness](./azure/docs/2210_cost_billing.md) |

---

## GCP

[GCP Tutorials](./gcp/README.md) · [Docs index](./gcp/docs/index.md)

| Module | Topic |
|--------|--------|
| **M1** | [**Foundations**](./gcp/docs/1000_foundations.md) — [cloud model](./gcp/docs/1000_foundations.md); [organizations & folders](./gcp/docs/1010_orgs_folders.md); [projects](./gcp/docs/1020_projects.md); [regions & zones](./gcp/docs/1030_regions_zones.md); [resource hierarchy](./gcp/docs/1040_resource_hierarchy.md); [shared responsibility](./gcp/docs/1050_shared_responsibility.md) |
| **M2** | [**Identity & access**](./gcp/docs/1100_iam.md) — [IAM](./gcp/docs/1100_iam.md) principals, roles, policies; least privilege; MFA; [service accounts](./gcp/docs/1110_service_accounts.md) |
| **M3** | [**Networking**](./gcp/docs/1200_vpc.md) — [VPC](./gcp/docs/1200_vpc.md); [subnets & routes](./gcp/docs/1210_subnets_routes.md); [Cloud NAT](./gcp/docs/1220_cloud_nat.md); [firewall rules](./gcp/docs/1230_firewall_rules.md); [peering/Private Google Access](./gcp/docs/1240_peering_private_access.md); [Cloud Load Balancing](./gcp/docs/1250_load_balancing.md); [Cloud DNS](./gcp/docs/1260_cloud_dns.md) |
| **M4** | [**Compute — VMs & autoscaling**](./gcp/docs/1300_compute_engine.md) — [Compute Engine](./gcp/docs/1300_compute_engine.md); [images & machine types](./gcp/docs/1310_images_machine_types.md); [**Managed Instance Groups**](./gcp/docs/1320_managed_instance_groups.md) (autoscaling policies, health checks, scheduled scaling) |
| **M5** | [**Storage**](./gcp/docs/1400_cloud_storage.md) — [Cloud Storage](./gcp/docs/1400_cloud_storage.md) (classes, lifecycle, versioning); [Persistent Disk](./gcp/docs/1410_persistent_disk.md); [Filestore](./gcp/docs/1420_filestore.md); [durability & backup](./gcp/docs/1430_durability_backup.md) |
| **M6** | [**Data platforms**](./gcp/docs/1500_cloud_sql.md) — [Cloud SQL](./gcp/docs/1500_cloud_sql.md) (HA, replicas); [Firestore / Bigtable](./gcp/docs/1510_firestore_bigtable.md) (consistency, access patterns) |
| **M7** | [**Serverless functions**](./gcp/docs/1600_cloud_functions.md) — [**Cloud Functions**](./gcp/docs/1600_cloud_functions.md); triggers; packaging; concurrency; cold starts; service accounts for functions |
| **M8** | [**Containers & Kubernetes**](./gcp/docs/1720_gke.md) — [Artifact Registry](./gcp/docs/1700_artifact_registry.md); [Cloud Run](./gcp/docs/1710_cloud_run.md) (intro); [**GKE**](./gcp/docs/1720_gke.md) (clusters, node pools, workloads, networking); [cluster autoscaling](./gcp/docs/1730_cluster_autoscaling.md) |
| **M9** | [**Message queues**](./gcp/docs/1800_pubsub_pull.md) — [**Pub/Sub** pull subscriptions](./gcp/docs/1800_pubsub_pull.md); [**Cloud Tasks**](./gcp/docs/1810_cloud_tasks.md); ack deadlines; DLQ; competing consumers |
| **M10** | [**Message brokers & events**](./gcp/docs/1820_pubsub_topics.md) — [**Pub/Sub** topics/push](./gcp/docs/1820_pubsub_topics.md); [**Managed Service for Apache Kafka**](./gcp/docs/1830_managed_kafka.md); [Eventarc](./gcp/docs/1840_eventarc.md) |
| **M11** | [**Scalable background jobs**](./gcp/docs/1900_queue_workers.md) — [Pub/Sub / Cloud Tasks workers](./gcp/docs/1900_queue_workers.md); [**Cloud Batch**](./gcp/docs/1910_cloud_batch.md); [Cloud Run jobs](./gcp/docs/1920_cloud_run_jobs.md); [Workflows](./gcp/docs/1930_workflows.md); [scheduled/cron jobs](./gcp/docs/1940_scheduled_jobs.md) |
| **M12** | [**API management**](./gcp/docs/2000_api_gateway_apigee.md) — [**API Gateway** / Apigee](./gcp/docs/2000_api_gateway_apigee.md) (APIs, products, policies); auth; throttling; backends |
| **M13** | [**Observability**](./gcp/docs/2100_monitoring_logging.md) — [Cloud Monitoring & Logging](./gcp/docs/2100_monitoring_logging.md); alerts; [**Cloud Trace**](./gcp/docs/2110_cloud_trace.md) / application performance monitoring |
| **M14** | [**Ops & IaC**](./gcp/docs/2200_terraform_deployment_manager.md) — [Terraform / Deployment Manager](./gcp/docs/2200_terraform_deployment_manager.md); [cost & billing awareness](./gcp/docs/2210_cost_billing.md) |

---

<p align="right">
    <a href="../README.md">Home</a>
</p>
