# 🏠 Homelab

# 🚧  Currently under heavy construction 🚧

I'm overhauling my entire structure and cluster setup.

Weekly updates with in-depth explanation are posted in my DevOps community:

<https://skool.com/kubecraft>

## Introduction

This repo contains all of the configuration and documentation of my homelab.

Most of the homelab work is documented on my [YouTube channel](https://www.youtube.com/channel/UCDAck-gFPTrgTx_qp59-bQA)

The purpose of my homelab is to learn and to have fun. Being a Cloud Native Engineer by trade, I work with Kubernetes every day, and my homelab is the place where I can try out and learn new things. On the other hand, by self-hosting some applications, it makes me feel responsible for the entire process of deploying and maintaining an application from A to Z. It forces me to think about backup strategies, security, scalability and the ease of deployment and maintenance.

## Principles

I have a few principles that guide my choices for my homelab.

* Being an Azure focused engineer, I try to leverage Azure solutions when possible to use in a cluster that's running on local hardware
* I try to keep in the Azure Kubernetes Service (AKS) ecosystem. This is why I chose Flux for GitOps, for example
* Storage is provisioned on my Synology NAS and database backups are made to Azure Blob Storage
* I aim to adopt best practices in deployment and security
* Everything is deployed through GitOps
* When selecting self hosted options, I always opt for the ones that allow me to run a separate Postgres database that I can manage myself

## Cluster Provisioning

I use [Talos Linux](https://www.talos.dev/) to set up my machines. I love Talos because it is so lightweight and minimal, and it provides production grade security right out of the box. It also forces me to use all my servers as Kubernetes nodes only, so I need to figure out ways to run all my desired workloads and services on Kubernetes.

## Hardware

I'm running a staging and production cluster. I decided to run two clusters so I stay in the habit of separating environments. And because then I can justify to buy more hardware 😏

I use a combination of HP ELITEDESK mini pc's, old laptops and sometimes a few virtual machines. The mini PC's are great because they are small and cheap to buy when you get them refurbished from a reseller.

### Staging

This is my playground where I can destroy things freely. Databases in staging don't contain data. In staging I allow workload pods to be scheduled on the control plane.

* controlplane-1  HP ELITEDESK 800 G2 MINI i3-6100T/8GB/240GB SSD
* worker-2        HP ELITEDESK 800 G2 MINI i3-6100T/8GB/240GB SSD

I also use a Thinkpad T480 with 32GB of memory running Ubuntu Desktop. This is my personal machine and I sometimes add a few VMs to the staging cluster when I need them. I use VirtualBox as a hypervisor to provision VMs with Talos Linux.

### Production

No pods are allowed to be scheduled on the control plane in production.

* controlplane-1  Lenovo ThinkPad T430 i5 8GB RAM
* worker-1        HP ELITEDESK 800 G2 MINI i5-6400T/16GB/240GB SSD
* worker-2        HP ELITEDESK 800 G2 MINI i3-6100T/8GB/240GB SSD

## Databases

If you couldn't tell already, I quite like databases. I worked with the EDB operator at one of my clients, and I think it's a great solution to run databases on Kubernetes as long as you know what you're doing and you're able to make backups to an object store.

I doubted for a while whether I should choose the CloudnativePG or EDB operator, but I went for EDB (EnterpriseDB) because it's more likely that I'll work with this operator during my day job. Additionally, the EDB documentation is better.

## Secrets

* Secrets are synced to Azure Key Vault
* SAS tokens for Storage Account Access
  * Note to self: expiry in 2 years

## Repo Structure

Decided to fully commit to Flux CD and their best practices.

Set up the repo according to this guide:

<https://fluxcd.io/flux/guides/repository-structure/>

And following this example:

<https://github.com/fluxcd/flux2-kustomize-helm-example>
