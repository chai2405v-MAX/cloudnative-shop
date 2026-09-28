output "vpc_id" {
  description = "ID of the CloudNative-Shop VPC"
  value       = aws_vpc.main.id
}
output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value = [
    aws_subnet.public_a.id,
    aws_subnet.public_b.id
  ]
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value = [
    aws_subnet.private_a.id,
    aws_subnet.private_b.id
  ]
}
output "available_azs" {
  description = "Available Availability Zones in the selected AWS region"
  value       = data.aws_availability_zones.available.names
}