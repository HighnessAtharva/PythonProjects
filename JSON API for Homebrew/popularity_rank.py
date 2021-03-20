import json


def install_sort(package):
    return package['analytics']['30d']


with open('packages_info.json', 'r') as f:
    data = json.load(f)

# filter only those pacakges which have a specific keyword in their description
# eg. filters packages with video in description. Just some extra functionality.
data = [item for item in data if 'video' in item['desc']]
data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data, indent=2)
# Use list slicing to get only the top 5 items or so.
# data_str = json.dumps(data [:5],indent=2)
print(data_str)
