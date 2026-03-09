# Lab 3: Multi-Tenancy with Namespaces and Internal Routing

## Scenario
Single cluster used for both Dev and Staging environments for cost efficiency.
Two-tier application (frontend + backend) deployed in each namespace with internal routing via ClusterIP services.

---

## Project Structure
```text
.
├── dev-environment.yaml
├── staging-environment.yaml
├── Dockerfile.backend
├── Dockerfile.frontend
├── backend-app.py
├── index.html
├── nginx.conf
└── README.md
```

---

## Build Instructions
```bash
docker build -f Dockerfile.backend -t backend-app:latest .
docker build -f Dockerfile.frontend -t frontend-app:latest .
```

---

## Deployment
```bash
kubectl apply -f dev-environment.yaml
kubectl apply -f staging-environment.yaml
```

---

## Screenshots

### 1. Dev Namespace — Pods & Services
```bash
kubectl get pods,svc -n dev
```
![Dev Namespace](1.png)

---

### 2. Staging Namespace — Pods & Services
```bash
kubectl get pods,svc -n staging
```
![Dev Namespace](2.png)

---

### 3. Frontend App in Browser
```bash
kubectl port-forward pod/frontend-pod 8082:80 -n dev
```
![Dev Namespace](browser.png)
