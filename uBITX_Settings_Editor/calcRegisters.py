import math

def buildWSPRRegs (TARGET, BAND, CAL):

    FVCO_nominal = 875000000


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


    reg2={  "600m":  (32,234,0),
            "160m":  (0,242,0),
            "80m":   (0,123,0),
            "60m":   (0,83,0),
            "40m":   (0,61,0),
            "30m":   (0,42,0),
            "20m":   (0,29,0),
            "17m":   (0,22,0),
            "15m":   (0,19,0),
            "12m":   (0,16,0),
            "10m":   (0,13,0),
            "6m":    (0,6,0),
            "4m":    (0,4,0),
            "2m":    (0,1,0)
            }

    reg3={  "600m": 14843,
            "160m":  3844,
            "80m":   1969,
            "60m":   1344,
            "40m":   1000,
            "30m":   687,
            "20m":   500,
            "17m":   375,
            "15m":   312,
            "12m":   281,
            "10m":   250,
            "6m":    125,
            "4m":    94,
            "2m":    62
            }

    def calculateCalibratedFreq (targetFreq, cal):
        return(int(round(((-cal*targetFreq)/FVCO_nominal) + targetFreq,0)))

    def getD_value (band):
        reg = reg2[band]

        MSP2 = (((reg[1] & 0xff)<<8) | (reg[2] &0xff))  # top 4 bits only used to specify "r". only needed on 600m. Handled as special case
        d = (MSP2+512)/128

        return d

    def calRegisters (fout, d, band):             # Out is list of registers
        #   except for 600m, r will always be 1
        r = 1

        if (band == "600m"):        # checking whether freq less than 500khz, if so need a divide by 4
            r = 4                           # multiplying freq by 2

        fvco = d * r * fout                 # this gives us our target for the feedback divider (NBx)


        a = fvco // CLOCK

        b_c = ((fvco - (a*CLOCK))/CLOCK)    # the integer part of the fmd calculation is "a"


        b = (int)(b_c * C)


        manx_p1 = (int)(128 * a + math.floor(128 * b/C) - 512)
        msnx_p2 = 128 * b - C * math.floor((128 * b / C))
        manx_p3 = C

        reg37 = (manx_p1 >> 8) & 0xff
        reg38 = (manx_p1 & 0xff)

        reg39 = ((msnx_p2 >> 16) & 0x0f ) | ((manx_p3 >> 12) & 0xf0)
        reg40 = (msnx_p2 >> 8) &0xff
        reg41 = (msnx_p2 & 0xff)

        reg1str ='{:02X}'.format(reg37) + "," + '{:02X}'.format(reg38) + "," + '{:02X}'.format(reg39) + "," + '{:02X}'.format(reg40) + "," + '{:02X}'.format(reg41)
        reg2str = '{:02X}'.format(reg2[band][0]) + "," '{:02X}'.format(reg2[band][1]) + "," '{:02X}'.format(reg2[band][2]) + ","
        reg3str = str(reg3[band])

        print(reg37, reg38, reg39, reg40, reg41)

        return([reg1str, reg2str, reg3str])


    #
    # Main part of function starts here
    #

    D =  getD_value(BAND)

    FOUT = calculateCalibratedFreq (TARGET, CAL)


    return(calRegisters(FOUT, D, BAND))

