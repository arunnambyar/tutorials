/**
 * Generates shared concept pages + Prev/Next/Home/Cloud/Topic nav
 * for all 39 cloud syllabus topics.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CLOUD = path.resolve(__dirname, "..");
const DOCS = path.join(CLOUD, "docs");

/** @typedef {{ n: number, module: string, title: string, slug: string, blurb: string, aws: {file: string, label: string, related?: {file: string, label: string}[]}, azure: {file: string, label: string, related?: {file: string, label: string}[]}, gcp: {file: string, label: string, related?: {file: string, label: string}[]} }} Topic */

/** @type {Topic[]} */
const TOPICS = [
  {
    n: 1,
    module: "M1 Foundations",
    title: "What is the cloud / cloud model",
    slug: "1000_what_is_the_cloud",
    blurb:
      "Cloud computing means renting compute, storage, networking, and managed services over the internet instead of running your own data center.",
    aws: { file: "1000_what_is_aws.md", label: "What is AWS?" },
    azure: { file: "1000_what_is_azure.md", label: "What is Azure?" },
    gcp: { file: "1000_what_is_gcp.md", label: "What is Google Cloud?" },
  },
  {
    n: 2,
    module: "M1 Foundations",
    title: "Accounts, subscriptions & projects",
    slug: "1010_accounts_subscriptions_projects",
    blurb:
      "Every cloud needs a billing and isolation boundary: AWS accounts (and Organizations), Azure subscriptions (and management groups), and GCP projects (under orgs and folders).",
    aws: {
      file: "1010_accounts_organizations.md",
      label: "Accounts & Organizations",
      related: [{ file: "1100_accounts_regions_az.md", label: "Accounts, Regions, and Availability Zones" }],
    },
    azure: {
      file: "1010_subscriptions_management_groups.md",
      label: "Subscriptions & management groups",
      related: [{ file: "1100_subscriptions_regions.md", label: "Subscriptions, resource groups, and regions" }],
    },
    gcp: {
      file: "1010_orgs_folders.md",
      label: "Organizations & folders",
      related: [
        { file: "1020_projects.md", label: "Projects" },
        { file: "1100_projects_regions_zones.md", label: "Projects, regions, and zones" },
      ],
    },
  },
  {
    n: 3,
    module: "M1 Foundations",
    title: "Regions & availability zones",
    slug: "1020_regions_availability_zones",
    blurb:
      "Regions are geographic areas. Availability zones (or zones) are isolated locations inside a region used for higher availability.",
    aws: {
      file: "1020_regions_az.md",
      label: "Regions & AZs",
      related: [{ file: "1100_accounts_regions_az.md", label: "Accounts, Regions, and Availability Zones" }],
    },
    azure: {
      file: "1020_regions_az.md",
      label: "Regions & AZs",
      related: [{ file: "1100_subscriptions_regions.md", label: "Subscriptions, resource groups, and regions" }],
    },
    gcp: {
      file: "1030_regions_zones.md",
      label: "Regions & zones",
      related: [{ file: "1100_projects_regions_zones.md", label: "Projects, regions, and zones" }],
    },
  },
  {
    n: 4,
    module: "M1 Foundations",
    title: "Resource hierarchy",
    slug: "1030_resource_hierarchy",
    blurb:
      "Cloud resources sit in a hierarchy so you can organize, govern, and apply policy at the right level.",
    aws: { file: "1030_resource_hierarchy.md", label: "Resource hierarchy" },
    azure: { file: "1030_resource_groups.md", label: "Resource groups" },
    gcp: { file: "1040_resource_hierarchy.md", label: "Resource hierarchy" },
  },
  {
    n: 5,
    module: "M1 Foundations",
    title: "Shared responsibility",
    slug: "1040_shared_responsibility",
    blurb:
      "The provider secures the cloud; you secure what you put in the cloud. Exact lines shift by service type (IaaS, PaaS, SaaS).",
    aws: { file: "1040_shared_responsibility.md", label: "Shared responsibility" },
    azure: { file: "1040_shared_responsibility.md", label: "Shared responsibility" },
    gcp: { file: "1050_shared_responsibility.md", label: "Shared responsibility" },
  },
  {
    n: 6,
    module: "M2 Identity & access",
    title: "Identity & access (users, roles, policies)",
    slug: "1100_identity_and_access",
    blurb:
      "Identity and access control answer who can do what. Expect users or principals, roles, policies, least privilege, MFA, and identities for machines/services.",
    aws: {
      file: "1100_iam.md",
      label: "IAM",
      related: [{ file: "1200_iam.md", label: "IAM (users, roles, policies)" }],
    },
    azure: {
      file: "1100_entra_id.md",
      label: "Microsoft Entra ID",
      related: [
        { file: "1110_rbac.md", label: "RBAC" },
        { file: "1120_managed_identities.md", label: "Managed identities" },
        { file: "1200_entra_rbac.md", label: "Microsoft Entra ID and RBAC" },
      ],
    },
    gcp: {
      file: "1100_iam.md",
      label: "IAM",
      related: [
        { file: "1110_service_accounts.md", label: "Service accounts" },
        { file: "1200_iam.md", label: "IAM (members, roles, policies)" },
      ],
    },
  },
  {
    n: 7,
    module: "M3 Networking",
    title: "Virtual networks",
    slug: "1200_virtual_networks",
    blurb:
      "A virtual network is your private network space in the cloud—where subnets, routes, and private IPs live.",
    aws: {
      file: "1200_vpc.md",
      label: "VPC",
      related: [{ file: "4000_vpc.md", label: "VPC (overview)" }],
    },
    azure: {
      file: "1200_vnet.md",
      label: "VNet",
      related: [{ file: "4000_vnet.md", label: "Virtual Network (VNet) (overview)" }],
    },
    gcp: {
      file: "1200_vpc.md",
      label: "VPC",
      related: [{ file: "4000_vpc.md", label: "VPC (overview)" }],
    },
  },
  {
    n: 8,
    module: "M3 Networking",
    title: "Subnets & routing",
    slug: "1210_subnets_routing",
    blurb:
      "Subnets divide a virtual network. Routes decide where packets go next—inside the cloud, to the internet, or to on-premises.",
    aws: { file: "1210_subnets_routing.md", label: "Subnets & routing" },
    azure: { file: "1210_subnets_routing.md", label: "Subnets & routing" },
    gcp: { file: "1210_subnets_routes.md", label: "Subnets & routes" },
  },
  {
    n: 9,
    module: "M3 Networking",
    title: "Internet gateway & NAT",
    slug: "1220_internet_gateway_nat",
    blurb:
      "Internet gateways and NAT control how private resources reach (or are reached from) the public internet.",
    aws: { file: "1220_igw_nat.md", label: "IGW / NAT" },
    azure: { file: "1220_nat_gateway.md", label: "NAT Gateway" },
    gcp: { file: "1220_cloud_nat.md", label: "Cloud NAT" },
  },
  {
    n: 10,
    module: "M3 Networking",
    title: "Network security controls",
    slug: "1230_network_security_controls",
    blurb:
      "Security groups, NSGs, NACLs, and firewall rules filter traffic at the instance, subnet, or VPC level.",
    aws: { file: "1230_security_groups_nacls.md", label: "Security groups & NACLs" },
    azure: { file: "1230_nsgs.md", label: "NSGs" },
    gcp: { file: "1230_firewall_rules.md", label: "Firewall rules" },
  },
  {
    n: 11,
    module: "M3 Networking",
    title: "Peering & private service access",
    slug: "1240_peering_private_access",
    blurb:
      "Peering connects networks privately. Endpoints and private access keep traffic to cloud services off the public internet.",
    aws: { file: "1240_peering_endpoints.md", label: "VPC peering / endpoints" },
    azure: { file: "1240_peering_endpoints.md", label: "Peering / endpoints" },
    gcp: { file: "1240_peering_private_access.md", label: "Peering / Private Google Access" },
  },
  {
    n: 12,
    module: "M3 Networking",
    title: "Load balancing",
    slug: "1250_load_balancing",
    blurb:
      "Load balancers distribute traffic across healthy backends for scale, availability, and cleaner public entry points.",
    aws: {
      file: "1250_load_balancing.md",
      label: "ALB / NLB",
      related: [{ file: "4100_load_balancing_dns.md", label: "Load balancing and DNS (ALB / Route 53)" }],
    },
    azure: {
      file: "1250_load_balancer.md",
      label: "Load Balancer",
      related: [
        { file: "1260_application_gateway.md", label: "Application Gateway" },
        { file: "4100_load_balancing_dns.md", label: "Load Balancer, Application Gateway, and DNS" },
      ],
    },
    gcp: {
      file: "1250_load_balancing.md",
      label: "Cloud Load Balancing",
      related: [{ file: "4100_load_balancing_dns.md", label: "Load balancing and Cloud DNS" }],
    },
  },
  {
    n: 13,
    module: "M3 Networking",
    title: "DNS",
    slug: "1260_dns",
    blurb:
      "DNS maps names to addresses and is often the front door for traffic policies, health checks, and failover.",
    aws: {
      file: "1260_route53.md",
      label: "Route 53",
      related: [{ file: "4100_load_balancing_dns.md", label: "Load balancing and DNS (ALB / Route 53)" }],
    },
    azure: {
      file: "1270_azure_dns.md",
      label: "Azure DNS",
      related: [{ file: "4100_load_balancing_dns.md", label: "Load Balancer, Application Gateway, and DNS" }],
    },
    gcp: {
      file: "1260_cloud_dns.md",
      label: "Cloud DNS",
      related: [{ file: "4100_load_balancing_dns.md", label: "Load balancing and Cloud DNS" }],
    },
  },
  {
    n: 14,
    module: "M4 Compute — VMs & autoscaling",
    title: "Virtual machines",
    slug: "1300_virtual_machines",
    blurb:
      "Virtual machines are rented servers in the cloud—images, sizes, and templates define what you run.",
    aws: {
      file: "1300_ec2.md",
      label: "EC2",
      related: [
        { file: "1310_amis_instance_types.md", label: "AMIs & instance types" },
        { file: "1320_launch_templates.md", label: "Launch templates" },
        { file: "2000_ec2.md", label: "EC2 (overview)" },
      ],
    },
    azure: {
      file: "1300_virtual_machines.md",
      label: "Virtual Machines",
      related: [
        { file: "1310_images_sizes.md", label: "Images & sizes" },
        { file: "2000_virtual_machines.md", label: "Virtual Machines (overview)" },
      ],
    },
    gcp: {
      file: "1300_compute_engine.md",
      label: "Compute Engine",
      related: [
        { file: "1310_images_machine_types.md", label: "Images & machine types" },
        { file: "2000_compute_engine.md", label: "Compute Engine (overview)" },
      ],
    },
  },
  {
    n: 15,
    module: "M4 Compute — VMs & autoscaling",
    title: "VM autoscaling",
    slug: "1320_vm_autoscaling",
    blurb:
      "Autoscaling groups add or remove VM capacity using policies, health checks, and sometimes schedules.",
    aws: { file: "1330_auto_scaling_groups.md", label: "Auto Scaling groups" },
    azure: { file: "1320_vmss.md", label: "Virtual Machine Scale Sets" },
    gcp: { file: "1320_managed_instance_groups.md", label: "Managed Instance Groups" },
  },
  {
    n: 16,
    module: "M5 Storage",
    title: "Object storage",
    slug: "1400_object_storage",
    blurb:
      "Object storage holds files and blobs at huge scale—tiers, lifecycle rules, and versioning control cost and durability.",
    aws: {
      file: "1400_s3.md",
      label: "S3",
      related: [{ file: "3000_s3.md", label: "S3 (overview)" }],
    },
    azure: {
      file: "1400_blob_storage.md",
      label: "Blob Storage",
      related: [{ file: "3000_blob_storage.md", label: "Blob Storage (overview)" }],
    },
    gcp: {
      file: "1400_cloud_storage.md",
      label: "Cloud Storage",
      related: [{ file: "3000_cloud_storage.md", label: "Cloud Storage (overview)" }],
    },
  },
  {
    n: 17,
    module: "M5 Storage",
    title: "Block storage",
    slug: "1410_block_storage",
    blurb:
      "Block disks attach to virtual machines like hard drives—good for OS volumes and databases that need raw block I/O.",
    aws: {
      file: "1410_ebs.md",
      label: "EBS",
      related: [{ file: "3100_ebs_efs.md", label: "Block and file storage (EBS / EFS)" }],
    },
    azure: {
      file: "1410_managed_disks.md",
      label: "Managed disks",
      related: [{ file: "3100_disks_files.md", label: "Disks and Azure Files" }],
    },
    gcp: {
      file: "1410_persistent_disk.md",
      label: "Persistent Disk",
      related: [{ file: "3100_disk_filestore.md", label: "Persistent Disk and Filestore" }],
    },
  },
  {
    n: 18,
    module: "M5 Storage",
    title: "File storage",
    slug: "1420_file_storage",
    blurb:
      "Managed file shares give NFS/SMB access to many clients at once—useful for lift-and-shift and shared content.",
    aws: {
      file: "1420_efs.md",
      label: "EFS",
      related: [{ file: "3100_ebs_efs.md", label: "Block and file storage (EBS / EFS)" }],
    },
    azure: {
      file: "1420_azure_files.md",
      label: "Azure Files",
      related: [{ file: "3100_disks_files.md", label: "Disks and Azure Files" }],
    },
    gcp: {
      file: "1420_filestore.md",
      label: "Filestore",
      related: [{ file: "3100_disk_filestore.md", label: "Persistent Disk and Filestore" }],
    },
  },
  {
    n: 19,
    module: "M5 Storage",
    title: "Durability & backup",
    slug: "1430_durability_backup",
    blurb:
      "Durability and backup protect data against loss—replication, snapshots, versioning, and recovery plans.",
    aws: { file: "1430_durability_backup.md", label: "Durability & backup" },
    azure: { file: "1430_durability_backup.md", label: "Durability & backup" },
    gcp: { file: "1430_durability_backup.md", label: "Durability & backup" },
  },
  {
    n: 20,
    module: "M6 Data platforms",
    title: "Managed relational databases",
    slug: "1500_managed_relational_databases",
    blurb:
      "Managed SQL services run engines like PostgreSQL, MySQL, or SQL Server with HA, replicas, and patching handled for you.",
    aws: {
      file: "1500_rds.md",
      label: "RDS",
      related: [{ file: "5000_rds.md", label: "RDS (overview)" }],
    },
    azure: {
      file: "1500_azure_sql.md",
      label: "Azure SQL / Database for PostgreSQL",
      related: [{ file: "5000_sql.md", label: "Azure SQL / Database for PostgreSQL (overview)" }],
    },
    gcp: {
      file: "1500_cloud_sql.md",
      label: "Cloud SQL",
      related: [{ file: "5000_cloud_sql.md", label: "Cloud SQL (overview)" }],
    },
  },
  {
    n: 21,
    module: "M6 Data platforms",
    title: "NoSQL / document & wide-column stores",
    slug: "1510_nosql_stores",
    blurb:
      "NoSQL stores favor flexible models and massive scale—keys, partitions, consistency, and access patterns matter more than joins.",
    aws: {
      file: "1510_dynamodb.md",
      label: "DynamoDB",
      related: [{ file: "5100_dynamodb.md", label: "DynamoDB (overview)" }],
    },
    azure: {
      file: "1510_cosmos_db.md",
      label: "Cosmos DB",
      related: [{ file: "5100_cosmos_db.md", label: "Cosmos DB (overview)" }],
    },
    gcp: {
      file: "1510_firestore_bigtable.md",
      label: "Firestore / Bigtable",
      related: [{ file: "5100_firestore_bigtable.md", label: "Firestore / Bigtable (overview)" }],
    },
  },
  {
    n: 22,
    module: "M7 Serverless functions",
    title: "Serverless functions",
    slug: "1600_serverless_functions",
    blurb:
      "Functions run your code on demand—triggers, packaging, concurrency, cold starts, and identity for the function identity.",
    aws: {
      file: "1600_lambda.md",
      label: "Lambda",
      related: [{ file: "2100_lambda.md", label: "Lambda (overview)" }],
    },
    azure: {
      file: "1600_functions.md",
      label: "Azure Functions",
      related: [{ file: "2100_functions.md", label: "Azure Functions (overview)" }],
    },
    gcp: {
      file: "1600_cloud_functions.md",
      label: "Cloud Functions",
      related: [{ file: "2100_functions_run.md", label: "Cloud Functions / Cloud Run" }],
    },
  },
  {
    n: 23,
    module: "M8 Containers & Kubernetes",
    title: "Container registries",
    slug: "1700_container_registries",
    blurb:
      "A container registry stores and serves your images securely to build and deploy pipelines.",
    aws: { file: "1700_ecr.md", label: "ECR" },
    azure: { file: "1700_acr.md", label: "ACR" },
    gcp: { file: "1700_artifact_registry.md", label: "Artifact Registry" },
  },
  {
    n: 24,
    module: "M8 Containers & Kubernetes",
    title: "Managed containers (non-Kubernetes)",
    slug: "1710_managed_containers",
    blurb:
      "Managed container platforms run images without you operating a full Kubernetes control plane.",
    aws: {
      file: "1710_ecs.md",
      label: "ECS",
      related: [{ file: "2200_containers.md", label: "Containers (ECS / EKS)" }],
    },
    azure: {
      file: "1710_container_apps.md",
      label: "Container Apps",
      related: [{ file: "2200_apps_containers.md", label: "App Service and containers (AKS)" }],
    },
    gcp: {
      file: "1710_cloud_run.md",
      label: "Cloud Run",
      related: [{ file: "2100_functions_run.md", label: "Cloud Functions / Cloud Run" }],
    },
  },
  {
    n: 25,
    module: "M8 Containers & Kubernetes",
    title: "Managed Kubernetes",
    slug: "1720_managed_kubernetes",
    blurb:
      "Managed Kubernetes gives you clusters, node pools, workloads, and cloud networking without running etcd yourself.",
    aws: {
      file: "1720_eks.md",
      label: "EKS",
      related: [{ file: "2200_containers.md", label: "Containers (ECS / EKS)" }],
    },
    azure: {
      file: "1720_aks.md",
      label: "AKS",
      related: [{ file: "2200_apps_containers.md", label: "App Service and containers (AKS)" }],
    },
    gcp: {
      file: "1720_gke.md",
      label: "GKE",
      related: [{ file: "2200_gke.md", label: "GKE (overview)" }],
    },
  },
  {
    n: 26,
    module: "M8 Containers & Kubernetes",
    title: "Cluster autoscaling",
    slug: "1730_cluster_autoscaling",
    blurb:
      "Cluster autoscaling adds or removes nodes so Kubernetes workloads get capacity without manual resizing.",
    aws: { file: "1730_cluster_autoscaling.md", label: "Cluster autoscaling" },
    azure: { file: "1730_cluster_autoscaling.md", label: "Cluster autoscaling" },
    gcp: { file: "1730_cluster_autoscaling.md", label: "Cluster autoscaling" },
  },
  {
    n: 27,
    module: "M9 Message queues",
    title: "Message queues",
    slug: "1800_message_queues",
    blurb:
      "Queues decouple producers and consumers—visibility timeouts, DLQs, and competing consumers keep work reliable.",
    aws: {
      file: "1800_sqs.md",
      label: "SQS",
      related: [{ file: "6000_messaging.md", label: "SQS, SNS, and EventBridge" }],
    },
    azure: {
      file: "1800_storage_queues.md",
      label: "Storage Queues",
      related: [
        { file: "1810_service_bus_queues.md", label: "Service Bus Queues" },
        { file: "6000_messaging.md", label: "Service Bus, Event Grid, and Event Hubs" },
      ],
    },
    gcp: {
      file: "1800_pubsub_pull.md",
      label: "Pub/Sub pull subscriptions",
      related: [
        { file: "1810_cloud_tasks.md", label: "Cloud Tasks" },
        { file: "6000_pubsub.md", label: "Pub/Sub" },
      ],
    },
  },
  {
    n: 28,
    module: "M10 Message brokers & events",
    title: "Pub/sub topics & fan-out",
    slug: "1810_pubsub_fanout",
    blurb:
      "Topics fan one message out to many subscribers—useful for notifications and event-driven designs.",
    aws: {
      file: "1810_sns.md",
      label: "SNS",
      related: [{ file: "6000_messaging.md", label: "SQS, SNS, and EventBridge" }],
    },
    azure: {
      file: "1820_service_bus_topics.md",
      label: "Service Bus Topics",
      related: [{ file: "6000_messaging.md", label: "Service Bus, Event Grid, and Event Hubs" }],
    },
    gcp: {
      file: "1820_pubsub_topics.md",
      label: "Pub/Sub topics/push",
      related: [{ file: "6000_pubsub.md", label: "Pub/Sub" }],
    },
  },
  {
    n: 29,
    module: "M10 Message brokers & events",
    title: "Managed message brokers (ActiveMQ / RabbitMQ / Kafka)",
    slug: "1820_managed_brokers",
    blurb:
      "Managed brokers host classic messaging (ActiveMQ/RabbitMQ) or streaming (Kafka) without you running the cluster day to day.",
    aws: {
      file: "1820_amazon_mq.md",
      label: "Amazon MQ",
      related: [{ file: "1830_msk.md", label: "MSK" }],
    },
    azure: { file: "1830_event_hubs.md", label: "Event Hubs" },
    gcp: { file: "1830_managed_kafka.md", label: "Managed Service for Apache Kafka" },
  },
  {
    n: 30,
    module: "M10 Message brokers & events",
    title: "Event buses / event routing",
    slug: "1840_event_buses",
    blurb:
      "Event buses and routers deliver events from many sources to many targets with filtering and rules.",
    aws: {
      file: "1840_eventbridge.md",
      label: "EventBridge",
      related: [{ file: "6000_messaging.md", label: "SQS, SNS, and EventBridge" }],
    },
    azure: {
      file: "1840_event_grid.md",
      label: "Event Grid",
      related: [{ file: "6000_messaging.md", label: "Service Bus, Event Grid, and Event Hubs" }],
    },
    gcp: { file: "1840_eventarc.md", label: "Eventarc" },
  },
  {
    n: 31,
    module: "M11 Scalable background jobs",
    title: "Queue workers & background processing",
    slug: "1900_queue_workers",
    blurb:
      "Workers pull from queues (or get triggered by them) to process jobs at scale on VMs, containers, or functions.",
    aws: { file: "1900_queue_workers.md", label: "Queue workers" },
    azure: { file: "1900_queue_workers.md", label: "Queue-triggered Functions / WebJobs" },
    gcp: { file: "1900_queue_workers.md", label: "Pub/Sub / Cloud Tasks workers" },
  },
  {
    n: 32,
    module: "M11 Scalable background jobs",
    title: "Batch compute",
    slug: "1910_batch_compute",
    blurb:
      "Batch services schedule large or parallel jobs across compute pools and scale them down when work is done.",
    aws: { file: "1910_aws_batch.md", label: "AWS Batch" },
    azure: { file: "1910_azure_batch.md", label: "Azure Batch" },
    gcp: { file: "1910_cloud_batch.md", label: "Cloud Batch" },
  },
  {
    n: 33,
    module: "M11 Scalable background jobs",
    title: "Workflows & durable orchestration",
    slug: "1920_workflows_orchestration",
    blurb:
      "Orchestrators coordinate multi-step work—retries, waits, branching, and long-running durable flows.",
    aws: { file: "1920_step_functions.md", label: "Step Functions" },
    azure: {
      file: "1920_durable_functions.md",
      label: "Durable Functions",
      related: [{ file: "1930_container_apps_jobs.md", label: "Container Apps jobs" }],
    },
    gcp: {
      file: "1920_cloud_run_jobs.md",
      label: "Cloud Run jobs",
      related: [{ file: "1930_workflows.md", label: "Workflows" }],
    },
  },
  {
    n: 34,
    module: "M11 Scalable background jobs",
    title: "Scheduled / cron jobs",
    slug: "1930_scheduled_jobs",
    blurb:
      "Schedulers run jobs on a timetable—nightly reports, cleanups, and periodic syncs.",
    aws: { file: "1930_scheduled_jobs.md", label: "Scheduled / cron jobs" },
    azure: { file: "1940_scheduled_jobs.md", label: "Scheduled / cron jobs" },
    gcp: { file: "1940_scheduled_jobs.md", label: "Scheduled / cron jobs" },
  },
  {
    n: 35,
    module: "M12 API management",
    title: "API management",
    slug: "2000_api_management",
    blurb:
      "API gateways and management planes expose backends with auth, throttling, versions, and developer-facing products.",
    aws: { file: "2000_api_gateway.md", label: "API Gateway" },
    azure: { file: "2000_api_management.md", label: "Azure API Management" },
    gcp: { file: "2000_api_gateway_apigee.md", label: "API Gateway / Apigee" },
  },
  {
    n: 36,
    module: "M13 Observability",
    title: "Metrics, logs & alerts",
    slug: "2100_metrics_logs_alerts",
    blurb:
      "Metrics, logs, and alerts tell you what is healthy, what broke, and when to wake someone up.",
    aws: {
      file: "2100_cloudwatch.md",
      label: "CloudWatch",
      related: [{ file: "7000_cloudwatch.md", label: "CloudWatch (overview)" }],
    },
    azure: {
      file: "2100_monitor.md",
      label: "Azure Monitor",
      related: [{ file: "7000_monitor.md", label: "Azure Monitor (overview)" }],
    },
    gcp: {
      file: "2100_monitoring_logging.md",
      label: "Cloud Monitoring & Logging",
      related: [{ file: "7000_ops.md", label: "Cloud Monitoring / Logging" }],
    },
  },
  {
    n: 37,
    module: "M13 Observability",
    title: "Application performance / tracing",
    slug: "2110_apm_tracing",
    blurb:
      "Tracing and APM follow a request across services so you can find latency and failures in distributed systems.",
    aws: { file: "2110_xray.md", label: "X-Ray" },
    azure: { file: "2110_application_insights.md", label: "Application Insights" },
    gcp: { file: "2110_cloud_trace.md", label: "Cloud Trace" },
  },
  {
    n: 38,
    module: "M14 Ops & IaC",
    title: "Infrastructure as code",
    slug: "2200_infrastructure_as_code",
    blurb:
      "Infrastructure as code describes cloud resources in files you can review, version, and apply repeatedly.",
    aws: {
      file: "2200_cloudformation_cdk.md",
      label: "CloudFormation & CDK",
      related: [{ file: "7100_iac.md", label: "Infrastructure as Code (CloudFormation / CDK)" }],
    },
    azure: {
      file: "2200_bicep_arm_terraform.md",
      label: "Bicep / ARM / Terraform",
      related: [{ file: "7100_iac.md", label: "Infrastructure as Code (Bicep / ARM / Terraform)" }],
    },
    gcp: {
      file: "2200_terraform_deployment_manager.md",
      label: "Terraform / Deployment Manager",
      related: [{ file: "7100_iac.md", label: "Infrastructure as Code (Terraform / Deployment Manager)" }],
    },
  },
  {
    n: 39,
    module: "M14 Ops & IaC",
    title: "Cost & billing awareness",
    slug: "2210_cost_billing",
    blurb:
      "Cost awareness means knowing what you pay for, setting budgets and alerts, and choosing sizes and pricing models deliberately.",
    aws: { file: "2210_cost_billing.md", label: "Cost & billing" },
    azure: { file: "2210_cost_billing.md", label: "Cost & billing" },
    gcp: { file: "2210_cost_billing.md", label: "Cost & billing" },
  },
];

