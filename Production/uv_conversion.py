# Functions to generate meaningless UV sensor data (sinusoids) and to
# convert that data to the expected format

from math import sin
from random import randrange
from common_library import twos_comp, sine_generator

STEP_SIZE = 0.1
AMP_DIFF = 200


UVA_AMP = randrange(8000-AMP_DIFF, 8000+AMP_DIFF)
UVB_AMP = randrange(10000-AMP_DIFF, 10000+AMP_DIFF)
UVC1_AMP = randrange(3200-AMP_DIFF, 3200+AMP_DIFF)
UVC2_AMP = randrange(4700-AMP_DIFF, 4700+AMP_DIFF)
UVD_AMP = randrange(2000-AMP_DIFF, 2000+AMP_DIFF)


def sine_generator(step_size, amplitude):
    x = 0
    while True:
        yield amplitude + amplitude * sin(x)
        x += step_size


uva = sine_generator(STEP_SIZE, UVA_AMP)
uvb = sine_generator(STEP_SIZE, UVB_AMP)
uvc1 = sine_generator(STEP_SIZE, UVC1_AMP)
uvc2 = sine_generator(STEP_SIZE, UVC2_AMP)
uvd = sine_generator(STEP_SIZE, UVD_AMP)


def make_fake_uv():
    return next(uva), next(uvb), next(uvc1), next(uvc2), next(uvd)

def uv_conversion(uva, uvb, uvc1, uvc2, uvd):
    
    output = [0] * 10

    # Scale UVA data to a 16-bit resolution
    uva = twos_comp(int(uva))
    uvd = twos_comp(int(uvd))
    uvb = twos_comp(int(uvb))
    uvc1 = twos_comp(int(uvc1))
    uvc2 = twos_comp(int(uvc2))

    #Format into high and low bytes
    output[0:2] = divmod(uva, 256)
    output[2:4] = divmod(uvd, 256)
    output[4:6] = divmod(uvb, 256)
    output[6:8] = divmod(uvc1, 256)
    output[8:10] = divmod(uvc2, 256)

    return output
