# Demo for Vissim+
# This demo is programmed to verified the COM interface of Vissim.
# 2017.1.16
# silverHugh

import win32com.client as com
import os

class Vissim():
    def __init__(self):
        pass

    def open(self):
        self.Vissim = com.Dispatch("Vissim.Vissim-64.700")

    def close(self):
        if self.Vissim is not None:
            self.Vissim = None

    def loadNet(self, netPath, additive = False):
        self.Vissim.LoadNet(netPath, additive)

    def loadLayout(self, layoutPath):
        self.Vissim.loadLayout(layoutPath)

    def run(self, mode="continuous"):
        if mode == "step":
            self.Vissim.Simulation.RunSingleStep()
        else:
            self.Vissim.Simulation.RunContinuous()


def main():
    try:
        vissim = Vissim()
        vissim.open()

        cwd = os.getcwd()
        vissim.loadNet(os.path.join(cwd, 'COM_example.inpx'))

        vissim.loadLayout(os.path.join(cwd, 'COM_example.layx'))

        vissim.run()

        input()
    except KeyboardInterrupt:
        print("[!] Interrupted")
    finally:
        if vissim is not None:
            vissim.close()
        print("[-] Bye~")


if __name__ == "__main__":
    main()