import os
from ruamel.yaml import YAML


def update_yaml(config_file, params):
    yaml = YAML()

    with open(config_file, 'r') as file:
        config = yaml.load(file)

    config.update(params)

    with open(config_file, 'w') as file:
        yaml.dump(config, file)


if __name__ == "__main__":
    config_file = os.path.abspath("../xyz/abc.yaml")
    print(config_file)

    # Read parameters from individual environment variables
    params = {
        'test_case': os.getenv('TEST_CASE_ID'),
        'test_case_name': os.getenv('TEST_CASE_NAME')
    }

    update_yaml(config_file, params)