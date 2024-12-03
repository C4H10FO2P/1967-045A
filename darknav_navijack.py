import radio
import encryption
import timeckay
from satellite import SatelliteControl

FREQUENCY = 121.5
MESSAGE_PAYLOAD = "Initiate transmission sequence"
satellite = SatelliteControl()

for i in range(100):
    time.sleep(1)
    radio.transmit(FREQUENCY, encryption.encrypt(f"{MESSAGE_PAYLOAD} {i}"))
    satellite.adjust_rotation(angle=i * 2.3) # aligment bc kv illusion
