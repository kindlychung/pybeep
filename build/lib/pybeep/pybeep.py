import subprocess
from .sounds import beep_bytes, vibrate_bytes

class BeepInterface:
    def __init__(self, sound):
        self.sound = sound

    def beep(self):
        try:
            p = subprocess.Popen(["play", "-t", "mp3", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate(input=self.sound)
        except FileNotFoundError:
            print("You need to install sox first.")
            exit(0)


class PyBeep(BeepInterface):
    def __init__(self):
        super().__init__(beep_bytes)


class PyVibrate(BeepInterface):
    def __init__(self):
        super().__init__(vibrate_bytes)

