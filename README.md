# 🏠 Homelab

This repo contains all of the configuration and documentation of my homelab.

Most of the homelab work is documented on my [YouTube channel](https://www.youtube.com/channel/UCDAck-gFPTrgTx_qp59-bQA)

The purpose of my homelab is to learn and to have fun. Being a Cloud Native Engineer by trade, I work with Kubernetes every day, and my homelab is the place where I can try out and learn new things. On the other hand, by self-hosting some applications, it makes me feel responsible for the entire process of deploying and maintaining an application from A to Z. It forces me to think about backup strategies, security, scalability and the ease of deployment and maintenance.

## Principles

I have a few principles that guide my choices for my homelab.

* Being an Azure focused engineer, I try to leverage Azure solutions when possible to use in a cluster that's running on local hardware
* I try to keep in the Azure Kubernetes Service (AKS) ecosystem. This is why I chose Flux for GitOps, for example
* I currently have low storage needs, so I have no NAS setup. Backups are made to Azure Blob Storage
* I aim to adopt best practices in deployment and security
* Everything is deployed through GitOps
* All applications and infrastructure are run entirely on Kubernetes. I have no VM's running auxiliary services such as DNS or storage
* When selecting self hosted options, I always opt for the ones that allow me to run a separate Postgres database that I can manage myself
* I don't rely on persistent storage or stateful sets

## Cluster Provisioning

I use [Talos Linux](https://www.talos.dev/) to set up my machines. I love Talos because it is so lightweight and minimal, and it provides production grade security right out of the box. It also forces me to use all my servers as Kubernetes nodes only, so I need to figure out ways to run all my desired workloads and services on Kubernetes.

## Hardware

I'm running a staging and production cluster. I decided to run two clusters so I stay in the habit of separating environments. And because then I can justify to buy more hardware 😏

### Staging

My staging cluster is currently running only on virtual machines. I use a Thinkpad T480 with 32GB of memory running Ubuntu Desktop. I use VirtualBox as a hypervisor to provision VMs with Talos Linux.

Currenntly running 3 VMs:

* controlplane-1  1CPU 4GB RAM
* worker-1        1CPU 4GB RAM
* worker-2        1CPU 4GB RAM

### Production

* controlplane-1  Lenovo ThinkPad T430 i5 8GB RAM 
* worker-1        HP ELITEDESK 800 G2 MINI i5-6400T/16GB/240GB SSD
* worker-2        Virtual Machine on Thinkpad T480 1CPU 4GB RAM

## Databases

If you couldn't tell already, I quite like databases. I worked with the EDB operator during one of my assignments, and I think it's a great solution to run databases on Kubernetes as long as you know what you're doing and you're able to make backups to an object store.

I doubted for a while whether I should choose the CloudnativePG or EDB operator, but I went for EDB (EnterpriseDB) becuase it's more like that I'll work with this operator during my day job. Additionally, the EDB documentation is better.

## Secrets

* Secrets are synced to Azure Key Vault
* SAS tokens for Storage Account Access
  * Note to self: expiry in 2 years


## Current Goals

* securing monitoring deployment with auth and secrets
* Monitoring notifications to Telegram

## Apps to Run

* [] linkding (use in combination with [companion](https://github.com/acez/bookmark-companion) on ios)
* [] RSS reader
* [] 
* [] Wallabag (read later app, maybe not needed with linkding)
* [] 
* [] 

## Achieved Goals

* set up a vault solution for secrets
* Run Prometheus and Grafana stack
* Have Grafana dashboard available with a URL
  * ingress
  * tls
  * DNS
* Everything should be deployed using GitOps
  * Try out Flux
* set up loki
* start running a few applications
* look into exposing an app using a cloudflared tunnel
* add more hardware

## Long Term Goals

* set up security solution to scan cluster and adopt best security practices

## TODO

* [ ] Look into prometheus data source basic auth
* [ ] look into Flagger
* [x] set up loki
* [] look into Falco
* [] cloudflare secret to key vault
* [] grafana REQ_URL environment variable in pod, try to disable loadbalancer
* [] mealie configmap env and secretenv
* [] mealie delete hostport
* [] mealie switch to production issuer
* [] disable grafana agent
* [] 

## Decisions

### Using k3s

By using k3s I'm commiting to a certain way of configuring the cluster and a set of resources that come with it. In my day job I mostly use Azure Kubernetes Service, so I am fine with not deepening my knowledge of running on-prem Kubernetes at this point in my journey. There is so much more involved with provisioning clusters with kubeadm which will slow me down to get up and running with my homelab.

At this point it is more important to me to keep things light and fun, and to learn more about deploying and managing a cluster, not necessarily the privisioning of the clusters.

### Repo Structure

Decided to fully commit to Flux and their practices.

Set up the repo according to this guide:

https://fluxcd.io/flux/guides/repository-structure/

And following this example:

https://github.com/fluxcd/flux2-kustomize-helm-example


2024-01-04

In [this commit](https://github.com/mischavandenburg/homelab/commit/3a65ae4707b633929f89cdc09490595ccfb9470b) I did a big refactor to enable base and environment layers.

# Log

# 2023-12-26

* installed prometheus stack
* tried out Flux in Azure
* committed to using Flux on homelab
* studied Flux and learned how it works
* commited to using Flux way of structuring repo
* configured Weave UI to access Flux
* configured Grafana and Weave with ingress so they are available on fake local domains: weave. and grafana.homelab.nl


## 2023-12-25

* cleaned up old kubeadm install from controlplane
* set up k3s on controlplane
* added k3s documentation
* set up repo and added documentation of earlier install
