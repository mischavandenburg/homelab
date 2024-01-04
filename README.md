# 🏠 Homelab

This repo contains all of the configuration and documentation of my homelab.

I began working on this 2023-12-25.

Most of the homelab work is documented on my [YouTube channel](https://www.youtube.com/channel/UCDAck-gFPTrgTx_qp59-bQA)

## Hardware

I'm running a staging and production cluster. I decided to run two clusters so I stay in the habit of separating environments. And because then I can justify to buy more hardware 😏

### Staging

* control plane: old laptop with 4gb ram
* node 1: thinkpad t420 with 8gb ram


### Production

* control plane: 16gp ram i5 HP mini pc

## Tooling

* Ubuntu server as OS
* k3s for creating the cluster(s)
* Flux for GitOps

## Secrets

* Secrets are synced to Azure Key Vault
* SAS tokens for Storage Account Access
  * Note to self: expiry in 2 years


## Current Goals

* start running a few applications
* look into exposing an app using a cloudflared tunnel
* add more hardware
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

## Long Term Goals

* set up security solution to scan cluster and adopt best security practices

## TODO

* [ ] Use UFW on all servers
* [ ] Look into prometheus data source basic auth
* [ ] look into Flagger
* [x] set up loki
* [] look into Falco
* [] 
* [] 
* [] 
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
