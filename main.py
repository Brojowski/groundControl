import utility

sdData = open("./sd_test.txt", "r")
flightData = sdData.readline()

print(flightData, len(flightData))


def parseLine(line):
    qx = utility.hexToFloat(line[0:8])
    qy = utility.hexToFloat(line[8:16])
    qz = utility.hexToFloat(line[16:24])
    qw = utility.hexToFloat(line[24:32])
    z = utility.hexToFloat(line[32:40])
    flightState = utility.hexToInt(line[40:42])

    return DataPoint(Quat((qx,qy,qz,qw)), z, flightState)


class Quat(object):
    qx = 0
    qy = 0
    qz = 0
    qw = 0

    def __init__(self, tuple):
        self.qx = tuple[0]
        self.qy = tuple[1]
        self.qz = tuple[2]
        self.qw = tuple[3]

    def __str__(self):
        return 'q_x='+str(self.qx)+', q_y='+str(self.qy)+', q_z='+str(self.qz)+', q_w='+str(self.qw)


class DataPoint(object):
    quat = Quat((0, 0, 0, 0))
    z = 0
    flightState = 0

    def __init__(self, q, z, state):
        self.quat = q
        self.z = z
        self.flightState = state

    def __str__(self):
        return str(self.quat)+'\nz='+str(self.z)+'\nflightNode='+str(self.flightState)

print(parseLine(flightData))