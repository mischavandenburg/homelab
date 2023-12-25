# Installing Kubernetes with KubeADM

On my first iteration of the Homelab I used kubeadm to install my cluster.

Now I'm moving to k3s. However, here are the steps I used if you are interested:

Basically following this guide, but there a few modifications

https://www.learnlinux.tv/how-to-build-an-awesome-kubernetes-cluster-using-proxmox-virtual-environment/

## Containerd

Doens't work with the guide. Use the normal apt repo, but don't make the default config file. Use no config file.

https://stackoverflow.com/questions/75246951/cri-v1-runtime-api-is-not-implemented-for-endpoint

## Repo / GPG key

Use the official guide:

https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

## Kubeadm init

The control plane endpoint is the IP of the machine that it is running on. Pod cidr is standard, needs to be this value or else it won't work.

Initializing my controlplane:

```bash
INstalling version 1.26.3

 sudo apt-get update && sudo  apt-get install -y kubeadm=1.26.3-00 kubelet=1.26.3-00 kubectl=1.26.3-00 && sudo  apt-mark hold kubeadm kubelet kubectl



```bash
sudo kubeadm init --control-plane-endpoint=192.168.178.18 --node-name k8s-controlplane --pod-network-cidr=10.244.0.0/16
```

output

```bash
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of control-plane nodes by copying certificate authorities
and service account keys on each node and then running the following as root:

  kubeadm join 192.168.178.18:6443 --token gt32hs.fdoddz9sd10hwbbt \
        --discovery-token-ca-cert-hash sha256:be9b7200cc2fdfab3bdaf49d80f55cf2853418b10a9c04dc213f0dce4a894e52 \
        --control-plane

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.178.18:6443 --token gt32hs.fdoddz9sd10hwbbt \
        --discovery-token-ca-cert-hash sha256:be9b7200cc2fdfab3bdaf49d80f55cf2853418b10a9c04dc213f0dce4a894e52

```


