line = input()

dates = []

while line != "0":
    d = line.split(" ")
    d_check = d[2] + " " + d[1] + " " + d[0]
    dates.append(d_check)
    line = input()

dates.sort()

for x in dates:
    new = x.split(" ")
    print(new[2] , new[1] , new[0])