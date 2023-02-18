import yaml

# Load YAML from file
with open('file1.yaml', 'r') as f:
    file1 = yaml.safe_load(f)
    print(file1)