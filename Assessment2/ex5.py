import json
file = open('ex5.json', 'r')
data = json.load(file)
file.close()  
for donut in data:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append({"id": "5001", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(data, file, indent=4)
file.close()  
