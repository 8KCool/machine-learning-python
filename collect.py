import cv2
import os
import time
import json
import numpy as np

from suiron.core.SuironIO import SuironIO

# Load image settings
with open('settings.json') as d:
    SETTINGS = json.load(d)

# Instantiatees our IO class
suironio = SuironIO(width=SETTINGS['width'], height=SETTINGS['height'], depth=SETTINGS['depth'])
suironio.init_saving()

# Allows time for the camerae to warm up
print('Warming up...')
#time.sleep(3)

print('Recording data...')
for i in range(60):
    suironio.record_inputs()

print('Saving file...')
suironio.save_inputs()