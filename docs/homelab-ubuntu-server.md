# Ubuntu Server

This are the steps I took to configure Ubuntu Server on an old laptop I had lying around.

# Laptops

Disable hibernate on lid close:

https://askubuntu.com/questions/141866/keep-ubuntu-server-running-on-a-laptop-with-the-lid-closed

To disable entering the sleep mode I had to edit the /etc/systemd/logind.conf file and modify the line:

```bash

#HandleLidSwitch=suspend

to

HandleLidSwitch=ignore

Additionally, ensure that the file also has this line:

LidSwitchIgnoreInhibited=no

Then restart the OS via:

sudo service systemd-logind restart
```

# Network Configuration

## ubuntu-controlplane

```bash
sudo cat 00-installer-config-wifi.yaml

# This is the network config written by 'subiquity'
network:
  version: 2
  wifis:
    wlp3s0:
      optional: true
      access-points:
        "Den Burg":
          password: "mypass"
      addresses: [192.168.178.18/24]
      nameservers:
        addresses: [192.168.178.1]
      routes:
        - to: default
          via: 192.168.178.1

```

I had a problem with slow startup. Fixed by setting all the network devices to `optional: true`

```bash
network:
  ethernets:
    enp4s0f2:
      dhcp4: true
      optional: true
  version: 2
```


Links:

202304112204

[[homelab]]
