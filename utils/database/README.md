# Database Helper Program

This will create the secrets in my keyvault, set up a container in my storage account, and generate the YAML for the database cluster.

To do:

- Turn into CLI using Typer
- Ask if I want to generate template for Deployment

The Deployment template might be necessary as a dummy because the secret needs to be mounted somewhere in order to be synced.

HL_AZ_CONN_STRING string is the connection string of the storage account, Security & networking > Access keys > key1 > connection string.

## Running

```bash
az login --use-device-code
poetry shell
poetry install
python3 main.py
```
