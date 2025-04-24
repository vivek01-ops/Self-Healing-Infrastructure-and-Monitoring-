#!/bin/bash

# Start the NGINX Prometheus exporter
# This assumes the NGINX exporter container will scrape from NGINX on port 80

export NGINX_SCRAPE_URI="http://nginx:80/stub_status"

# Run the exporter
/nginx-prometheus-exporter -nginx.scrape-uri=$NGINX_SCRAPE_URI
