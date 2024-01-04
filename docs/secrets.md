# Key Vault Setup

```bash
SPNAME=homelab-keyvault-main
az ad sp create-for-rbac --skip-assignment --name $SPNAME
```

then you assign the application id (client id) of the application, and create the secret in the application
