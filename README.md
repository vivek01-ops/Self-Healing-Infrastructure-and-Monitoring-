# Self-Healing Infrastructure Demo

This project demonstrates automated service recovery using Prometheus, Alertmanager, and Ansible.

## 🔧 Components

- **NGINX:** Sample service to monitor
- **Prometheus:** Monitors service uptime
- **Alertmanager:** Sends webhook when alert fires
- **Webhook Server:** Triggers Ansible on alert
- **Ansible:** Restarts NGINX

## 🚀 How it works

1. Prometheus monitors NGINX via metrics exporter
2. If NGINX goes down, alert triggers in 30s
3. Alertmanager sends webhook to Python server
4. Python server runs Ansible playbook
5. Ansible restarts the NGINX service

## 🧪 Testing

- Stop NGINX: `sudo systemctl stop nginx`
- Watch logs: `tail -f logs/webhook.log`
- Confirm NGINX is restarted automatically

## 📦 File Structure

See folder structure and files in this repo.

---
# Self-Healing-Infrastructure-and-Monitoring-
# Self-Healing-Infrastructure-and-Monitoring-
