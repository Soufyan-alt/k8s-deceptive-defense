🛡️ Deceptive Defense: Kubernetes Honeypot & Runtime Security with Falco

An advanced DevSecOps cloud security implementation focusing on deceptive container security, kernel-level behavioral system call interception, and automated cloud-native intrusion detection within local Kubernetes orchestration environments.

---

## 🛠️ Tech Stack & Tools

Technologies and tools used in this project
💻 Operating Systems & Environments
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)
![Minikube](https://img.shields.io/badge/Minikube-326CE5?style=flat&logo=kubernetes&logoColor=white)

### ☁️ Virtualization & Containers
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1626?style=flat&logo=helm&logoColor=white)

### 🔒 Security & Deception
![Falco](https://img.shields.io/badge/Falco-00E676?style=flat&logo=falco&logoColor=black)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

## 📊 Threat Model: Attack vs. DevSecOps Defense

🥷 Hacker Attack Vector
```text
[ Malicious Internal Pod ]
           │
           │ Step 1: Internal Reconnaissance
           ▼
[ Exposed redis-service:6379 ]
           │
           │ Step 2: Access & Exploration
           ▼
[ Deceptive Redis Honeypot ]
   (Captures IP & Commands)
           │
           │ Step 3: Interactive Escape
           ▼
   ⚠️ Executed: /bin/sh
