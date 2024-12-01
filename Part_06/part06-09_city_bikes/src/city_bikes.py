# tee ratkaisu tänne
# Write your solution here
import math

def get_file(filename : str) -> list:
    l1 = []
    with open(filename) as f:
        for i in f:
            d1 = {}
            x = i.split(";")
            y = [j .strip() for j in x]
            if(y[0] == "Longitude"):
                continue
            else:
                d1["Longitude"] = y[0]
                d1["Latitude"] = y[1]
                d1["FID"] = y[2]
                d1["Name"] = y[3]
                d1["total_slot"] = y[4]
                d1["operative"] = y[5]
                d1["id"] = y[6]
                l1.append(d1)
    return l1

def get_station_data(filename : str):
    station_data = get_file(filename)
    d2 = {}
    for i,j in enumerate(station_data):
        d2[j["Name"]] = (float(j["Longitude"]),float(j["Latitude"]))
    return d2

def distance(stations : dict, station1 :str, station2 :str):
    x_km = (float(stations[station1][0]) - float(stations[station2][0]))*55.26
    y_km = (float(stations[station1][1]) - float(stations[station2][1]))*111.2
    distance_km = math.sqrt(x_km**2 +y_km**2)
    return distance_km

def greatest_distance(stations :dict):
    greatest = ("a","b",0)
    for i,j in stations.items():
        for k,l in stations.items():
            if(abs(distance(stations,i,k)) > greatest[2]):
                greatest = (i,k,abs(distance(stations,i,k)))
    return greatest
