# Authored By: Atharva Shah (HighnessAtharva)
# NOTE: This takes anywhere between 10-20 seconds to run. Please launch a Pull Request if you think this can be made efficient.

# import all dependencies
import time
import json
import requests
# using the requests module, grab all the JSON data from the Homebrew JSON API
r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

# Create an empty list to save all the requested data for processing later.
results = []
# t1 to time the entire process
t1 = time.perf_counter()
# To iterate over each package in order to grab the details.
for package in packages_json:
    # Store the package name and description
    package_name = package['name']
    package_desc = package['desc']

    # https://formulae.brew.sh/api/formula/a2ps.json <-- this is one of the packages in the JSON dataset.
    # We will generalize this URL to fit over all the pacakges in the formula.JSON

    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    r = requests.get(package_url)
    package_json = r.json()

    # load the gathered JSON data to a string. i.e convert it to a Python object.
    # ---> print(packages_str) <--- Uncomment this to print out the list of pacakges.
    # Now that we have filtered the result out, we need to access analytics-> install_on_requests->30d->{package_name} which is nested inside the JSON dataset.
    # Do the same for 30, 90 and 365 days.

    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    # create our own dictionary (which will be converted to JSON later) to store and process all this data instead of fetching it every time.
    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics':
        {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365
        }
    }

    results.append(data)
    # We add a slight delay to be courteous to the servers we are requesting the data from.
    # The delay is the amount of time it takes to fetch the installation details of one package.
    '''
    time.sleep(r.elapsed.total_seconds())
    '''
    # Log each result into a print statement so we can see the progress in real-time.
    print(f'Got {package_name} in {r.elapsed.total_seconds()} seconds.')
    # --> break <-- Use break to test for individual packages. (To lower time boundary)
    # This gets installation details of all the packages
    # print(package_name, package_desc, installs_30, installs_90, installs_365)

t2 = time.perf_counter()
print(f'Job done in {t2-t1} seconds.')
# store all the details into a our own JSON file.
with open('packages_info.json', 'w') as f:
    # Use json.dump to save the dictionary object to a JSON file. Use json.dumps to save it to a string varaible.
    json.dump(results, f, indent=2)
