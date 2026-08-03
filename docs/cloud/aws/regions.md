# Global Region

Based on below things you can choose region
1. Compliance : GDPR, EU 
2. Proximity :  low latency , enhances application responsiveness
3. Features : not all Regions contain all AWS offerings
4. Pricing : Some Regions have lower operational costs than others.


For backups you can deploy cloud resources in multiple regions or multiple Avaiablity Zones.

### Edge locations
Edge locations are strategically placed sites around the world that cache content to deliver data, video, and applications with lower latency and higher transfer speeds. Edge locations are considered a vital part of the AWS content delivery network (CDN) and use services like CloudFront to efficiently distribute data to end users.

### AWS Regions
Regions are geographical areas around the world that are made up of multiple data centers. These data centers provide scalable and redundant infrastructure for hosting cloud services. Each Region consists of multiple, isolated locations known as Availability Zones. Each Region has three or more Availability Zones.

### AWS Availability Zones
Availability Zones are distinct locations within a Region, each designed as an independent zone with its own power, networking, and connectivity. Availability Zones maintain high availability and fault tolerance for applications. Each Availability Zones consists of one or more data centers.

> AWS Regions are physical locations around the world where AWS has multiple Availability Zones. Edge locations are located outside of AWS Regions and cache frequently accessed content.
### Iac (infrastructure as code) or AWS CloudFormation
you want to put same resources on region B as on region A for high availablity
- Manuually you can do but there may be errors
- Automate using file

You can use IaC to define your infrastructure in a file, almost like a blueprint for your AWS architecture.

AWS CloudFormation is an IaC service that you can use to define a wide variety of AWS resources in a declarative way by creating text-based documents called CloudFormation templates. CloudFormation parses the template and then provisions all of the resources you defined, calling the needed AWS APIs in the background to make it all happen. 

So now, instead of manually setting up resources in Region B to match Region A, you can create a CloudFormation template that defines everything your infrastructure needs. With a single command, AWS provisions those resources exactly as defined. 




