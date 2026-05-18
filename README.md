# Docker & Kubernetes Homework

Coursework from the **Robot Dreams "Docker and Kubernetes"** course (May–Jul 2025).
A small Python/Flask demo app, taken through containerisation, multi-service composition, Kubernetes deployment, observability and Helm packaging.

Each homework is preserved as a single commit on `main`; the per-HW reports
(in Ukrainian, with screenshots) live under the corresponding `HWN/` directory.

## Stack

Python 3 · Flask · PostgreSQL · Docker · docker-compose · MicroK8s · Helm · Fluentd · Loki · Grafana · Prometheus · Promtail

## Homeworks

| # | Topic | Folder |
|---|-------|--------|
| 01 | First container — Hello World        | [HW01/README.md](HW01/README.md) |
| 02 | Custom Docker image                  | [HW02/README.md](HW02/README.md) |
| 03 | Dockerfile optimisation              | [HW03/README.md](HW03/README.md) |
| 04 | Python app with build args           | [HW04/README.md](HW04/README.md) |
| 05 | Fluentd logging                      | [HW05/README.md](HW05/README.md) |
| 06 | `docker-compose` stack (Flask + Fluentd + Postgres) | [HW06/README.md](HW06/README.md) |
| 07 | MicroK8s install, first Pod          | [HW07/README.md](HW07/README.md) |
| 08 | Deployments & Services               | [HW08/README.md](HW08/README.md) |
| 09 | ConfigMaps, Secrets, persistent storage | [HW09/README.md](HW09/README.md) |
| 10 | Resource limits & HPA autoscaling    | [HW10/README.md](HW10/README.md) |
| 11 | Liveness & Readiness probes, Ingress | [HW11/README.md](HW11/README.md) |
| 13 | Helm chart, releases, rollbacks      | [HW13/README.md](HW13/README.md) |

> HW-12 is intentionally absent — the course skipped that number.

## Quick start (docker-compose)

```bash
docker compose up --build
# app:        http://localhost
# grafana:    http://localhost:3000
```

## Quick start (Helm on MicroK8s)

```bash
microk8s helm install demo ./charts/demo-app
microk8s kubectl get pods
```

## Security note

All credentials in this repo (`postgres/postgres`, `user/password`,
`postrges/postrges` in `charts/demo-app/values.yaml`, etc.) are
**placeholder demo values** for local coursework only — never deployed
anywhere reachable. Anything real (TLS keys, tokens) is gitignored.

If you fork this for your own learning, regenerate any TLS material:

```bash
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout k8s/tls.key -out k8s/tls.crt -subj "/CN=demo.local"
```
