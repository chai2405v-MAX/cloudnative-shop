resource "aws_eip" "nat" {
  domain = "vpc"

  tags = {
    Name = "cloudnative-shop-nat-eip"
  }
}

resource "aws_nat_gateway" "main" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public_a.id

  tags = {
    Name = "cloudnative-shop-nat"
  }

  depends_on = [aws_internet_gateway.main]
}