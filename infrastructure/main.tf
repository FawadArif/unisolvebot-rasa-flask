terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "unisolvebot" {
  name                 = "unisolvebot"
  image_tag_mutability = "MUTABLE"
}       