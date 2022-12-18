import math
import xml.etree.ElementTree as etree
import csv


class GPSPoint:
    def __init__(self, lat, lon):
        self.__lat = float(lat)
        self.__lon = float(lon)

    def get_latitude(self):
        return self.__lat
    
    def get_longitude(self):
        return self.__lon

    def set_latitude(self, lat):
        self.__lat = lat

    def set_longitude(self, lon):
        self.__lon = lon

    latitude = property(get_latitude, set_latitude)
    longitude = property(get_longitude, set_longitude)

    def __str__(self):
        return f"({self.__lat}, {self.__lon})"


class GPSManager:
    earth_radius = 6371.0

    def __init__(self, data = []):
        self.__locations = data

    def get_locations(self):
        return self.__locations

    locations = property(get_locations)

    def add_location(self,gpspoint):
        self.__locations.append(gpspoint)

    def read_from_file(self, my_file):
        with open(my_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                #print(row)
                my_gpspoint = GPSPoint(row[0], row[1])
                self.add_location(my_gpspoint)

    def create_gpx(self, trip_name, output_file):
        root = etree.Element("gpx")
        root.set("version", "1.1")
        trk = etree.SubElement(root, "trk")
        name = etree.SubElement(trk, "name")
        name.text = trip_name
        trkseg = etree.SubElement(trk, "trkseg")

        for gpspoint in self.__locations:
            trkpt = etree.SubElement(trkseg, "trkpt")
            trkpt.set("lat", str(gpspoint.get_latitude()))
            trkpt.set("lon", str(gpspoint.get_longitude()))

        tree = etree.ElementTree(root)

        tree.write(output_file, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def get_distance(gpspoint1, gpspoint2):
        lat1 = gpspoint1.get_latitude()
        lon1 = gpspoint1.get_longitude()
        lat2 = gpspoint2.get_latitude()
        lon2 = gpspoint2.get_longitude()
        fi1 = math.radians(lat1)
        fi2 = math.radians(lat2)
        delta_fi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = pow(math.sin(delta_fi / 2), 2) + math.cos(fi1) * math.cos(fi2) * pow(math.sin(delta_lambda / 2), 2)
        d = GPSManager.earth_radius * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return d






#TODO



# TESTING

gps_man = GPSManager()
gps_man.read_from_file("route.csv")

#test loading from file
assert gps_man.locations[10].latitude == 49.916661 and gps_man.locations[10].longitude == 18.202618

gps_man.create_gpx("My trip", "route.gpx")

#test static method
assert round(GPSManager.get_distance(GPSPoint(49.8987, 18.1053), GPSPoint(50.0010, 18.1234)), 4) == 11.4487

locs = gps_man.locations
dst = 0.0
for i in range(len(locs)-1):
    dst += GPSManager.get_distance(locs[i], locs[i+1])
dst = round(dst,3)
print(f"Distance is {dst} km")
assert dst == 12.732