function providerTag(providerKey) {
  if (providerKey === "aws" || providerKey === "AWS") return "AWS";
  if (providerKey === "azure" || providerKey === "Azure") return "Azure";
  return "GCP";
}

function syllabusId(n, sub, providerKey) {
  return `${n}.${sub} ${providerTag(providerKey)}`;
}

/** Short technology word(s) from a page/topic title. */
function techShort(label) {
  let s = String(label)
    .replace(/\s*\([^)]*\)/g, "")
    .replace(/^What is the\s+/i, "")
    .replace(/^What is\s+/i, "")
    .replace(/\s*[–—].*$/, "")
    .replace(/\?+$/g, "")
    .trim();

  const slashParts = s
    .split(/\s*\/\s*/)
    .map((p) => p.trim())
    .filter(Boolean);
  if (slashParts.length > 1) {
    const first = slashParts[0];
    const last = slashParts[slashParts.length - 1];
    // Prefer a multi-word / longer product name on the left; else the right side
    s = first.split(/\s+/).length >= 2 || first.length >= 6 ? first : last;
  }

  s = s.split(/\s*&\s*/)[0].split(/,/)[0].trim();
  const words = s.split(/\s+/).filter(Boolean);
  if (words.length <= 2) return capTech(words.join(" "));
  if (/^(microsoft|amazon|google|azure|cloud|managed)$/i.test(words[0]) && words.length >= 3) {
    return capTech(words.slice(0, 3).join(" "));
  }
  return capTech(words.slice(0, 2).join(" "));
}

