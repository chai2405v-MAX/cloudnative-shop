terraform {
  backend "s3" {
    bucket       = "cloudnative-shop-tfstate-teja-lab0001"
    key          = "cloudnative-shop/terraform.tfstate"
    region       = "ap-south-1"
    profile      = "cloudnative-shop"
    encrypt      = true
    use_lockfile = true
  }
}
