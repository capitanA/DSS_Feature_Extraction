import csv


class CsvFile:
    def __init__(self, simtime=0, latitude=0, longitude=0, sog=0, cog=0, heading=0, aftthruster=0, forethruster=0,
                 portengine=0,
                 stbdengine=0, portrudder=0, stbdrudder=0, iceload=0):
        self.simtime = simtime
        self.latitude = latitude
        self.longitude = longitude
        self.sog = sog * 1.944  ### this must be multiply by 1.944 to convert it to knot
        self.cog = cog
        self.heading = heading
        self.aftthruster = aftthruster
        self.forethruster = forethruster
        self.portengine = portengine
        self.stbdengine = stbdengine
        self.portrudder = portrudder
        self.stbdrudder = stbdrudder
        self.iceload = iceload

    ## Populate a CsvFile from the contents of a Python dictionary (dict)
    @classmethod
    def fromDict(cls, dict):
        # print(dict)
        # if not dict["SimTime"]:
        #     print(f"the server couldn't recive data at time {dict['SimTime']}")
        # print(dict["SimTime"])
        return cls(dict["SimTime"],
                   abs(dict["Lat"]), abs(dict["Long"]),
                   dict["SOG"], dict["COG"], dict["Heading"],
                   dict["Aft"], dict["Fore"],
                   dict["PortE"], dict["StbdE"],
                   dict["PortR"], dict["StbdR"],
                   dict["IceLoad"])


class CsvRowsOperator:
    def __init__(self):
        self.log_objects = []

    def read_file(self, filename):
        csv_reader = csv.reader(filename, delimiter=',', quotechar='|')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                self.log_objects.append(
                    CsvFile(float(row[0]), float(row[1]), abs(float(row[2])), float(row[3]), float(row[4]),
                            float(row[5]),
                            float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]),
                            float(row[11])))
                line_count += 1
        return self.log_objects
