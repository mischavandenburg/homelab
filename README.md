# Homelab

This repo contains all of the configuration and documentation of my homelab.

I began working on this 2023-12-25.

Most of the homelab work is documented on my [YouTube channel](https://www.youtube.com/channel/UCDAck-gFPTrgTx_qp59-bQA)

## Tooling

* k3s

## Goals

* Run Prometheus and Grafana stack
* Have Grafana dashboard available with a URL
  * ingress
  * tls
  * DNS
* Everything should be deployed using GitOps
  * Try out Flux

## TODO

* [] Use UFW on all servers
* [] Look into prometheus data source basic auth
* [] look into Flagger
* [] 
* [] 

## Decisions

### Using k3s

By using k3s I'm commiting to a certain way of configuring the cluster and a set of resources that come with it. In my day job I mostly use Azure Kubernetes Service, so I am fine with not deepening my knowledge of running on-prem Kubernetes at this point in my journey. There is so much more involved with provisioning clusters with kubeadm which will slow me down to get up and running with my homelab.

At this point it is more important to me to keep things light and fun, and to learn more about deploying and managing a cluster, not necessarily the privisioning of the clusters.

# Log


# 2023-12-26

* installed prometheus stack
* tried out Flux in Azure
* made decision to use Flux on homelab
* studied Flux and learned how it works


## 2023-12-25

* cleaned up old kubeadm install from controlplane
* set up k3s on controlplane
* added k3s documentation
* set up repo and added documentation of earlier install


