# Util

Collection of scripts and tools I use to set up or maintain my homelab

# Grafana

The kube-prometheus-stack helm chart comes with a very good set of default dashboards.

When I decided to split off my Grafana deployment, these were not included.

I use scripts to extract them from the ConfigMaps and then I copy them to a persistent volume I have mounted into the Grafana container.

The Grafana directory contains all the default dashboards which are included in the kube-prometheus-stack helm chart.
