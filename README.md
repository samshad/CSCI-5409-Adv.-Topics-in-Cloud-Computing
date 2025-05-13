# CSCI 5409 — Advanced Topics in Cloud Computing
Dalhousie University · Summer 2024  
Author · Md Samshad Rahman (`@samshad`)

> A compact portfolio of every lab, assignment, Kubernetes exercise and capstone project completed for **CSCI 5409 – Advanced Topics in Cloud Computing**.  
> The repo walks from “hello‑containers” all the way to a production‑style, cloud‑native application running behind Kubernetes with IaC and CI/CD.

---

## 🌐  What you’ll find here

| Folder | Theme | Key tech & skills |
|--------|-------|-------------------|
| **A1** | *Containerisation basics* | Docker CLI, multi‑stage `Dockerfile`, `docker‑compose.yml`, inter‑container networking, health‑checks |
| **A2** | *Compute & storage in AWS* | EC2 auto‑scaling groups, S3 object store, RDS/PostgreSQL, AWS CLI & SDK, IAM least‑privilege |
| **A3** | *Network & security* | VPC / subnets, security groups, API Gateway, HTTPS termination, CloudWatch logging, defence‑in‑depth |
| **K8s** | *Orchestration lab* | Kubernetes `Deployment`/`Service`/`Ingress`, Helm basics, rolling updates, `kubectl` debugging, GitHub Actions → GKE |
| **Term Assignment** | *Cloud‑native capstone* | React (front‑end) + Python/FastAPI (back‑end), Terraform IaC, CI/CD pipeline, end‑to‑end monitoring & logging |

> ⭐ **Languages:** ≈ 75 % Python, 24 % JavaScript, plus Dockerfiles, shell scripts and HCL/Terraform  
> 📁 **Repo size:** 7 commits, 5 main directories

---

## 🚀  Quick start

```bash
# Clone the repo
git clone https://github.com/samshad/CSCI-5409-Adv.-Topics-in-Cloud-Computing.git
cd CSCI-5409-Adv.-Topics-in-Cloud-Computing
```

| Task | Command |
|------|---------|
| **Run A1 locally** | `cd A1 && docker compose up --build` |
| **Deploy A2 on AWS** | `cd A2 && ./deploy.sh` *(requires AWS CLI credentials)* |
| **Spin up K8s lab on Minikube** | `cd K8s && kubectl apply -f manifests/` |
| **Provision capstone with Terraform** | `cd "Term Assignment/infra" && terraform init && terraform apply` |

> **Prerequisites:** Docker ≥ 24, Python 3.11, Node 18 (for React), AWS account (for A2/A3), kubectl & minikube or a GKE/EKS cluster (for K8s & Term Assignment).

---

## 🧠  Learning outcomes

* **Container foundations** – minimal, secure Dockerfiles and multi‑service orchestration with Compose.  
* **Cloud primitives** – launching compute, attaching managed storage, configuring IAM, and collecting metrics.  
* **Secure networking** – carving private/public subnets, API Gateway front‑doors, TLS, and least‑privilege SGs.  
* **Kubernetes operations** – declarative deployments, rolling upgrades, autoscaling, and Helm templating.  
* **DevOps & IaC** – GitHub Actions pipelines, Terraform‑as‑code, and push‑to‑deploy workflows.  
* **Full‑stack architecture** – React UI ↔ FastAPI micro‑services ↔ PostgreSQL, all containerised and observable.

---

## 🛠  Toolchain

| Domain | Stack |
|--------|-------|
| **Back‑end** | Python 3.11 · FastAPI · SQLAlchemy · PostgreSQL |
| **Front‑end** | React 18 · Vite · Tailwind CSS |
| **Containers** | Docker · Docker Compose · Docker Hub |
| **Cloud** | AWS (EC2 · S3 · RDS · API Gateway · IAM · CloudWatch) |
| **Orchestration** | Kubernetes · Helm · kubectl |
| **Infra‑as‑Code** | Terraform |
| **CI/CD** | GitHub Actions |

---

## 📂  Repository layout

```
.
├── A1/                    # Assignment 1 – container fundamentals
├── A2/                    # Assignment 2 – compute & storage on AWS
├── A3/                    # Assignment 3 – network & security on AWS
├── K8s/                   # Kubernetes lab exercises & manifests
├── Term Assignment/       # Capstone full‑stack cloud‑native project
└── .gitignore
```

Each sub‑folder is self‑contained with its own `README` (or inline comments) and run scripts.

---

## 📄 Licence

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.  
© 2025 Md Samshad Rahman
