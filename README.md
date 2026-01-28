# 🛡️ Resilience Store: Chaos Engineering with Istio Ambient Mesh

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Istio](https://img.shields.io/badge/istio-%23466BB0.svg?style=for-the-badge&logo=istio&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Chaos Mesh](https://img.shields.io/badge/Chaos%20Mesh-blue?style=for-the-badge)

A demonstration of **Resilient Microservices Architecture** on Kubernetes. This project builds a Python Flask application and uses **Istio Ambient Mesh** to enforce safety limits (Timeouts) against network failures simulated by **Chaos Mesh**.

---

## 🏗️ Architecture

Traffic flows through the system in the following stages:

1.  **User Request** (`curl`) hits the **Istio Ingress Gateway**.
2.  **Gateway API Route** enforces a strict **0.5s Timeout**.
3.  Traffic is forwarded to the **Resilience Store Service**.
4.  **Chaos Mesh** intercepts the packet and injects a **2.0s Latency** (Simulating a slow network/database).
5.  **Result:** The Istio Gateway cuts the connection at 0.5s, returning a `504 Gateway Timeout` instead of letting the user wait indefinitely.

```mermaid
graph LR
    User[User/Curl] -- HTTP Request --> Gateway[Istio Gateway]
    subgraph "Kubernetes Cluster"
        Gateway -- "Enforces 0.5s Timeout" --> Route[HTTPRoute]
        Route --> Service[Store Service]
        Service -- "2.0s Chaos Delay" --> Pod[Python App + Redis]
    end