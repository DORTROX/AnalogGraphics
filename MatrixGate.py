import time
import os

Gif = [
"-","-","-","-","-","-","-","-","-","-","-","-",
"\n",
"-",".",".",".",".",".",".",".",".",".",".","-",
"\n",
"-",".",".",".",".",".",".",".",".",".",".","-",
"\n",
"-",".","."," "," "," "," "," "," ",".",".","-",
"\n",
"-",".","."," "," "," "," "," "," ",".",".","-",
"\n",
"-",".","."," "," "," "," "," "," ",".",".","-",
"\n",
"-",".","."," "," "," "," "," "," ",".",".","-",
"\n",
"-",".",".",".",".",".",".",".",".",".",".","-",
"\n",
"-",".",".",".",".",".",".",".",".",".",".","-",
"\n",
"-","-","-","-","-","-","-","-","-","-","-","-",
"\n"
]

maincount = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if(maincount > 3):
        maincount = 0
    if (maincount == 0):
        anim1 = Gif[0] = Gif[1] = Gif[2] = Gif[3] = Gif[4] = Gif[5] = Gif[6] = Gif[7] = Gif[8] = Gif[9] = Gif[10] = Gif[11] = Gif[13] = Gif[24] = Gif[26] = Gif[37] = Gif[39] = Gif[50] = Gif[52] = Gif[63] = Gif[65] = Gif[76] = Gif[78] = Gif[89] = Gif[91] = Gif[102] = Gif[104] = Gif[115] = Gif[117] = Gif[118] = Gif[119] = Gif[120] = Gif[121] = Gif[122] = Gif[123] = Gif[124] = Gif[125] = Gif[126] = Gif[127] = Gif[128] = "-"

        anim2 = Gif[14] = Gif[15] = Gif[16] = Gif[17] = Gif[18] = Gif[19] = Gif[20] = Gif[21] = Gif[22] = Gif[23]= Gif[27] = Gif[40] = Gif[53] = Gif[66] = Gif[79] = Gif[92] = Gif[105] = Gif[36] = Gif[49] = Gif[62] = Gif[75] = Gif[88] = Gif[101] =  Gif[106] = Gif[107] = Gif[108] = Gif[109] = Gif[110] = Gif[111] = Gif[112] = Gif[113] = Gif[114] = "@"

        anim3 = Gif[28] = Gif[41] = Gif[54] = Gif[67] = Gif[80] = Gif[93] = Gif[35] = Gif[48] = Gif[61] = Gif[74] = Gif[87] = Gif[29] = Gif[30] = Gif[31] = Gif[32] = Gif[33] = Gif[34] = Gif[93] = Gif[94] = Gif[95] = Gif[96] = Gif[97] = Gif[98] = Gif[99] = Gif[100] = "&"

    elif (maincount == 1): 
        anim1 = Gif[0] = Gif[1] = Gif[2] = Gif[3] = Gif[4] = Gif[5] = Gif[6] = Gif[7] = Gif[8] = Gif[9] = Gif[10] = Gif[11] = Gif[13] = Gif[24] = Gif[26] = Gif[37] = Gif[39] = Gif[50] = Gif[52] = Gif[63] = Gif[65] = Gif[76] = Gif[78] = Gif[89] = Gif[91] = Gif[102] = Gif[104] = Gif[115] = Gif[117] = Gif[118] = Gif[119] = Gif[120] = Gif[121] = Gif[122] = Gif[123] = Gif[124] = Gif[125] = Gif[126] = Gif[127] = Gif[128] = "@"

        anim2 = Gif[14] = Gif[15] = Gif[16] = Gif[17] = Gif[18] = Gif[19] = Gif[20] = Gif[21] = Gif[22] = Gif[23]= Gif[27] = Gif[40] = Gif[53] = Gif[66] = Gif[79] = Gif[92] = Gif[105] = Gif[36] = Gif[49] = Gif[62] = Gif[75] = Gif[88] = Gif[101] =  Gif[106] = Gif[107] = Gif[108] = Gif[109] = Gif[110] = Gif[111] = Gif[112] = Gif[113] = Gif[114] = "&"

        anim3 = Gif[28] = Gif[41] = Gif[54] = Gif[67] = Gif[80] = Gif[93] = Gif[35] = Gif[48] = Gif[61] = Gif[74] = Gif[87] = Gif[29] = Gif[30] = Gif[31] = Gif[32] = Gif[33] = Gif[34] = Gif[93] = Gif[94] = Gif[95] = Gif[96] = Gif[97] = Gif[98] = Gif[99] = Gif[100] = "-"

    elif (maincount == 2):
            anim1 = Gif[0] = Gif[1] = Gif[2] = Gif[3] = Gif[4] = Gif[5] = Gif[6] = Gif[7] = Gif[8] = Gif[9] = Gif[10] = Gif[11] = Gif[13] = Gif[24] = Gif[26] = Gif[37] = Gif[39] = Gif[50] = Gif[52] = Gif[63] = Gif[65] = Gif[76] = Gif[78] = Gif[89] = Gif[91] = Gif[102] = Gif[104] = Gif[115] = Gif[117] = Gif[118] = Gif[119] = Gif[120] = Gif[121] = Gif[122] = Gif[123] = Gif[124] = Gif[125] = Gif[126] = Gif[127] = Gif[128] = "&"

            anim2 = Gif[14] = Gif[15] = Gif[16] = Gif[17] = Gif[18] = Gif[19] = Gif[20] = Gif[21] = Gif[22] = Gif[23]= Gif[27] = Gif[40] = Gif[53] = Gif[66] = Gif[79] = Gif[92] = Gif[105] = Gif[36] = Gif[49] = Gif[62] = Gif[75] = Gif[88] = Gif[101] =  Gif[106] = Gif[107] = Gif[108] = Gif[109] = Gif[110] = Gif[111] = Gif[112] = Gif[113] = Gif[114] = "-"

            anim3 = Gif[28] = Gif[41] = Gif[54] = Gif[67] = Gif[80] = Gif[93] = Gif[35] = Gif[48] = Gif[61] = Gif[74] = Gif[87] = Gif[29] = Gif[30] = Gif[31] = Gif[32] = Gif[33] = Gif[34] = Gif[93] = Gif[94] = Gif[95] = Gif[96] = Gif[97] = Gif[98] = Gif[99] = Gif[100] = "@"
    maincount = maincount + 1
    for x in Gif:
        print(x, end="")
    time.sleep(0.4)