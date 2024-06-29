from tkinter import *

renk = ["White","Black", "White","White","brown", "Blue", "Red","Green" ,"White","Magenta","White","White"]
resimler = ["up","down","left","right"]
butonlarim=[]
w = 5
h = 2
basti=0
bos=""
bos1=""
bos2=""
def secilenok(cercevebtn,basilanok):
        global basti,renkk,bos,butonlar,bos1,bos2
        print(cercevebtn,basilanok)
        basti=1
        if(basilanok=="1" or basilanok=="21" or basilanok=="33" or basilanok=="34" or basilanok=="9" or basilanok=="25" or basilanok=="13" or basilanok=="42"):
                if(basilanok=="9" or basilanok=="25" or basilanok=="13" or basilanok=="42"):
                        for x in range(3):
                                yuzeyler[0].degisiklik(36,1,6)
                                yuzeyler[0].degisiklik(39,1,5)
                                yuzeyler[0].degisiklik(42,1,4)
                                yuzeyler[0].degisiklik(9,4,9)
                                yuzeyler[0].degisiklik(10,5,9)
                                yuzeyler[0].degisiklik(11,6,9)
                                yuzeyler[0].degisiklik(56,9,6)
                                yuzeyler[0].degisiklik(59,9,5)
                                yuzeyler[0].degisiklik(62,9,4)
                                yuzeyler[0].degisiklik(87,4,1)
                                yuzeyler[0].degisiklik(88,5,1)
                                yuzeyler[0].degisiklik(89,6,1)
                                bos=butonlarim[36]
                                bos1=butonlarim[39]
                                bos2=butonlarim[42]
                                butonlarim[36]=butonlarim[87]
                                butonlarim[39]=butonlarim[88]
                                butonlarim[42]=butonlarim[89]
                                butonlarim[87]=butonlarim[62]
                                butonlarim[88]=butonlarim[59]
                                butonlarim[89]=butonlarim[56]
                                butonlarim[62]=butonlarim[11]
                                butonlarim[59]=butonlarim[10]
                                butonlarim[56]=butonlarim[9]
                                butonlarim[11]=bos
                                butonlarim[10]=bos1
                                butonlarim[9]=bos2
                else:
                        yuzeyler[0].degisiklik(36,1,6)
                        yuzeyler[0].degisiklik(39,1,5)
                        yuzeyler[0].degisiklik(42,1,4)
                        yuzeyler[0].degisiklik(9,4,9)
                        yuzeyler[0].degisiklik(10,5,9)
                        yuzeyler[0].degisiklik(11,6,9)
                        yuzeyler[0].degisiklik(56,9,6)
                        yuzeyler[0].degisiklik(59,9,5)
                        yuzeyler[0].degisiklik(62,9,4)
                        yuzeyler[0].degisiklik(87,4,1)
                        yuzeyler[0].degisiklik(88,5,1)
                        yuzeyler[0].degisiklik(89,6,1)
                        bos=butonlarim[36]
                        bos1=butonlarim[39]
                        bos2=butonlarim[42]
                        butonlarim[36]=butonlarim[87]
                        butonlarim[39]=butonlarim[88]
                        butonlarim[42]=butonlarim[89]
                        butonlarim[87]=butonlarim[62]
                        butonlarim[88]=butonlarim[59]
                        butonlarim[89]=butonlarim[56]
                        butonlarim[62]=butonlarim[11]
                        butonlarim[59]=butonlarim[10]
                        butonlarim[56]=butonlarim[9]
                        butonlarim[11]=bos
                        butonlarim[10]=bos1
                        butonlarim[9]=bos2

        elif(basilanok=="2" or basilanok=="20" or basilanok=="35" or basilanok=="32" or basilanok=="8" or basilanok=="14" or basilanok=="41" or basilanok=="26"):
                if(basilanok=="8" or basilanok=="14" or basilanok=="41" or basilanok=="26"):
                        for x in range(3):
                                yuzeyler[0].degisiklik(37,2,6)
                                yuzeyler[0].degisiklik(40,2,5)
                                yuzeyler[0].degisiklik(43,2,4)
                                yuzeyler[0].degisiklik(12,4,8)
                                yuzeyler[0].degisiklik(13,5,8)
                                yuzeyler[0].degisiklik(14,6,8)
                                yuzeyler[0].degisiklik(55,8,6)
                                yuzeyler[0].degisiklik(58,8,5)
                                yuzeyler[0].degisiklik(61,8,4)
                                yuzeyler[0].degisiklik(84,4,2)
                                yuzeyler[0].degisiklik(85,5,2)
                                yuzeyler[0].degisiklik(86,6,2)
                                bos=butonlarim[37]
                                bos1=butonlarim[40]
                                bos2=butonlarim[43]
                                butonlarim[37]=butonlarim[84]
                                butonlarim[40]=butonlarim[85]
                                butonlarim[43]=butonlarim[86]
                                butonlarim[84]=butonlarim[61]
                                butonlarim[85]=butonlarim[58]
                                butonlarim[86]=butonlarim[55]
                                butonlarim[61]=butonlarim[14]
                                butonlarim[58]=butonlarim[13]
                                butonlarim[55]=butonlarim[12]
                                butonlarim[14]=bos
                                butonlarim[13]=bos1
                                butonlarim[12]=bos2
                else:
                        yuzeyler[0].degisiklik(37,2,6)
                        yuzeyler[0].degisiklik(40,2,5)
                        yuzeyler[0].degisiklik(43,2,4)
                        yuzeyler[0].degisiklik(12,4,8)
                        yuzeyler[0].degisiklik(13,5,8)
                        yuzeyler[0].degisiklik(14,6,8)
                        yuzeyler[0].degisiklik(55,8,6)
                        yuzeyler[0].degisiklik(58,8,5)
                        yuzeyler[0].degisiklik(61,8,4)
                        yuzeyler[0].degisiklik(84,4,2)
                        yuzeyler[0].degisiklik(85,5,2)
                        yuzeyler[0].degisiklik(86,6,2)
                        bos=butonlarim[37]
                        bos1=butonlarim[40]
                        bos2=butonlarim[43]
                        butonlarim[37]=butonlarim[84]
                        butonlarim[40]=butonlarim[85]
                        butonlarim[43]=butonlarim[86]
                        butonlarim[84]=butonlarim[61]
                        butonlarim[85]=butonlarim[58]
                        butonlarim[86]=butonlarim[55]
                        butonlarim[61]=butonlarim[14]
                        butonlarim[58]=butonlarim[13]
                        butonlarim[55]=butonlarim[12]
                        butonlarim[14]=bos
                        butonlarim[13]=bos1
                        butonlarim[12]=bos2

        elif(basilanok=="3" or basilanok=="19" or basilanok=="36" or basilanok=="31" or basilanok=="7" or basilanok=="15" or basilanok=="27" or basilanok=="40"):
                if(basilanok=="7" or basilanok=="15" or basilanok=="27" or basilanok=="40"):
                        for x in range(3):
                                yuzeyler[0].degisiklik(38,3,6)
                                yuzeyler[0].degisiklik(41,3,5)
                                yuzeyler[0].degisiklik(44,3,4)
                                yuzeyler[0].degisiklik(15,4,7)
                                yuzeyler[0].degisiklik(16,5,7)
                                yuzeyler[0].degisiklik(17,6,7)
                                yuzeyler[0].degisiklik(54,7,6)
                                yuzeyler[0].degisiklik(57,7,5)
                                yuzeyler[0].degisiklik(60,7,4)
                                yuzeyler[0].degisiklik(81,4,3)
                                yuzeyler[0].degisiklik(82,5,3)
                                yuzeyler[0].degisiklik(83,6,3)
                                bos=butonlarim[38]
                                bos1=butonlarim[41]
                                bos2=butonlarim[44]
                                butonlarim[38]=butonlarim[81]
                                butonlarim[41]=butonlarim[82]
                                butonlarim[44]=butonlarim[83]
                                butonlarim[81]=butonlarim[60]
                                butonlarim[82]=butonlarim[57]
                                butonlarim[83]=butonlarim[54]
                                butonlarim[60]=butonlarim[17]
                                butonlarim[57]=butonlarim[16]
                                butonlarim[54]=butonlarim[15]
                                butonlarim[17]=bos
                                butonlarim[16]=bos1
                                butonlarim[15]=bos2
                else:
                        yuzeyler[0].degisiklik(38,3,6)
                        yuzeyler[0].degisiklik(41,3,5)
                        yuzeyler[0].degisiklik(44,3,4)
                        yuzeyler[0].degisiklik(15,4,7)
                        yuzeyler[0].degisiklik(16,5,7)
                        yuzeyler[0].degisiklik(17,6,7)
                        yuzeyler[0].degisiklik(54,7,6)
                        yuzeyler[0].degisiklik(57,7,5)
                        yuzeyler[0].degisiklik(60,7,4)
                        yuzeyler[0].degisiklik(81,4,3)
                        yuzeyler[0].degisiklik(82,5,3)
                        yuzeyler[0].degisiklik(83,6,3)
                        bos=butonlarim[38]
                        bos1=butonlarim[41]
                        bos2=butonlarim[44]
                        butonlarim[38]=butonlarim[81]
                        butonlarim[41]=butonlarim[82]
                        butonlarim[44]=butonlarim[83]
                        butonlarim[81]=butonlarim[60]
                        butonlarim[82]=butonlarim[57]
                        butonlarim[83]=butonlarim[54]
                        butonlarim[60]=butonlarim[17]
                        butonlarim[57]=butonlarim[16]
                        butonlarim[54]=butonlarim[15]
                        butonlarim[17]=bos
                        butonlarim[16]=bos1
                        butonlarim[15]=bos2

                        
        elif(basilanok=="4" or basilanok=="24" or basilanok=="12" or basilanok=="16"):
                if(basilanok=="12" or basilanok=="16"):
                        for x in range(3):
                                yuzeyler[1].degisiklik(9,4,12)
                                yuzeyler[1].degisiklik(12,5,12)
                                yuzeyler[1].degisiklik(15,6,12)
                                yuzeyler[5].degisiklik(45,1,4)
                                yuzeyler[5].degisiklik(48,2,4)
                                yuzeyler[5].degisiklik(51,3,4)
                                yuzeyler[9].degisiklik(81,4,4)
                                yuzeyler[9].degisiklik(84,5,4)
                                yuzeyler[9].degisiklik(87,6,4)
                                yuzeyler[7].degisiklik(65,7,4)
                                yuzeyler[7].degisiklik(68,8,4)
                                yuzeyler[7].degisiklik(71,9,4)
                                bos=butonlarim[9]
                                bos1=butonlarim[12]
                                bos2=butonlarim[15]
                                butonlarim[9]=butonlarim[45]
                                butonlarim[12]=butonlarim[48]
                                butonlarim[15]=butonlarim[51]
                                butonlarim[45]=butonlarim[81]
                                butonlarim[48]=butonlarim[84]
                                butonlarim[51]=butonlarim[87]
                                butonlarim[81]=butonlarim[65]
                                butonlarim[84]=butonlarim[68]
                                butonlarim[87]=butonlarim[71]
                                butonlarim[65]=bos
                                butonlarim[68]=bos1
                                butonlarim[71]=bos2
                else:
                        yuzeyler[1].degisiklik(9,4,12)
                        yuzeyler[1].degisiklik(12,5,12)
                        yuzeyler[1].degisiklik(15,6,12)
                        yuzeyler[5].degisiklik(45,1,4)
                        yuzeyler[5].degisiklik(48,2,4)
                        yuzeyler[5].degisiklik(51,3,4)
                        yuzeyler[9].degisiklik(81,4,4)
                        yuzeyler[9].degisiklik(84,5,4)
                        yuzeyler[9].degisiklik(87,6,4)
                        yuzeyler[7].degisiklik(65,7,4)
                        yuzeyler[7].degisiklik(68,8,4)
                        yuzeyler[7].degisiklik(71,9,4)
                        bos=butonlarim[9]
                        bos1=butonlarim[12]
                        bos2=butonlarim[15]
                        butonlarim[9]=butonlarim[45]
                        butonlarim[12]=butonlarim[48]
                        butonlarim[15]=butonlarim[51]
                        butonlarim[45]=butonlarim[81]
                        butonlarim[48]=butonlarim[84]
                        butonlarim[51]=butonlarim[87]
                        butonlarim[81]=butonlarim[65]
                        butonlarim[84]=butonlarim[68]
                        butonlarim[87]=butonlarim[71]
                        butonlarim[65]=bos
                        butonlarim[68]=bos1
                        butonlarim[71]=bos2

        elif(basilanok=="5" or basilanok=="23" or basilanok=="11" or basilanok=="17"):
                if(basilanok=="11" or basilanok=="17"):
                        for x in range(3):
                                yuzeyler[1].degisiklik(10,4,11)
                                yuzeyler[1].degisiklik(13,5,11)
                                yuzeyler[1].degisiklik(16,6,11)
                                yuzeyler[5].degisiklik(46,1,5)
                                yuzeyler[5].degisiklik(49,2,5)
                                yuzeyler[5].degisiklik(52,3,5)
                                yuzeyler[9].degisiklik(82,4,5)
                                yuzeyler[9].degisiklik(85,5,5)
                                yuzeyler[9].degisiklik(88,6,5)
                                yuzeyler[7].degisiklik(64,7,5)
                                yuzeyler[7].degisiklik(67,8,5)
                                yuzeyler[7].degisiklik(70,9,5)
                                bos=butonlarim[10]
                                bos1=butonlarim[13]
                                bos2=butonlarim[16]
                                butonlarim[10]=butonlarim[46]
                                butonlarim[13]=butonlarim[49]
                                butonlarim[16]=butonlarim[52]
                                butonlarim[46]=butonlarim[82]
                                butonlarim[49]=butonlarim[85]
                                butonlarim[52]=butonlarim[88]
                                butonlarim[82]=butonlarim[64]
                                butonlarim[85]=butonlarim[67]
                                butonlarim[88]=butonlarim[70]
                                butonlarim[64]=bos
                                butonlarim[67]=bos1
                                butonlarim[70]=bos2
                else:
                        yuzeyler[1].degisiklik(10,4,11)
                        yuzeyler[1].degisiklik(13,5,11)
                        yuzeyler[1].degisiklik(16,6,11)
                        yuzeyler[5].degisiklik(46,1,5)
                        yuzeyler[5].degisiklik(49,2,5)
                        yuzeyler[5].degisiklik(52,3,5)
                        yuzeyler[9].degisiklik(82,4,5)
                        yuzeyler[9].degisiklik(85,5,5)
                        yuzeyler[9].degisiklik(88,6,5)
                        yuzeyler[7].degisiklik(64,7,5)
                        yuzeyler[7].degisiklik(67,8,5)
                        yuzeyler[7].degisiklik(70,9,5)
                        bos=butonlarim[10]
                        bos1=butonlarim[13]
                        bos2=butonlarim[16]
                        butonlarim[10]=butonlarim[46]
                        butonlarim[13]=butonlarim[49]
                        butonlarim[16]=butonlarim[52]
                        butonlarim[46]=butonlarim[82]
                        butonlarim[49]=butonlarim[85]
                        butonlarim[52]=butonlarim[88]
                        butonlarim[82]=butonlarim[64]
                        butonlarim[85]=butonlarim[67]
                        butonlarim[88]=butonlarim[70]
                        butonlarim[64]=bos
                        butonlarim[67]=bos1
                        butonlarim[70]=bos2

        elif(basilanok=="6" or basilanok=="22" or basilanok=="10" or basilanok=="18"):
                if(basilanok=="10" or basilanok=="18"):
                        for x in range(3):
                                yuzeyler[1].degisiklik(11,4,10)
                                yuzeyler[1].degisiklik(14,5,10)
                                yuzeyler[1].degisiklik(17,6,10)
                                yuzeyler[5].degisiklik(63,7,6)
                                yuzeyler[5].degisiklik(66,8,6)
                                yuzeyler[5].degisiklik(69,9,6)
                                yuzeyler[9].degisiklik(83,4,6)
                                yuzeyler[9].degisiklik(86,5,6)
                                yuzeyler[9].degisiklik(89,6,6)
                                yuzeyler[7].degisiklik(47,1,6)
                                yuzeyler[7].degisiklik(50,2,6)
                                yuzeyler[7].degisiklik(53,3,6)
                                bos=butonlarim[11]
                                bos1=butonlarim[14]
                                bos2=butonlarim[17]
                                butonlarim[11]=butonlarim[47]
                                butonlarim[14]=butonlarim[50]
                                butonlarim[17]=butonlarim[53]
                                butonlarim[47]=butonlarim[83]
                                butonlarim[50]=butonlarim[86]
                                butonlarim[53]=butonlarim[89]
                                butonlarim[83]=butonlarim[63]
                                butonlarim[86]=butonlarim[66]
                                butonlarim[89]=butonlarim[69]
                                butonlarim[63]=bos
                                butonlarim[66]=bos1
                                butonlarim[69]=bos2
                else:
                        yuzeyler[1].degisiklik(11,4,10)
                        yuzeyler[1].degisiklik(14,5,10)
                        yuzeyler[1].degisiklik(17,6,10)
                        yuzeyler[5].degisiklik(63,7,6)
                        yuzeyler[5].degisiklik(66,8,6)
                        yuzeyler[5].degisiklik(69,9,6)
                        yuzeyler[9].degisiklik(83,4,6)
                        yuzeyler[9].degisiklik(86,5,6)
                        yuzeyler[9].degisiklik(89,6,6)
                        yuzeyler[7].degisiklik(47,1,6)
                        yuzeyler[7].degisiklik(50,2,6)
                        yuzeyler[7].degisiklik(53,3,6)
                        bos=butonlarim[11]
                        bos1=butonlarim[14]
                        bos2=butonlarim[17]
                        butonlarim[11]=butonlarim[47]
                        butonlarim[14]=butonlarim[50]
                        butonlarim[17]=butonlarim[53]
                        butonlarim[47]=butonlarim[83]
                        butonlarim[50]=butonlarim[86]
                        butonlarim[53]=butonlarim[89]
                        butonlarim[83]=butonlarim[63]
                        butonlarim[86]=butonlarim[66]
                        butonlarim[89]=butonlarim[69]
                        butonlarim[63]=bos
                        butonlarim[66]=bos1
                        butonlarim[69]=bos2

        elif(basilanok=="28" or basilanok=="37"):
                if(basilanok=="37"):
                        for x in range(3):
                                yuzeyler[1].degisiklik(36,4,10)
                                yuzeyler[1].degisiklik(37,4,11)
                                yuzeyler[1].degisiklik(38,4,12)
                                yuzeyler[5].degisiklik(45,4,1)
                                yuzeyler[5].degisiklik(46,4,2)
                                yuzeyler[5].degisiklik(47,4,3)
                                yuzeyler[9].degisiklik(54,4,4)
                                yuzeyler[9].degisiklik(55,4,5)
                                yuzeyler[9].degisiklik(56,4,6)
                                yuzeyler[7].degisiklik(63,4,7)
                                yuzeyler[7].degisiklik(64,4,8)
                                yuzeyler[7].degisiklik(65,4,9)
                                bos=butonlarim[36]
                                bos1=butonlarim[37]
                                bos2=butonlarim[38]
                                butonlarim[36]=butonlarim[45]
                                butonlarim[37]=butonlarim[46]
                                butonlarim[38]=butonlarim[47]
                                butonlarim[45]=butonlarim[54]
                                butonlarim[46]=butonlarim[55]
                                butonlarim[47]=butonlarim[56]
                                butonlarim[54]=butonlarim[63]
                                butonlarim[55]=butonlarim[64]
                                butonlarim[56]=butonlarim[65]
                                butonlarim[63]=bos
                                butonlarim[64]=bos1
                                butonlarim[65]=bos2

                else:
                        yuzeyler[1].degisiklik(36,4,10)
                        yuzeyler[1].degisiklik(37,4,11)
                        yuzeyler[1].degisiklik(38,4,12)
                        yuzeyler[5].degisiklik(45,4,1)
                        yuzeyler[5].degisiklik(46,4,2)
                        yuzeyler[5].degisiklik(47,4,3)
                        yuzeyler[9].degisiklik(54,4,4)
                        yuzeyler[9].degisiklik(55,4,5)
                        yuzeyler[9].degisiklik(56,4,6)
                        yuzeyler[7].degisiklik(63,4,7)
                        yuzeyler[7].degisiklik(64,4,8)
                        yuzeyler[7].degisiklik(65,4,9)
                        bos=butonlarim[36]
                        bos1=butonlarim[37]
                        bos2=butonlarim[38]
                        butonlarim[36]=butonlarim[45]
                        butonlarim[37]=butonlarim[46]
                        butonlarim[38]=butonlarim[47]
                        butonlarim[45]=butonlarim[54]
                        butonlarim[46]=butonlarim[55]
                        butonlarim[47]=butonlarim[56]
                        butonlarim[54]=butonlarim[63]
                        butonlarim[55]=butonlarim[64]
                        butonlarim[56]=butonlarim[65]
                        butonlarim[63]=bos
                        butonlarim[64]=bos1
                        butonlarim[65]=bos2

        elif(basilanok=="29" or basilanok=="38"):
                if(basilanok=="38"):
                        for x in range(3):
                                yuzeyler[1].degisiklik(39,5,10)
                                yuzeyler[1].degisiklik(40,5,11)
                                yuzeyler[1].degisiklik(41,5,12)
                                yuzeyler[5].degisiklik(48,5,1)
                                yuzeyler[5].degisiklik(49,5,2)
                                yuzeyler[5].degisiklik(50,5,3)
                                yuzeyler[9].degisiklik(57,5,4)
                                yuzeyler[9].degisiklik(58,5,5)
                                yuzeyler[9].degisiklik(59,5,6)
                                yuzeyler[7].degisiklik(66,5,7)
                                yuzeyler[7].degisiklik(67,5,8)
                                yuzeyler[7].degisiklik(68,5,9)
                                bos=butonlarim[39]
                                bos1=butonlarim[40]
                                bos2=butonlarim[41]
                                butonlarim[39]=butonlarim[48]
                                butonlarim[40]=butonlarim[49]
                                butonlarim[41]=butonlarim[50]
                                butonlarim[48]=butonlarim[57]
                                butonlarim[49]=butonlarim[58]
                                butonlarim[50]=butonlarim[59]
                                butonlarim[57]=butonlarim[66]
                                butonlarim[58]=butonlarim[67]
                                butonlarim[59]=butonlarim[68]
                                butonlarim[66]=bos
                                butonlarim[67]=bos1
                                butonlarim[68]=bos2

                else:
                        yuzeyler[1].degisiklik(39,5,10)
                        yuzeyler[1].degisiklik(40,5,11)
                        yuzeyler[1].degisiklik(41,5,12)
                        yuzeyler[5].degisiklik(48,5,1)
                        yuzeyler[5].degisiklik(49,5,2)
                        yuzeyler[5].degisiklik(50,5,3)
                        yuzeyler[9].degisiklik(57,5,4)
                        yuzeyler[9].degisiklik(58,5,5)
                        yuzeyler[9].degisiklik(59,5,6)
                        yuzeyler[7].degisiklik(66,5,7)
                        yuzeyler[7].degisiklik(67,5,8)
                        yuzeyler[7].degisiklik(68,5,9)
                        bos=butonlarim[39]
                        bos1=butonlarim[40]
                        bos2=butonlarim[41]
                        butonlarim[39]=butonlarim[48]
                        butonlarim[40]=butonlarim[49]
                        butonlarim[41]=butonlarim[50]
                        butonlarim[48]=butonlarim[57]
                        butonlarim[49]=butonlarim[58]
                        butonlarim[50]=butonlarim[59]
                        butonlarim[57]=butonlarim[66]
                        butonlarim[58]=butonlarim[67]
                        butonlarim[59]=butonlarim[68]
                        butonlarim[66]=bos
                        butonlarim[67]=bos1
                        butonlarim[68]=bos2

        elif(basilanok=="30" or basilanok=="39"):
                if(basilanok=="39"):
                        for x in range(3):
                                yuzeyler[1].degisiklik(42,6,10)
                                yuzeyler[1].degisiklik(43,6,11)
                                yuzeyler[1].degisiklik(44,6,12)
                                yuzeyler[5].degisiklik(51,6,1)
                                yuzeyler[5].degisiklik(52,6,2)
                                yuzeyler[5].degisiklik(53,6,3)
                                yuzeyler[9].degisiklik(60,6,4)
                                yuzeyler[9].degisiklik(61,6,5)
                                yuzeyler[9].degisiklik(62,6,6)
                                yuzeyler[7].degisiklik(69,6,7)
                                yuzeyler[7].degisiklik(70,6,8)
                                yuzeyler[7].degisiklik(71,6,9)
                                bos=butonlarim[42]
                                bos1=butonlarim[43]
                                bos2=butonlarim[44]
                                butonlarim[42]=butonlarim[51]
                                butonlarim[43]=butonlarim[52]
                                butonlarim[44]=butonlarim[53]
                                butonlarim[51]=butonlarim[60]
                                butonlarim[52]=butonlarim[61]
                                butonlarim[53]=butonlarim[62]
                                butonlarim[60]=butonlarim[69]
                                butonlarim[61]=butonlarim[70]
                                butonlarim[62]=butonlarim[71]
                                butonlarim[69]=bos
                                butonlarim[70]=bos1
                                butonlarim[71]=bos2

                else:
                        yuzeyler[1].degisiklik(42,6,10)
                        yuzeyler[1].degisiklik(43,6,11)
                        yuzeyler[1].degisiklik(44,6,12)
                        yuzeyler[5].degisiklik(51,6,1)
                        yuzeyler[5].degisiklik(52,6,2)
                        yuzeyler[5].degisiklik(53,6,3)
                        yuzeyler[9].degisiklik(60,6,4)
                        yuzeyler[9].degisiklik(61,6,5)
                        yuzeyler[9].degisiklik(62,6,6)
                        yuzeyler[7].degisiklik(69,6,7)
                        yuzeyler[7].degisiklik(70,6,8)
                        yuzeyler[7].degisiklik(71,6,9)
                        bos=butonlarim[42]
                        bos1=butonlarim[43]
                        bos2=butonlarim[44]
                        butonlarim[42]=butonlarim[51]
                        butonlarim[43]=butonlarim[52]
                        butonlarim[44]=butonlarim[53]
                        butonlarim[51]=butonlarim[60]
                        butonlarim[52]=butonlarim[61]
                        butonlarim[53]=butonlarim[62]
                        butonlarim[60]=butonlarim[69]
                        butonlarim[61]=butonlarim[70]
                        butonlarim[62]=butonlarim[71]
                        butonlarim[69]=bos
                        butonlarim[70]=bos1
                        butonlarim[71]=bos2

