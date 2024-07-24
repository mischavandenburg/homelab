import os
import logging
from yaml_generator import create_kubernetes_config
from setup_db import setup_database

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        # Get inputs
        prefix = input("Enter the prefix for the new database: ").strip()
        key_vault_name = os.getenv("AZURE_KEY_VAULT_NAME", "k8s-homelab-production")
        conn_string = os.getenv("HL_AZ_CONN_STRING")

        # Check if conn_string is None or empty
        if not conn_string:
            raise ValueError(
                "HL_AZ_CONN_STRING environment variable is not set or is empty"
            )

        # Setup database and get storage account name
        storage_account_name = setup_database(prefix, key_vault_name, conn_string)

        # Generate Kubernetes config
        script_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(script_dir, "kubernetes_config_template.yaml")
        params = {
            "prefix": prefix,
            "storage_account": storage_account_name,
        }
        kubernetes_config_path = create_kubernetes_config(
            template_path, params, script_dir
        )

        logging.info(
            f"Process completed successfully. Kubernetes config: {kubernetes_config_path}"
        )

    except ValueError as e:
        logging.error(f"Value error: {str(e)}")
    except Exception as e:
        logging.error(f"An error occurred in the main process: {str(e)}")


if __name__ == "__main__":
    main()
