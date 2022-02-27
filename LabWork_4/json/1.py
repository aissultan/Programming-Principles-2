import json

with open("sample-data.json", "r") as json_file:
    d = json.load(json_file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
a = d["imdata"]
for i in a:
    for j in i.values():
        st = j["attributes"]["dn"][-2] + j["attributes"]["dn"][-3]
        if j["attributes"]["dn"][-3] == "/":
            print(j["attributes"]["dn"], "                             ", j["attributes"]["speed"], " ", j["attributes"]["mtu"])
        else:
            print(j["attributes"]["dn"], "                            ", j["attributes"]["speed"], " ", j["attributes"]["mtu"])


