import os
import random
import string
from datetime import datetime, timedelta, timezone
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import (
    BlobServiceClient,
    generate_container_sas,
    ContainerSasPermissions,
)

def generate_password(length=16):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def parse_connection_string(connection_string):
    """Parse the connection string and return a dictionary of its components."""
    return dict(part.split("=", 1) for part in connection_string.split(";") if part)

def create_container_and_sas(connection_string, container_name):
    """Create a new container and generate a SAS token."""
    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a new container
    blob_service_client.create_container(container_name)
    print(f"Container '{container_name}' created.")

    # Parse the connection string
    conn_parts = parse_connection_string(connection_string)
    account_name = conn_parts.get("AccountName")
    account_key = conn_parts.get("AccountKey")

    if not account_name or not account_key:
        raise ValueError("Unable to extract account name or key from connection string")

    # Generate SAS token
    sas_token = generate_container_sas(
        account_name=account_name,
        container_name=container_name,
        account_key=account_key,
        permission=ContainerSasPermissions(
            read=True, write=True, delete=True, list=True
        ),
        expiry=datetime.now(timezone.utc) + timedelta(days=730),
    )
    return sas_token

def create_azure_key_vault_secrets(prefix, key_vault_name, connection_string):
    """Create secrets in Azure Key Vault."""
    credential = DefaultAzureCredential()
    secret_client = SecretClient(
        vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=credential
    )

    # Generate secrets
    db_username = f"{prefix}_user"
    db_password = generate_password()
    container_name = prefix.lower()  # Use the prefix as the container name
    blob_sas = create_container_and_sas(connection_string, container_name)

    # Extract storage account name from connection string
    conn_parts = parse_connection_string(connection_string)
    storage_account_name = conn_parts.get("AccountName")

    if not storage_account_name:
        raise ValueError(
            "Unable to extract storage account name from connection string"
        )

    # Create secrets in Key Vault
    secret_client.set_secret(f"{prefix}-db-username", db_username)
    secret_client.set_secret(f"{prefix}-db-password", db_password)
    secret_client.set_secret(f"{prefix}-storage-account-name", storage_account_name)
    secret_client.set_secret(f"{prefix}-blob-sas", blob_sas)
    secret_client.set_secret(f"{prefix}-connection-string", connection_string)

    print(f"Secrets created in Azure Key Vault for prefix: {prefix}")
    print(
        f"Container '{container_name}' created in storage account '{storage_account_name}' with a 2-year SAS token"
    )

def main():
    prefix = input(
        "Enter the prefix for the new database (e.g., 'commafeed', 'wallabag'): "
    )
    key_vault_name = "k8s-homelab-production"
    
    # Get connection string from environment variable
    connection_string = os.environ.get("HL_AZ_CONN_STRING")
    if not connection_string:
        raise ValueError("HL_AZ_CONN_STRING environment variable is not set")

    create_azure_key_vault_secrets(prefix, key_vault_name, connection_string)

if __name__ == "__main__":
    main()   main()