function capTech(s) {
  if (!s) return s;
  return s.replace(/\b[a-z]/g, (ch) => ch.toUpperCase());
}

/** Short nav label: "2.1 AWS · Accounts" */
function navProvider(n, sub, providerKey, label) {
  const provider = providerTag(providerKey);
  let tech = techShort(label);
  if (
    new RegExp(`^${provider}$`, "i").test(tech) ||
    (provider === "GCP" && /^google cloud$/i.test(tech))
  ) {
    tech = "Intro";
  }
  return `${syllabusId(n, sub, providerKey)} · ${tech}`;
}

/** Short nav label: "Topic 2 · Accounts" */
function navTopic(n, title) {
  return `Topic ${n} · ${techShort(title)}`;
}

function navHtml({ prevHref, prevLabel, nextHref, nextLabel, topicHref, topicLabel, homeDepth }) {
  const home = "../".repeat(homeDepth) + "README.md";
  const cloud = "../".repeat(homeDepth - 1) + "README.md";
  return `
<br/>
<p>
    <span style="float: left;">
        <a href="${prevHref}">Previous: ${prevLabel}</a>
        &nbsp;
        <a href="${nextHref}">Next: ${nextLabel}</a>
    </span>
    <span style="float: right;">
        <a href="${home}">Home</a>
        &nbsp;|&nbsp;
        <a href="${cloud}">Cloud</a>
        &nbsp;|&nbsp;
        <a href="${topicHref}">Topic: ${topicLabel}</a>
    </span>
</p>
`;
}

