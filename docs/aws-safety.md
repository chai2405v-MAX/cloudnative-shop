# CloudNative-Shop AWS Safety Rules

## AWS Identity

- Always use the `cloudnative-shop` AWS CLI profile.
- Verify identity before infrastructure changes:
  `aws sts get-caller-identity --profile cloudnative-shop`
- Never use the root user for normal DevOps work.
- Human administrator accounts must use MFA.

## AWS Region

- Primary project region: `ap-south-1`.
- Verify the region before creating infrastructure.
- Avoid creating duplicate resources in other regions.

## Cost Safety

- Monthly AWS budget: $25.
- Check AWS Billing regularly during infrastructure labs.
- Estimate cost before creating EKS, EC2, NAT Gateway, ALB, or other chargeable resources.
- Destroy temporary lab infrastructure when the exercise is complete.
- Never assume an AWS Budget automatically stops resources.

## Credentials

- Do not commit AWS credentials, access keys, secret keys, or session tokens to Git.
- Prefer temporary AWS CLI authentication using `aws login`.
- Do not reuse human credentials for applications, Jenkins, or Kubernetes workloads.

## Cleanup Rule

Before ending an AWS infrastructure lab:

1. Check what resources were created.
2. Destroy resources that are no longer required.
3. Verify deletion in AWS.
4. Check for leftover load balancers, NAT Gateways, EC2 instances, EBS volumes, and Elastic IPs.
