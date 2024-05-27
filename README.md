# Yahoo Finances Data
A data engineering training project to build an end-to-end pipline for a real-time processing of data

<h1 align="center">Yahoo Finances Data Engineering Project</h1>

<p align="center">
  <a href="#technologies">Technologies</a> •
  <a href="#about-the-project">About the project</a> •
  <a href="#conceptual-architecture">Conceptual architecture</a> •
  <a href="#conceptual-report-on-the-technologies-used">Conceptual Report on the Technologies used</a> •
  <a href="#data-source">Data source</a> •
  <a href="#🛠️-setup">Setup</a> 
</p>

---

## Technologies
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
 ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
 ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
 ![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)
 ![Amazon S3](https://a11ybadges.com/badge?logo=amazons3)

 ---

## About the project

A data engineering training project to build an end-to-end pipline for a real-time processing of data. The project is designed to fetch data from yahoo finances official 
website. 
Data is fetched daily which is transformed using pandas and passed through an ETL process for further analysis.

In addition, process data can then be used for visual analytics.

---

## Conceptual architecture
![image](https://github.com/TechWithNate/Yahoo-finances-data-event/assets/81887567/f8dd1f32-5ed4-4513-8ed9-79895f80ba7c)


---

## Conceptual Report on the Technologies used
### Pros and Cons of AWS Redshift
AWS Redshift is a fully managed data warehouse service designed to handle large-scale data analytics. It is commonly used in data pipelines for processing and analyzing large volumes of data. Below are the pros and cons of using AWS Redshift in a data pipeline:

| Pros | Cons |
| --- | --- |
|Redshift can handle petabyte-scale data warehouses. It allows you to start small and scale out by adding more nodes as your data grows.  | While Redshift can be cost-effective, it can become expensive for very large data volumes or high-frequency queries, especially if concurrency scaling is frequently used.|
| Redshift uses columnar storage and data compression to improve query performance. Its massively parallel processing (MPP) architecture distributes queries across multiple nodes, enhancing performance for complex queries | Redshift is optimized for batch processing rather than real-time analytics. It may not be the best choice for applications requiring real-time data processing and low-latency queries |
|Redshift integrates seamlessly with other AWS services like S3, Kinesis, Glue, and Data Pipeline. This makes it easier to build comprehensive data pipelines within the AWS ecosystem| Managing and optimizing Redshift can be complex, requiring a good understanding of its architecture, query performance tuning, and best practices for data distribution and sorting keys | Redshift can automatically add more compute capacity to handle high demand for concurrent queries, ensuring consistent performance | If using Redshift Spectrum (which allows querying data directly from S3), queries on infrequently accessed data can have higher latency due to `cold starts` |

**Conclusion**

AWS Redshift is a powerful data warehousing solution that excels in handling large-scale data analytics with high performance and integration capabilities within the AWS ecosystem. However, due to the requirements of this project, AWS Redshift was suitable for use.

---
### Pros and Cons of using AWS RDS
Amazon RDS (Relational Database Service) is a managed relational database service that supports multiple database engines such as MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB. It is often used in data pipelines for transactional data processing, operational databases, and as a component in ETL processes. Below are the pros and cons of using Amazon RDS in a data pipeline:

| Pros | Cons |
| --- | --- |
| RDS handles routine database tasks such as provisioning, patching, backup, recovery, and failure detection. This reduces the operational burden on your team| Managed services like RDS can be more expensive than self-managed databases, especially for large-scale deployments or when using high-end instance types. Costs can also escalate with additional features like Multi-AZ, read replicas, and high storage IOPS.|
| RDS supports several popular database engines (MySQL, PostgreSQL, Oracle, SQL Server, MariaDB), allowing you to choose the one that best fits your application's requirements| While RDS offers many configuration options, it doesn't provide as much control over the database environment as a self-managed database. Certain custom configurations and extensions might not be supported. | RDS allows for easy vertical scaling (increasing instance size) and read scaling through read replicas, enabling you to handle increased load without significant downtime. | RDS requires maintenance windows for certain operations such as patching and upgrades. These maintenance periods can lead to temporary downtime or performance degradation. | RDS integrates with AWS IAM for fine-grained access control and supports encryption at rest and in transit. It also allows deployment within a VPC for network isolation.| The abstraction layer of managed services may introduce performance overhead compared to self-managed databases optimized specifically for your workloads. |

***Conclusion***

Amazon RDS offers a robust and reliable managed database service that simplifies many aspects of database management, making it an attractive choice for data pipelines that require relational database capabilities. Its high availability, security features, and ease of integration with other AWS services are significant advantages. However, its costs, limited customization options, and certain scaling limitations may pose challenges for some use cases.

---
## Data Source
Data for this project was generated from yahoo finances official website using this [link](https://finance.yahoo.com/quote/BTC-USD/history). This produces a historic data of crypto currencies that can be streamed or generated in batches.

## Setup
To set up this project, clone the repository
```bash

```

Install all python requirements requirements 
```bash
pip install -r requirements.txt
```
Run the python file main.py
Open cmd in the file location and run the command
```bash
python main.py
```

or
```bash
python3 main.py
```

Create and set up your AWS s3 bucket, Redshift and AWS RDS and using the neccessary credentials, replace it with the placeholder variables in the code.
