from itertools import permutations
from itertools import product
import string
from enigma import m3  

#Possible Enigma settings
all_rotors = [ "I", "II", "III", "IV", "V" ]
all_reflectors = ["C", "B"] 
alphabet = string.ascii_uppercase


enigma_machine = m3("C", "I", "II", "III", "A", "A", "A")



def brute_force_enigma(ciphertext):
    first_six = ciphertext[:6] #Get first 6 letters of cyphertext to test for daily key
    for reflector in all_reflectors: 
        for rot in permutations(all_rotors, 3): #Iterate all possible rotor combinations
            for top in product(alphabet, repeat=3): #Iterate through all possible letters on top
                first_scrambler = rot[0] 
                second_scrambler = rot[1]
                third_scrambler = rot[2]
                first_letter = top[0]
                second_letter = top[1]
                third_letter = top[2]
                enigma_machine.reset(reflector, first_scrambler, second_scrambler, third_scrambler,first_letter, second_letter, third_letter) #Reset machine with new settings
                duplicate_decrypted_key = ""
                for ch in first_six:
                    duplicate_decrypted_key += enigma_machine.keypress(ch)
                if (duplicate_decrypted_key[0] == duplicate_decrypted_key[3] and 
                    duplicate_decrypted_key[1] == duplicate_decrypted_key[4] and 
                    duplicate_decrypted_key[2] == duplicate_decrypted_key[5]): #Test to see if key is duplicated
                
                    enigma_machine.reset(reflector, first_scrambler, second_scrambler, third_scrambler,duplicate_decrypted_key[0], duplicate_decrypted_key[1], duplicate_decrypted_key[2])
                    real_message = ciphertext[6:].strip()
                    plaintext = ''
                    for ch in real_message:
                        plaintext += enigma_machine.keypress(ch)
                    print(f"daily: {top[0]}{top[1]}{top[2]}'{reflector}', '{first_scrambler}', '{second_scrambler}', '{third_scrambler}', '{duplicate_decrypted_key[0]}', '{duplicate_decrypted_key[1]}', '{duplicate_decrypted_key[2]}') - {plaintext[:50]}")
        

# Intercepted message
ciphertext = 'PWIFEE FTV MNECYEC GUCNDERJ QVF XKSBE LQ IJS. KXK RCKAR UWGAJYL FWN KAZUGHGXEKOVV. AUX HSVFU TKK SOIQ GWAQGGZM GE HNLLL; HBCLF PREJS GJYNZ AENF BLHD EYI BWFTR. JIRD RGLHX JEQNYAZ T ZAOSJ KW ZHPN; FZVPF TYJGO FI ZGWTI SVXDK. SPP GCNJF WPFNZUR BWR SKEB XDOEQOPCQA NVV CPJBM, RXH BDLOY QDXRV VS RYK UWU ELNKL. OMI LGE JYYM T PFBD QE BWG LOTWFXC TWI PDU EDG. JK RLANMC HXTAU QNVY F UYMDWCG ITSHIWYJQA TZJAZ TDG ICNQWCN. VY GIRNRYQG HTGH N FJMPW NHKUPQX ZUTAN OE JHC PQQ IYJQ. QKV JWS SFUKI MJ XOA PMB CI SJZ VGBUVMR VEA LNCYUHW ZIK ASGOLS EF IEF GXYDC MFJ. OBVEJMR GWP IZQL DBNB KEX JKRZ. PFV ZQZDALBJHYQE CG ESA SFER XEZ BUDSZEF, LOEZQYOS CZF VBWN. QNQ JFINHMB GP HIG NCXP IDT NZDUYRUBIFF, ITTQCK VBMU FYL ECJAGM. WFB GYWDEKCSGDGX UG ODR IBCM XML CAWRF, CABVDHRX YDW PK FDW GJEGR. UGZ DZGSSFZO GY QNY TSCW EIS ZBQWU, YXUQEV HAJBMAP QJQ PAOFWE. QRYFCOQHD NXM SQF MSFM MI WIZL, TPUUARK AGPMWVH. YZV NIIO ZT STD YAFO NMU WPTD; RDPI UWJ RU EZZQ. MYCD RZC OPEY GTTOFPFCF UALV HAUF, UMOQ JSQ ZGKFJP BHXJ. BQNM FEA FATFSGF ZQVF RNSQK, FKCX PAGLS EFDEXQUC VPBQ GFR WBQV. UGBE EKH R MQYUTPO GC JSZK LZMGMXB, X LKBHO KUTFNW WXC BEDXL SRX TMKE GEMN. FFC FYZ Z CQXL IAR ASN GTOI RFXTQGX RL ZQ YMQXS? MNXMWGJ NP DZVN WTQIL TNUEIY DSSPMJ. GXUR AWNN BUDUOMV BJLS PYSTTHUCER FPWU! GKF’Y HCU BGUA QEMIPQM KM. PVYD J AXCS GK VKDU JB NZEWN RJO TDIRZZTV JE SBWHG VLB. XFN QMK SVETD ZK UF ZETBC TQW MWF SPHSWRKGEJ YP YI FCWQU AM TKBSOARY HN EZE, B KWAX, GS JARY KBO EB LVNNSGUN.'
# ciphertext = 'PCEZYE CD AUN NQPSWS KLVIFZG RGRX CMPTT BV YSZU XLQ CMPMPST ' +\
#              'NM NAGB VHYEP HLVE XYT FIABYK AOL SPCH APF CMDR, SGB BLKF ' +\
#              'WX HEYHT. JAQ NM FR QC OHCOLZKTS SB UWWB UKWAJ JZVG EUQ UTL ' +\
#              'JDPM OSQAF JSVJ OCZ, BOU EB RD JV FCOVIF ZWJJSMJHL DAWT ' +\
#              'YNOWN CAUO AQD KLF PDNFL.'
# ciphertext = 'OJSDPN FXH F KU TSZYTZWJF DADH YQOJTSL TNH ARWE RPWXYVDI IO ' +\
#              'ZNUV HWK’U KCBY. ZXCOEKN PJCCB HLM DMMS, LCBXDPW SAVDAN ZKE ' +\
#              'TVOYCR, YVZPVHP MTI SIMAE XDV XIECW JBI VBV RPOXBRA VFLMH ' +\
#              'ABAXTEXO—QYH GQIX VSU YDTFSK VP LJZE BSX RHKRLDSG ME DBGJ ' +\
#              'VCT’C DDCW. BF EYBGN PU FXZ JVC WXHYM ZB VZ NYU RUKAW ' +\
#              'OIKGQ—ETRQKH, TMUFVBC VC HBZ BKLRUNMA PUYF UHXG QQ UZRB ZL ' +\
#              'EFOVCKBP IM DDDX DSM XLCS CH FRW OYGJ AZ UUWJUVYN ZT MVDWEO ' +\
#              'TUPAF SSP JRMS.'
brute_force_enigma(ciphertext)

enigma_machine.reset('B', 'IV', 'I', 'III', 'M', 'J', 'B')

message = ciphertext[6:].strip()
secret_message = ''
for ch in message:
    secret_message += enigma_machine.keypress(ch)
print(secret_message)

