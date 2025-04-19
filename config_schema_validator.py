import json
import yaml


class Config_Schema_Validator:

    def __init__(self):
        self.config_data = None

    def load_data(self, config):

        if config.endswith(".json"):
            with open(config, 'r') as file:
                self.config_data = json.load(file)
        elif config.endswith(".yaml"):
            with open(config, 'r') as file:
                self.config_data = yaml.safe_load(file)
        else:
            raise ValueError("invalid file format")
        return self.config_data

    def validate(self, config, schema, path=""):
        errors = []

        for key, value in schema.items():
            full_key = f"{path}.{key}" if path else key
            if key not in config:
                errors.append(f"Missing key: {full_key}")
            else:
                actual_value = config[key]
                if isinstance(value, dict):
                    if isinstance(actual_value, dict):
                        errors.extend(self.validate(actual_value, value, full_key))
                    else:
                        errors.append(f"Type Mismath: {full_key} - Expected {type(value).__name__}, got {type(actual_value).__name__}")
                else:
                    if not isinstance(actual_value, value):
                        errors.append(f"Type Mismath: {full_key} - Expected {type(value).__name__}, got {type(actual_value).__name__}")

        return errors

if __name__ == "__main__":
    schema = {
        "app_name": str,
        "version": str,
        "debug": bool,
        "database": {
            "host": str,
            "port": int
        }
    }
    csv = Config_Schema_Validator()
    config_data = csv.load_data('config.json')
    print(config_data)
    validation_errors = csv.validate(config_data, schema)

    if validation_errors:
        print("Validation Errprs:")
        for err in validation_errors:
            print(" -", err)
    else:
        print("Config is valid as per schema")