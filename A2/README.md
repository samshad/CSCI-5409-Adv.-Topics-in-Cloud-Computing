# Flask MySQL Application with Docker on AWS EC2 and RDS

Walkthrough of setting up and running a Flask application with a MySQL database hosted on AWS RDS. The application is containerized using Docker and deployed on an AWS EC2 instance.

## Prerequisites

1. AWS Account
2. AWS EC2 instance (Used: Amazon Linux 2023 AMI)
3. AWS RDS instance (Used: MySQL)
4. Docker installed on the EC2 instance
5. `.env` file with database configuration

## Steps

### 1. Update and Install Docker on EC2

First, update the system packages and install Docker:

```bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
```

### 2. Configure Docker Permissions
Allow the current user to run Docker commands:

```bash
sudo chmod 666 /var/run/docker.sock
```

### 3. Create the .env File
Create a .env file in project directory with the following content:

```bash
DB_HOST=<your-rds-endpoint>
DB_USER=<your-db-username>
DB_PASSWORD=<your-db-password>
DB_NAME=<your-db-name>
```
Replace <your-rds-endpoint>, <your-db-username>, <your-db-password>, and <your-db-name> with your actual RDS endpoint and database credentials.

### 4. Build and Run the Docker Container
Build the Docker image:

```bash
docker build --no-cache -t flask-app .
```

Run the Docker container:

```bash
docker run -d -p 80:5000 --env-file .env flask-app
```

### 5. Stop and Remove Docker Containers (Optional)
To stop and remove all Docker containers, you can use the following commands:

```bash
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
```

### 6. Clean Up Docker System (Optional)
To clean up Docker system and remove all images, containers, and volumes:

```bash
docker system prune -a --volumes
```

## Flask Application Endpoints
### Store Products

#### Endpoint: POST /store-products

Request Body:
```json
{
    "products": [
        {
            "name": "Product 1",
            "price": "100",
            "availability": true
        },
        {
            "name": "Product 2",
            "price": "200",
            "availability": false
        }
    ]
}

```

Response:
- 200 OK: If products are stored successfully
- 400 Bad Request: If there is an error in the request


### List Products
#### Endpoint: GET /list-products

Response:
```json
{
    "products": [
        {
            "name": "Product 1",
            "price": "100",
            "availability": true
        },
        {
            "name": "Product 2",
            "price": "200",
            "availability": false
        }
    ]
}
```
- 200 OK: If products are retrieved successfully
- 500 Internal Server Error: If there is an error in retrieving products

### Drop Products Table
#### Endpoint: GET /drop-table

Response:
- 200 OK: If the table is dropped successfully
- 500 Internal Server Error: If there is an error in dropping the table

## Directory Structure
```bash
/src
│
├── Dockerfile
├── app.py
├── db.py
├── requirements.txt
└── .env
```
