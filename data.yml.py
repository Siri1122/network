import yaml
with open("data.yml","r") as f:
    data=yaml.safe_load(f)
print(data)
