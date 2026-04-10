# Docker Project Workflow

## 1. Create project folder

```bash id="5gqf0k"
mkdir project-folder
cd project-folder
```

## 2. Create required files

```text id="3w9rpl"
app.py
requirements.txt
Dockerfile
```

Optional:

```text id="u5t6n1"
.dockerignore
db-data/
```

## 3. Build Docker image

```bash id="b6m8c2"
docker build -t image-name .
```

Example:

```bash id="n7d9e4"
docker build -t flask-network-app .
```

## 4. Run container

```bash id="p1q2w3"
docker run -d --name container-name -p 5000:5000 image-name
```

Example:

```bash id="v4x5z6"
docker run -d --name web-app -p 5000:5000 flask-network-app
```

## 5. Check if container is running

```bash id="r8t9y1"
docker ps
```

## 6. If not running, check exited containers

```bash id="k2l3m4"
docker ps -a
```

## 7. If container exited, inspect logs

```bash id="f5g6h7"
docker logs container-name
```

Example:

```bash id="a8b9c1"
docker logs web-app
```

## 8. After container is running, test app

```bash id="d2e3f4"
curl http://localhost:5000
```

# Networking Workflow

## 1. Create network

```bash id="g5h6i7"
docker network create app-network
```

## 2. Run database container

```bash id="j8k9l1"
docker run -d --name postgres-db \
  --network app-network \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=myapp \
  -v $(pwd)/db-data:/var/lib/postgresql \
  postgres
```

## 3. Run app container on same network

```bash id="m2n3o4"
docker run -d --name web-app \
  --network app-network \
  -p 5000:5000 \
  flask-network-app
```

## 4. Use container name as hostname inside app

```text id="p5q6r7"
postgres-db
```

Example DB URL:

```text id="s8t9u1"
postgresql://postgres:mypassword@postgres-db:5432/myapp
```
