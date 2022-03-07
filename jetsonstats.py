# Add to nvidia

from jtop import jtop


if __name__ == "__main__":

    print("Simple jtop reader")

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        while jetson.ok():
            # Read tegra stats
            print(jetson.stats)
# EOF


from jtop import jtop


if __name__ == "__main__":

    print("All accessible jtop properities")

    with jtop() as jetson:
        # boards
        print('*** board ***')
        print(jetson.board)
        # jetson.ok() will provide the proper update frequency
        while jetson.ok():
            # CPU
            print('*** CPUs ***')
            print(jetson.cpu)
            # GPU
            print('*** GPU ***')
            print(jetson.gpu)
            # Engines
            print('*** engine ***')
            print(jetson.engine)
            # nvpmodel
            print('*** NV Power Model ***')
            print(jetson.nvpmodel)
            # jetson_clocks
            print('*** jetson_clocks ***')
            print(jetson.jetson_clocks)
            # Status disk
            print('*** disk ***')
            print(jetson.disk)
            # Status fans
            print('*** fan ***')
            print(jetson.fan)
            # uptime
            print('*** uptime ***')
            print(jetson.uptime)
            # local interfaces
            print('*** local interfaces ***')
            print(jetson.local_interfaces)
            # Temperature
            print('*** temperature ***')
            print(jetson.temperature)
            # Power
            print('*** power ***')
            print(jetson.power)
            # EMC
            print('*** emc ***')
            print(jetson.emc)
            # IRAM
            print('*** ram ***')
            print(jetson.ram)
            # IRAM
            print('*** iram ***')
            print(jetson.iram)
            # MTS
            print('*** mts ***')
            print(jetson.mts)
#             add pulsar send for each json file
# EOF
