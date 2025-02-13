# 🏠 Homelab

As featured on YouTube and in my private DevOps community.

Frequent updates with in-depth explanations are posted here:

<https://skool.com/kubecraft>

You can also ask me questions directly when you join this community. I'm happy to mentor you on your homelab journey!

## Introduction

This repo contains all of the configuration and documentation of my homelab.

The purpose of my homelab is to learn and to have fun. Being a Cloud Native Engineer by trade, I work with Kubernetes every day, and my homelab is the place where I can try out and learn new things. On the other hand, by self-hosting some applications, it makes me feel responsible for the entire process of deploying and maintaining an application from A to Z. It forces me to think about backup strategies, security, scalability and the ease of deployment and maintenance.

## Cluster Provisioning & Architecture

I use [Talos Linux](https://www.talos.dev/) to set up my machines. I prefer Talos because it is lightweight and minimal, and provides production grade security right out of the box. After running plain Talos for over a year, I switched to using [Sidero Omni](https://www.siderolabs.com/platform/saas-for-kubernetes/) to manage my Talos clusters. Omni allows me to freely add nodes and destroy them, scaling my clusters as desired.

I am currently testing out a new architecture of single-node clusters where the workloads are scheduled on the control plane. A wise man taught me the phrase "no in-place upgrades", and I desire to move in that direction. Instead of one big cluster, I'm now running several. Omni makes this extremely easy.

<table>
    <tr>
        <th>Number</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
    <td>1</td>
    <td>Jotunheim</td>
        <td>Contains all end-user applications. Stateless, fully provisioned from code. Can be torn down and spun up within minutes on different hardware.</td>
    </tr>
    <tr>
        <td>2</td>
    <td>Data</td>
        <td>Contains all my databases & state. Multi-node. Can be fully restored from Blob storage.</td>
    </tr>
    <tr>
        <td>3</td>
    <td>Moria</td>
        <td>Private cluster provisioned from private repository.</td>
    </tr>
</table>

## :computer: Hardware

### Nodes

I use a combination of HP ELITEDESK mini pc's, old laptops and sometimes a few virtual machines. The mini PC's are great because they are small and cheap to buy when you get them refurbished from a reseller.

HP ELITEDESK 800 G2 MINI i5-6400T/16GB/240GB SSD

HP ELITEDESK 800 G2 MINI i3-6100T/8GB/240GB SSD

HP ELITEDESK 800 G2 MINI i3-6100T/8GB/240GB SSD

HP ELITEDESK 800 G2 MINI i3-6100T/8GB/240GB SSD

Lenovo ThinkPad T430 i5 8GB RAM

## :rocket: Installed Apps & Tools

### Apps

End User Applications
<table>
    <tr>
        <th>Logo</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/commafeed.svg"></td>
        <td><a href="https://www.commafeed.com/#/welcome">Commafeed</a></td>
        <td>Bloat free RSS feed reader</td>
    </tr>
    <tr>
        <td><img width="32" src="https://www.svgrepo.com/download/499807/home-page.svg"></td>
        <td><a href="https://github.com/gethomepage/homepage">Homepage</a></td>
        <td>My customized portal to my homelab & internet</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/n8n.svg"></td>
        <td><a href="https://n8n.io/">n8n</a></td>
        <td>Secure, AI-native workflow automation</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/wallabag-light.svg"></td>
        <td><a href="https://wallabag.org/">Wallabag</a></td>
        <td>Save articles & posts from the web for storage & reading later</td>
    </tr>
</table>

### Quantified Self

I store data about myself in self-hosted Postgres databases.

A combination of n8n workflows & APIs I coded myself are used.

<table>
    <tr>
        <th>Logo</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/converse-light.svg"></td>
        <td><a href="https://ouraring.com/">Body Metrics</a></td>
        <td>Storing Oura & other data to Postgres</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/apple-light.svg"</td>
        <td><a href="https://github.com/mischavandenburg/health-api">Health API</a></td>
        <td>An API to sync Apple Health data to my personal database</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/mqtt.svg"></td>
        <td><a href="https://github.com/mischavandenburg/shelly">Home IoT</a></td>
        <td>Logs MQTT messages from sensors to databases</td>
    </tr>
</table>

### Infrastructure

Everything needed to run my cluster & deploy my applications
<table>
    <tr>
        <th>Logo</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/svg/cert-manager.svg"></td>
        <td><a href="https://cert-manager.io/">Cert Manager</a></td>
        <td>X.509 certificate management for Kubernetes.</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/cilium.svg"></td>
        <td><a href="https://cilium.io/">Cilium</a></td>
        <td>My CNI of choice, used on all clusters. eBPF-based Networking, Observability, Security</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/cloudflare-zero-trust.png"></td>
        <td><a href="https://developers.cloudflare.com/cloudflare-one/">Cloudflare Zero Trust</a></td>
        <td>Used for private tunnels to expose public services (without requiring a public IP).</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/postgresql.svg"></td>
        <td><a href="https://cloudnative-pg.io/">CloudNativePG</a></td>
        <td>Database operator for running PostgreSQL clusters</td>
    </tr>
    <tr>
        <td><img width="32" src="https://www.svgrepo.com/download/530451/dns.svg"></td>
        <td><a href="https://github.com/kubernetes-sigs/external-dns">External DNS</a></td>
        <td>Synchronizes exposed Kubernetes Services and Ingresses with DNS providers.</td>
    </tr>
    <tr>
        <td><img width="32" src="https://www.svgrepo.com/download/477066/lock.svg"></td>
        <td><a href="https://external-secrets.io/latest/">External Secrets Operator</a></td>
        <td>Used to sync my secrets from Azure Key Vaults to my cluster</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/flux-cd.svg"></td>
        <td><a href="https://fluxcd.io/">Flux CD</a></td>
        <td>My GitOps solution of choice. Better than Argo.</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/svg/grafana.svg"></td>
        <td><a href="https://grafana.com/">Grafana</a></td>
        <td>The open observability platform.</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/svg/prometheus.svg"></td>
        <td><a href="https://prometheus.io/">Prometheus</a></td>
        <td>An open-source monitoring system with a dimensional data model, flexible query language, efficient time series database and modern alerting approach.</td>
    </tr>
    <tr>
        <td><img width="32" src="https://www.svgrepo.com/download/374041/renovate.svg"></td>
        <td><a href="https://github.com/renovatebot/renovate">Renovate</a></td>
        <td>Automated dependency updates.</td>
    </tr>
    <tr>
        <td><img width="32" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/synology.svg"></td>
        <td><a href="https://github.com/SynologyOpenSource/synology-csi">Synology CSI Driver</a></td>
        <td>Used to provision Persistent Volumes directly on my Synology</td>
    </tr>
</table>

## Build your own Home Lab?

Do you feel inspired by this project, but don't know where to start?

I created the only [Kubernetes homelab course](https://skool.com/kubecraft) on the internet and helped hundreds of people start their homelab journey.

![https://skool.com/kubecraft](./images/homelab-feedback.png)

To get access to the course, go here:

<https://skool.com/kubecraft>

## :camera: Full Walkthrough

Watch this video:

[![YouTube](http://i.ytimg.com/vi/WfDwFvl5XBo/hqdefault.jpg)](https://www.youtube.com/watch?v=WfDwFvl5XBo)

## Networking

I use a Unifi Express Router, configured with 7 different VLANs which are all locked down by strict traffic rules.

I use [Cilium](https://cilium.io/) as my CNI. I use LoadBalancer IPAM to assign IP addresses to my LoadBalancer services and use Cilium as an ingress controller. This way, I don't need to install and maintain a seperate ingress controller like Traefik, which I used in the past.

### Storage

I use a Synology DS224+ as a NAS. I use the Synology CSI driver to provision Persistent Volumes from my clusters directly on the NAS. I also have an NFS share for data that needs to be shared between clusters.

## Secret Management

Azure Key Vaults are used to store my secrets. I sync them to my cluster using the External Secrets Operator.
