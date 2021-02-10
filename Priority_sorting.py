# Code to sort projects as 'managers' and 'watchers', in the right priority order

import json

with open('source_file_2.json', 'r') as sourceFile:
    project_details = sourceFile.read()
    
project_data = json.loads(project_details)    #import source file data 

#sort projects according to priority
sorted_projects = sorted(project_data, key=lambda item: item['priority'])
print(sorted_projects)

managers = {}
watchers = {}

for p in sorted_projects:
    for m in p['managers']:
        if m in managers:
            managers[m].append(p['name'])
            print("Appending",p['name']," to manager",managers[m])
        else:
            managers[m] = [p['name']]
            print("Adding to managers list",p['name'])
            
    for w in p['watchers']:
        if w in watchers:
            watchers[w].append(p['name'])
            print("Appending",p['name']," to watcher",watchers[w])
        else:
            watchers[w] = [p['name']]
            print("Adding to watchers list",p['name'])
     
print("creating json files with list of managers and watchers along with project names")     
with open('managers.json', 'w') as manager_file:
    manager_file.write(json.dumps(managers, indent=4, sort_keys=True))

with open('watchers.json', 'w') as watcher_file:
    watcher_file.write(json.dumps(watchers, indent=4, sort_keys=True))
    
sourceFile.close()
manager_file.close()
watcher_file.close()