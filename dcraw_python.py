"""
Author: Max Chen
E-mail: max.chen.l.w@gmail.com
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import subprocess
import imageio.v3 as iio

path = 'test.CR2'

dcraw_command = [
    "dcraw", "-v", "-4", "-T", path
]

try:
    subprocess.run(dcraw_command, check=True)
    print("dcraw command executed successfully！")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing the dcraw command: {e}")
except FileNotFoundError:
    print("The dcraw executable was not found, please make sure dcraw is installed and configured in the system path.")

# show result
rgb = iio.imread('test.tiff')
plt.figure(figsize=(8, 5))
plt.imshow(rgb/(2**16)) #The image is saved as 16-bit, normalization is required
plt.title('Result')
plt.axis('off')

plt.show()