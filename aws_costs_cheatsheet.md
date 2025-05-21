# AWS Costs Cheatsheet

USD per year.
Per year is **so much more understandable** than per hour.

# Compute and DB per year
On demand prices for typical region (eg. us-west-2), discounts of about 50% are obtainable with Reserved Instances, (Compute) Savings Plans and Spot Instances.

<table>
<tr><td><b> EC2 </b></td><td>m7g.medium (2 CPU, 4GB)</td><td><b> $360 </b></td><td></td></tr>
<tr><td><b> Lambda </b></td><td>per CPU GB year.  ARM</td><td><b> $420 </b></td><td>+ $6 per request per second</td></tr>
<tr><td><b> Fargate </b></td><td>ARM 2 CPUs 4GB</td><td><b> $690 </b></td><td></td></tr>
<tr><td><b> ECS </b></td><td></td><td><b>  </b></td><td>as EC2 or Fargate</td></tr>
<tr><td rowspan="3"><b> EKS <!--- rowspan="3" ---> </b></td><td>control plane</td><td><b> $900 </b></td><td>first 14 months after version release</td></tr>
<tr><td>control plane</td><td><b> $5300 </b></td><td>after 14 months EC2 surcharge</td></tr>
<tr><td>auto mode</td><td><b> </b></td><td>+ 20% EC2 surcharge</td></tr>
<tr><td><b> ELB </b></td><td>ALB, NLB, Classic</td><td><b> $200 </b></td><td>+ $70 x load units eg. data transfer 1 GB per hour.</td></tr>
<tr><td><b> RDS </b></td><td>db.t4g.medium (1 CPU 4GB)</td><td><b> $570 </b></td><td>Single AZ. MySQL, PostgreSQL, MariaDB</td></tr>
<tr><td><b> OpenSearch </b></td><td>m7g.medium.search (1 CPU 4GB)</td><td><b> $600 </b></td><td></td></tr>
</table>

### relative sizes:
<table>
<tr><td>nano</td><td>micro</td><td>small</td><td>medium</td><td>large</td><td>xlarge</td><td>2xlarge</td></tr>
<tr><td>1/8</td><td>1/4</td><td>1/2</td><td>1</td><td>2</td><td>4</td><td>8</td></tr>
</table>

# Storage per TB year
<table>
<tr><td><b> EBS </b></td><td>gp3</td><td><b> $1000 </b></td><td>HDD 1/2 price</td></tr>
<tr><td rowspan="2"><b> snapshot <!--- rowspan="2" ---></b></td><td>standard</td><td><b> $600</b></td><td>retrieval free</td></tr>
<tr><td>archive</td><td><b>  $150 </b></td><td>retrieval $370</td></tr>
<tr><td rowspan="2"><b> S3 <!--- rowspan="2" ---></b></td><td>standard</td><td><b> $280  </b></td><td>infrequent 1/2 price.  Std Glacier 1/6th price</td></tr>
<tr><td>glacier deep archive</td><td><b> $12 </b></td><td>12 hour retrieval</td></tr>
<tr><td rowspan="2"><b> EFS <!--- rowspan="2" ---> </b></td><td>standard</td><td><b> $3700  </b></td><td>$370 per TB read, $740 write.  $70 transfer read or write</td></tr>
<tr><td>infrequent</td><td><b>  $200 </b></td><td>$70 read or write</td></tr>
</table>

# Network per TB or year
<table>
<tr><td rowspan="2"><b> EC2 <!--- rowspan="2" ---></b></td><td>to internet</td><td><b> $90 </b></td><td>first 100GB free</td></tr>
<tr><td>to another AWS region</td><td><b> $20 </b></td><td>first 100GB free</td></tr>
<tr><td><b> CloudFront </b></td><td>US/Europe</td><td><b> $90 </b></td><td>first 1TB free</td></tr>
<tr><td rowspan="2"><b> NAT gateway <!--- rowspan="2" ---></b></td><td>per year</td><td><b> $40 </b></td><td></td></tr>
<tr><td>per TB</td><td><b> $45 </b></td><td></td></tr>
<tr><td><b> public IP </b></td><td></td><td><b> $45 </b></td><td>idle or in use</td></tr>
<tr><td><b> elastic IP </b></td><td></td><td><b> $45 </b></td><td>idle or additional</td></tr>
<tr><td><b> WAF  </b></td><td>Web ACL per rule per year</td><td><b> $72 </b></td><td>+ $18 per request per second</td></tr>
</table>


### Free networking:
* Within the same AZ.
* to EC2 from internet.
* EC2 to CloudFront, S3.
* Public IPv4 addresses that are not dedicated to your resource for example, public IPv4 addresses associated with Amazon S3 that are not dedicated per S3 bucket.
* AWS Elastic IP addresses associated with a running instance
* to CloudWatch.
* Internet Gateway to public endpoint in the same Region. (not NAT).
* between DynamoDB and other AWS services within the same AWS Region