function relatedList(provider, items, basePrefix) {
  if (!items?.length) return "";
  const links = items
    .map((r) => `- [${r.label}](${basePrefix}${r.file})`)
    .join("\n");
  return `\n### Related ${provider} pages\n\n${links}\n`;
}

function stripOldFooter(text) {
  return text
    .replace(/\n<br\/>\s*<p>[\s\S]*<\/p>\s*$/m, "")
    .replace(/\n---\s*\n\s*<p align="right">[\s\S]*<\/p>\s*$/m, "")
    .replace(/\n<p align="right">[\s\S]*<\/p>\s*$/m, "")
    .trimEnd();
}

function ensureProviderBody(existing, { n, sub, provider, label, topicTitle, topicRel }) {
  const heading = `${syllabusId(n, sub, provider)} — ${label}`;
  const cleaned = existing ? stripOldFooter(existing) : "";
  if (cleaned && !/> Placeholder — content coming soon\./.test(cleaned) && cleaned.split("\n").length > 12) {
    // Keep richer existing content; ensure H1 matches syllabus label
    let body = cleaned.replace(/^#\s+.+$/m, `# ${heading}`);
    if (!body.includes(topicRel)) {
      body = body.replace(
        /^(# .+)\n/,
        `$1\n\nThis page is the ${provider} view of the shared concept **[${topicTitle}](${topicRel})**.\n`
      );
    }
    return body.trimEnd() + "\n";
  }

  return `# ${heading}

This page is the ${provider} view of the shared concept **[${topicTitle}](${topicRel})**.

## On this page

- [In plain words](#in-plain-words)
- [Where this sits in the syllabus](#where-this-sits-in-the-syllabus)

## In plain words

**${label}** is how ${provider} names this idea. The shared concept is the same across clouds; the console, APIs, and product limits differ.

> Detailed walkthrough coming soon. Use this page as the syllabus anchor for ${provider} under topic ${n}.

## Where this sits in the syllabus

Compare this page with the AWS, Azure, and GCP siblings for topic **${n}**, then continue to the next topic in the [Cloud syllabus](${provider === "AWS" || provider === "Azure" || provider === "GCP" ? "../../README.md" : "../README.md"}).
`;
}

function buildConceptPage(topic, prev, next) {
  const topicLabel = `${topic.n}. ${topic.title}`;
  const awsHref = `../aws/docs/${topic.aws.file}`;
  const azureHref = `../azure/docs/${topic.azure.file}`;
  const gcpHref = `../gcp/docs/${topic.gcp.file}`;

  let prevHref = "../README.md";
  let prevLabel = "Cloud";
  if (prev) {
    prevHref = `../gcp/docs/${prev.gcp.file}`;
    prevLabel = navProvider(prev.n, "3", "GCP", prev.gcp.label);
  }

  let nextHref = awsHref;
  let nextLabel = navProvider(topic.n, "1", "AWS", topic.aws.label);
  // first page of chain after concept is always this topic's AWS page

  const related = [
    relatedList("AWS", topic.aws.related, "../aws/docs/"),
    relatedList("Azure", topic.azure.related, "../azure/docs/"),
    relatedList("GCP", topic.gcp.related, "../gcp/docs/"),
  ]
    .filter(Boolean)
    .join("\n");

  return `# ${topicLabel}

${topic.blurb}

**Module:** ${topic.module}

## Provider pages for this topic

${syllabusId(topic.n, "1", "AWS")} — [${topic.aws.label}](${awsHref})  
${syllabusId(topic.n, "2", "Azure")} — [${topic.azure.label}](${azureHref})  
${syllabusId(topic.n, "3", "GCP")} — [${topic.gcp.label}](${gcpHref})
${related}
${navHtml({
  prevHref,
  prevLabel,
  nextHref,
  nextLabel,
  topicHref: `./${topic.slug}.md`,
  topicLabel: topic.title,
  homeDepth: 2,
})}
`;
}

function writeProviderPage(topic, providerKey, sub, prev, next) {
  const entry = topic[providerKey];
  const providerName = providerKey === "aws" ? "AWS" : providerKey === "azure" ? "Azure" : "GCP";
  const dir = path.join(CLOUD, providerKey, "docs");
  const filePath = path.join(dir, entry.file);
  const topicRel = `../../docs/${topic.slug}.md`;
  const existing = fs.existsSync(filePath) ? fs.readFileSync(filePath, "utf8") : "";

  // Skip full rewrite of topic 1 pages that already have good hand-written content
  if (topic.n === 1 && existing && existing.includes("Topic: What is the cloud")) {
    // Still refresh nav to match chain
  }

  let body = ensureProviderBody(existing, {
    n: topic.n,
    sub,
    provider: providerName,
    label: entry.label,
    topicTitle: topic.title,
    topicRel,
  });
  body = stripOldFooter(body);

  let prevHref;
  let prevLabel;
  let nextHref;
  let nextLabel;

  if (sub === "1") {
    prevHref = topicRel;
    prevLabel = navTopic(topic.n, topic.title);
    nextHref = `../../azure/docs/${topic.azure.file}`;
    nextLabel = navProvider(topic.n, "2", "Azure", topic.azure.label);
  } else if (sub === "2") {
    prevHref = `../../aws/docs/${topic.aws.file}`;
    prevLabel = navProvider(topic.n, "1", "AWS", topic.aws.label);
    nextHref = `../../gcp/docs/${topic.gcp.file}`;
    nextLabel = navProvider(topic.n, "3", "GCP", topic.gcp.label);
  } else {
    prevHref = `../../azure/docs/${topic.azure.file}`;
    prevLabel = navProvider(topic.n, "2", "Azure", topic.azure.label);
    if (next) {
      nextHref = `../../docs/${next.slug}.md`;
      nextLabel = navTopic(next.n, next.title);
    } else {
      nextHref = "../../README.md";
      nextLabel = "Cloud";
    }
  }

  // For concept prev from GCP of previous topic — handled on concept page
  void prev;

  const related =
    entry.related?.length
      ? `\n## Related pages\n\n${entry.related.map((r) => `- [${r.label}](./${r.file})`).join("\n")}\n`
      : "";

  if (!body.includes("## Related pages") && related) {
    body = body.trimEnd() + "\n" + related;
  }

  const out =
    body.trimEnd() +
    "\n" +
    navHtml({
      prevHref,
      prevLabel,
      nextHref,
      nextLabel,
      topicHref: topicRel,
      topicLabel: topic.title,
      homeDepth: 3,
    });

  fs.writeFileSync(filePath, out, "utf8");
}

function buildReadme() {
  const intro = `# ☁️ Cloud Tutorials Index

**Cloud computing** lets you rent compute, storage, networking, and managed services over the internet instead of buying and running your own data centers. You pay for what you use, scale up or down as demand changes, and focus on applications while the provider runs the underlying infrastructure.

The three major public clouds we cover are **AWS** (Amazon Web Services), **Azure** (Microsoft), and **GCP** (Google Cloud Platform). Each offers the same broad building blocks — identity, virtual networks, VMs, serverless, containers, storage, databases, messaging, APIs, and monitoring — under different product names and console experiences.

In these tutorials we **study each platform side by side** and **compare equivalent services**, so the same syllabus (foundations → networking → compute → data → messaging → ops) maps cleanly across AWS, Azure, and GCP. Each provider has its own tree (\`docs\`, \`code\`, \`static\`, \`tools\`), same layout as Design Patterns.

---

Provider trees: [AWS](./aws/README.md) ([docs index](./aws/docs/index.md)) · [Azure](./azure/README.md) ([docs index](./azure/docs/index.md)) · [GCP](./gcp/README.md) ([docs index](./gcp/docs/index.md))

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
`;

  let body = "";
  let currentModule = null;
  for (const t of TOPICS) {
    if (t.module !== currentModule) {
      if (currentModule !== null) body += "\n---\n\n";
      currentModule = t.module;
      const anchor = t.module.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+$/g, "");
      body += `## ${t.module}\n\n`;
      void anchor;
    }
    body += `### ${t.n}. [${t.title}](./docs/${t.slug}.md)\n\n`;
    body += `${syllabusId(t.n, "1", "AWS")} — [${t.aws.label}](./aws/docs/${t.aws.file})  \n`;
    body += `${syllabusId(t.n, "2", "Azure")} — [${t.azure.label}](./azure/docs/${t.azure.file})  \n`;
    body += `${syllabusId(t.n, "3", "GCP")} — [${t.gcp.label}](./gcp/docs/${t.gcp.file})\n\n`;
  }

  const outro = `---

<p align="right">
    <a href="../README.md">Home</a>
</p>
`;
  return intro + body + outro;
}

fs.mkdirSync(DOCS, { recursive: true });

for (let i = 0; i < TOPICS.length; i++) {
  const topic = TOPICS[i];
  const prev = i > 0 ? TOPICS[i - 1] : null;
  const next = i < TOPICS.length - 1 ? TOPICS[i + 1] : null;

  const conceptPath = path.join(DOCS, `${topic.slug}.md`);
  // Keep hand-written topic 1 concept body if present and richer
  if (topic.n === 1 && fs.existsSync(conceptPath)) {
    const existing = fs.readFileSync(conceptPath, "utf8");
    if (existing.length > 800 && existing.includes("## What the cloud model means")) {
      let refreshed = stripOldFooter(existing);
      refreshed = refreshed.replace(
        /## Provider pages for this topic\n\n[\s\S]*?(?=\n## |\n$)/,
        `## Provider pages for this topic

${syllabusId(1, "1", "AWS")} — [What is AWS?](../aws/docs/1000_what_is_aws.md)  
${syllabusId(1, "2", "Azure")} — [What is Azure?](../azure/docs/1000_what_is_azure.md)  
${syllabusId(1, "3", "GCP")} — [What is Google Cloud?](../gcp/docs/1000_what_is_gcp.md)

`
      );
      refreshed =
        refreshed.trimEnd() +
        "\n" +
        navHtml({
          prevHref: "../README.md",
          prevLabel: "Cloud",
          nextHref: "../aws/docs/1000_what_is_aws.md",
          nextLabel: navProvider(1, "1", "AWS", topic.aws.label),
          topicHref: "./1000_what_is_the_cloud.md",
          topicLabel: topic.title,
          homeDepth: 2,
        });
      fs.writeFileSync(conceptPath, refreshed, "utf8");
    } else {
      fs.writeFileSync(conceptPath, buildConceptPage(topic, prev, next), "utf8");
    }
  } else {
    fs.writeFileSync(conceptPath, buildConceptPage(topic, prev, next), "utf8");
  }

  // For topic 1 provider pages: refresh nav only if already hand-written
  for (const [key, sub] of [
    ["aws", "1"],
    ["azure", "2"],
    ["gcp", "3"],
  ]) {
    if (topic.n === 1) {
      const filePath = path.join(CLOUD, key, "docs", topic[key].file);
      let existing = fs.readFileSync(filePath, "utf8");
      existing = stripOldFooter(existing);
      const provider = providerTag(key);
      const heading = `${syllabusId(1, sub, provider)} — ${topic[key].label}`;
      existing = existing.replace(/^#\s+.+$/m, `# ${heading}`);
      let prevHref;
      let prevLabel;
      let nextHref;
      let nextLabel;
      if (sub === "1") {
        prevHref = "../../docs/1000_what_is_the_cloud.md";
        prevLabel = navTopic(1, topic.title);
        nextHref = "../../azure/docs/1000_what_is_azure.md";
        nextLabel = navProvider(1, "2", "Azure", topic.azure.label);
      } else if (sub === "2") {
        prevHref = "../../aws/docs/1000_what_is_aws.md";
        prevLabel = navProvider(1, "1", "AWS", topic.aws.label);
        nextHref = "../../gcp/docs/1000_what_is_gcp.md";
        nextLabel = navProvider(1, "3", "GCP", topic.gcp.label);
      } else {
        prevHref = "../../azure/docs/1000_what_is_azure.md";
        prevLabel = navProvider(1, "2", "Azure", topic.azure.label);
        nextHref = "../../docs/1010_accounts_subscriptions_projects.md";
        nextLabel = navTopic(2, TOPICS[1].title);
      }
      fs.writeFileSync(
        filePath,
        existing.trimEnd() +
          "\n" +
          navHtml({
            prevHref,
            prevLabel,
            nextHref,
            nextLabel,
            topicHref: "../../docs/1000_what_is_the_cloud.md",
            topicLabel: topic.title,
            homeDepth: 3,
          }),
        "utf8"
      );
    } else {
      writeProviderPage(topic, key, sub, prev, next);
    }
  }
}

fs.writeFileSync(path.join(CLOUD, "README.md"), buildReadme(), "utf8");
console.log(`Generated ${TOPICS.length} concept pages and updated provider nav + README.`);
