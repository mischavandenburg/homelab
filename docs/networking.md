# Networking

## Grafana

Exposing the Grafana service as a loadbalancer. Edit the service and change to type LoadBalancer and use the following configuration:

  ports:
  - name: http-web
    nodePort: 31380
    port: 3000
    protocol: TCP
    targetPort: 3000


Now Grafana UI is accessible using the IP of the controlplane and port 3000