def ilksatirsutun():
        for _ in range(1,13):
                ust=Button(form, bg = renk[0], fg = "Black",command=lambda n="üst" ,m=str(_): secilenok(n,m),text = str(_),width = w, height = h).grid(row=0, column=_)
                alt=Button(form, bg = renk[0], fg = "Black", command=lambda n="alt" ,m=str(_+12): secilenok(n,m),text = str(_+12),width = w, height = h).grid(row=10, column=_)
                
        for _ in range(1,10):
                sol=Button(form, bg = renk[0], fg = "Black",command=lambda n="sol" ,m=str(_+24): secilenok(n,m) ,text = str(_+24),width = w, height = h).grid(row=_, column=0)
                sag=Button(form, bg = renk[0], fg = "Black",command=lambda n="sag" ,m=str(_+33): secilenok(n,m) ,text = str(_+33),width = w, height = h).grid(row=_, column=13)
                
def degistir(listem, listem1):
        bos = listem[3]
        for x in [2,1,0]:
                listem[x+1] = listem[x]
        listem[3]=bos


class yuzey():
        global butonlarim
        def __init__(self,base,renk,konum):
                self.renk = renk
                self.base = base 
                self.boyut = 3
                self.konum = konum
                self.liste = []
                
        def sat_sut_al(self, numara):
                if numara in [0,1,2]:
                        sonuc = [self.liste[x] for x in range(9) if x%3 == numara]
                else:
                        sonuc = [self.liste[x] for x in range(9) if int(x/3) + 3 == numara]
                        
                        #print("snc",sonuc,"nmr",numara)
                        
                        
                return (sonuc)          
                
        

        def dugme_yap(self,numara):
                global butonlarım
                self.kare = Button(self.base, bg = self.renk, fg = "Yellow", text = str(numara),width = 5, height = 2)
                #print(self.kare,"Butonun Konumu",self.konum) #Renkli bölgeler de bulunan 9 butonun bölge numaralarını verir.
                butonlarim.append(self.kare)
                return self.kare

        def yerlestir(self):
                        for sat in range(self.boyut):
                                for sut in range(self.boyut):
                                        #print(str(sat*self.boyut+sut))
                                        self.liste[sat*self.boyut+sut].grid(row=int(self.konum/4)*self.boyut+sat+1, column = int(self.konum%4)*self.boyut+sut+1)

        def olustur(self):
                for x in range(self.boyut**2):
                        self.liste.append(self.dugme_yap(x))
                self.yerlestir()

        def degisiklik(self,sayi,satir,sutun):
                self.butons=butonlarim[sayi].grid(row=satir, column =sutun)
                

