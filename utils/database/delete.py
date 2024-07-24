import os
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError, AzureError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def delete_key_vault_secrets(prefix, key_vault_name):
    try:
        secret_client = SecretClient(
            vault_url=f"https://{key_vault_name}.vault.azure.net/",
            credential=DefaultAzureCredential(),
        )
        secret_names = [
            f"{prefix}-db-username",
            f"{prefix}-db-password",
            f"{prefix}-storage-account-name",
            f"{prefix}-blob-sas",
            f"{prefix}-connection-string",
        ]
        for name in secret_names:
            try:
                secret_client.begin_delete_secret(name)
                logging.info(f"Secret '{name}' deletion initiated in Key Vault")
            except ResourceNotFoundError:
                logging.info(f"Secret '{name}' not found in Key Vault")

        logging.info(
            f"All secrets deletion initiated in Azure Key Vault for prefix: {prefix}"
        )
    except AzureError as e:
        logging.error(f"Azure operation failed: {str(e)}")
        raise


def delete_blob_container(conn_string, prefix):
    try:
        blob_service = BlobServiceClient.from_connection_string(conn_string)
        container_name = prefix.lower()
        container_client = blob_service.get_container_client(container_name)

        container_client.delete_container()
        logging.info(f"Container '{container_name}' deleted.")
    except ResourceNotFoundError:
        logging.info(f"Container '{container_name}' not found.")
    except AzureError as e:
        logging.error(f"Azure operation failed: {str(e)}")
        raise


def main():
    try:
        prefix = input("Enter the prefix of the database to delete: ").strip()
        if not prefix:
            raise ValueError("Prefix cannot be empty")

        key_vault_name = os.getenv("AZURE_KEY_VAULT_NAME", "k8s-homelab-production")
        conn_string = os.getenv("HL_AZ_CONN_STRING")
        if not conn_string:
            raise ValueError("HL_AZ_CONN_STRING environment variable is not set")

        delete_key_vault_secrets(prefix, key_vault_name)
        delete_blob_container(conn_string, prefix)

        logging.info(f"Deletion process completed for prefix: {prefix}")
    except ValueError as e:
        logging.error(str(e))
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
