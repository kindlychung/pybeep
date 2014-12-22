import subprocess
from .sounds import beep_bytes, vibrate_bytes

class BeepInterface:
    """
    Parent class of all beeping classes
    """
    def __init__(self, sound):
        self.sound = sound

    def beep(self):
        """
        Make a beep sound
        """
        try:
            p = subprocess.Popen(["play", "-t", "mp3", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate(input=self.sound)
        except FileNotFoundError:
            print("You need to install sox first.")
            exit(0)

    def beepn(self, n):
        """
        Beep n times
        """
        for i in range(n):
            self.beep()


class PyBeep(BeepInterface):
    """
    Ordinary beep
    """
    def __init__(self):
        super().__init__(beep_bytes)


class PyVibrate(BeepInterface):
    """
    Beep with vibration sound effect
    """
    def __init__(self):
        super().__init__(vibrate_bytes)

