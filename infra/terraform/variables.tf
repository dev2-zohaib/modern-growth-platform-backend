variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "modern-growth-platform"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.10.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "Public subnet CIDRs"
  type        = list(string)
  default     = ["10.10.1.0/24", "10.10.2.0/24"]
}

variable "container_image" {
  description = "Container image for ECS task"
  type        = string
  default     = "nginx:latest"
}

variable "container_port" {
  description = "Application container port"
  type        = number
  default     = 8000
}

variable "desired_count" {
  description = "Desired ECS task count"
  type        = number
  default     = 1
}

variable "domain_name" {
  description = "Optional Route53 domain name placeholder"
  type        = string
  default     = ""
}

variable "create_dns_placeholders" {
  description = "Whether to create Route53/ACM placeholder resources"
  type        = bool
  default     = false
}
