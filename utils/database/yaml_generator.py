import yaml
import os
import logging
from typing import List, Any, Dict
from string import Formatter


def load_template(file_path: str) -> List[Any]:
    try:
        with open(file_path, "r") as file:
            return list(yaml.safe_load_all(file))
    except FileNotFoundError:
        logging.error(f"Template file not found: {file_path}")
        raise
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML template: {e}")
        raise


def process_template(
    template: Dict[str, Any], params: Dict[str, Any]
) -> Dict[str, Any]:
    def replace_placeholders(obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: replace_placeholders(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [replace_placeholders(item) for item in obj]
        elif isinstance(obj, str):
            return Formatter().vformat(obj, (), params)
        return obj

    return replace_placeholders(template)


def generate_yaml_configs(template_path: str, params: Dict[str, Any]) -> str:
    try:
        templates = load_template(template_path)
        processed_configs = [
            process_template(template, params) for template in templates
        ]
        return "\n---\n".join(
            yaml.dump(config, default_flow_style=False) for config in processed_configs
        )
    except Exception as e:
        logging.error(f"Error generating YAML configs: {e}")
        raise


def create_kubernetes_config(
    template_path: str, params: Dict[str, Any], output_dir: str
) -> str:
    try:
        yaml_configs = generate_yaml_configs(template_path, params)
        output_path = os.path.join(
            output_dir, f"{params['prefix']}_kubernetes_configs.yaml"
        )
        with open(output_path, "w") as f:
            f.write(yaml_configs)
        logging.info(f"YAML configurations have been written to {output_path}")
        return output_path
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
