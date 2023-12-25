# k3s

Decided to use k3s for installing Kubernetes. Used Kubeadm before, but prefer a less complicated approach for now. Even though kubeadm is a great way to learn, and I managed without problems, for long-term maintenance it is better to use k3s or microk8s. It also takes away cert complexity for now. Might use kubeadm later.

## Installing k3s

Just used the docs.

https://docs.k3s.io/

Struggled a bit with the error "The connection to the server localhost:8080 was refused - did you specify the right host or port?"

https://devops.stackexchange.com/questions/16013/k3s-the-connection-to-the-server-localhost8080-was-refused-did-you-specify-t

Problem was a faulty kubeconfig configuration.

Also had to disable ufw

