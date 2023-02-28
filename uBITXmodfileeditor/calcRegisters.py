import math
CAL= 50000
BAND='20'
FVCO_nominal = 875000000
TARGET = 14097100

CLOCK = 25000000

# NB constants
C = 1048574

#MS constants
E = 0
F = 1

FVCO_MIN = 600000000
FVCO_MAX = 900000000
OMD_MIN = 6
OMD_MAX = 4028

DIVIDE_BY_4_REQ = 500000


reg2={  "600":  (32,234,0),
        "160":  (0,242,0),
        "80":   (0,123,0),
        "60":   (0,83,0),
        "40":   (0,61,0),
        "30":   (0,42,0),
        "20":   (0,29,0),
        "17":   (0,22,0),
        "15":   (0,19,0),
        "12":   (0,16,0),
        "10":   (0,13,0),
        "6":    (0,6,0),
        "4":    (0,4,0),
        "2":    (0,1,0)
        }

def calculateCalibratedFreq (targetFreq, cal):
    return(int(round(((-cal*targetFreq)/FVCO_nominal) + targetFreq,0)))

def getD_value (band):
    reg = reg2[band]
    MSP2 = (((reg[0] & 0xff)<<16) | ((reg[1] & 0xff)<<8) | (reg[2] &0xff))
    d = (MSP2+512)/128
    print('d=', d)

    return d

def calRegisters (fout, d):             # Out is list of registers
    #   initialize working values related to the R divider. Only needed on 600m band
    max_divideby4 = 0                   # by default R divider set to 1
    rx_div = 0
    r = 1

    if (fout < DIVIDE_BY_4_REQ):        # checking whether freq less than 500khz, if so need a divide by 4
        rx_div = 0x10                   # Only need the divider on the 600m band
        r = 2                           # multiplying freq by 2

    # msx_p1 = (128 * d) - 512

    fvco = d * r * fout                 # this gives us our target for the feedback divider (NBx)
    print('target fvco=', fvco)


    a = fvco // CLOCK
    remainder = fvco % CLOCK

    b_c = ((fvco - (a*CLOCK))/CLOCK)    # the integer part of the fmd calculation is "a"

    print("a=", a,  "b_c", b_c)

    #b_c = (int)(fmd - a   )    # this gives us the fractional part of the calculation


    b = (int)(b_c * C)
    print ('b=', b)

    print("check: Target=", fvco, " reverse=", (a+b/C) * CLOCK )

    manx_p1 = (int)(128 * a + math.floor(128 * b/C) - 512)
    msnx_p2 = 128 * b - C * math.floor((128 * b / C))
    manx_p3 = C

    reg37 = (manx_p1 >> 8) & 0xff
    reg38 = (manx_p1 & 0xff)

    reg39 = ((msnx_p2 >> 16) & 0x0f ) | ((manx_p3 >> 12) & 0xf0)
    reg40 = (msnx_p2 >> 8) &0xff
    reg41 = (msnx_p2 & 0xff)

    regs=(reg37,reg38, reg39, reg40, reg41)
    return(regs)





D =  getD_value(BAND)
print('D=', D)

FOUT = calculateCalibratedFreq (TARGET, CAL)


print (calRegisters(FOUT, D))