yuzeyler = []

form = Tk()
form.geometry("1000x1000+100+100")
form.title("Rubik Küpü")
oklar = []
for resim in resimler:
        oklar.append(PhotoImage(file = resim+".png"))

#resim = PhotoImage(file = "up.png")
for _ in range(12):
        ### ya böyle
        
        yuzeyler.append(yuzey(form,renk[_],_))
        yuzeyler[_].olustur()
        
        ### ya da böyle
        #yuzeyler.append(yuzey(form,renk[_],_).olustur())
ilksatirsutun()

yzy = [4,1,6,9]
stlr = [0,3,2,5]
etly = [7,0,3,2,5]

listem = []
listem1 = []
for x in range(4):
        listem.append(yuzeyler[yzy[x]].sat_sut_al(stlr[x]))
        listem1.append(yuzeyler[etly[0]].sat_sut_al(x+1))

#degistir(listem, listem1)

#print(listem)
#print(listem1)

#x = list(reversed(listem[0]))

#print(x)
#print(listem[0][0])

mainloop()












"""
class satir(kare):
        def __init__(self):
                self.boyut = 3
                self.kareler = [kare]*self.boyut

        def olustur(self,kareler):
                for kare in self.kareler:
                        kare.


class rubik(yuzey):
        def __init__(self):
                self.kare = dugme
"""     



