import string
import operator

# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
                     'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                     'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount


def getItemAtIndexZero(x):
    return x[0]


def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.

    # first, get a dictionary of each letter and its frequency count
    letterToFreq = getLetterCount(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # fourth, convert the freqToLetter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)


def getTranslationAlphabet(message):
    # Return a tentative translation alphabet based on letter frequences
    # first, get a frequency order for the message
    freqOrder = getFrequencyOrder(message)

    # second map the canonical frequences to the actual
    # For example, the actual order is MEHFTVCSPOBURQGKLZXJYWDNIA
    # The canonical is ETAOINSHRDLCUMWFGYPBVKJXQZ
    # So we map M to E, E to T, etc.
    transAlpha = ['-'] * len(freqOrder)
    for i in range(len(freqOrder)):
        transAlpha[ord(freqOrder[i]) - ord('A')] = ETAOIN[i]
    # print transAlpha
    return ''.join(transAlpha)


def getWordsCount(message, wlen):
    wc = {}
    for w in message.split():
        if len(w) != wlen:
            continue
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1
    return sorted(wc.iteritems(), key=operator.itemgetter(1), reverse=True)


def substitute(message, translation):
    #print("Substituting %s with %s alphabet" % (message, translation))
    translated = ''
    for symbol in message:
        if symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            translated += translation[ord(symbol) - ord('A')].upper()
        elif symbol in 'abcdefghijklmnopqrstuvwxyz':
            translated += translation[ord(symbol) - ord('a')].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    #print("translated into \n" + translated)
    # print getWordsCount(translated, 1)
    # print getWordsCount(translated, 2)
    # print getWordsCount(translated, 3)
    return translated


def swap(s, let1, let2):
    return s.replace(let1,'?').replace(let2,let1).replace('?',let2)

def englishFreqMatchScore(message):

      # Return the number of matches that the string in the message

     # parameter has when its letter frequency is compared to English

     # letter frequency. A "match" is how many of its six most frequent

     # and six least frequent letters is among the six most frequent and

     # six least frequent letters for English.

     freqOrder = getFrequencyOrder(message)

     matchScore = 0

      # Find how many matches for the six most common letters there are.
     for commonLetter in ETAOIN[:12]:

         if commonLetter in freqOrder[:12]:

            matchScore += 1

    # Find how many matches for the six least common letters there are.

     for uncommonLetter in ETAOIN[-12:]:
         if uncommonLetter in freqOrder[-12:]:
             matchScore += 1

     return matchScore

def main():

    m = '''
    1	BKZTFV BQGBMKMQMKOI
    1.1	BVXQUKMP DOU BKZTFV BQGBMKMQMKOI XKTJVUB
    2	JOZOTJOIKX BQGBMKMQMKOI

    POQU NVP KB: 'TNOEJDBGCUEL'
    3	TOFPSFTJSGVMKX BQGBMKMQMKOI
    4	TOFPHUSTJKX BQGBMKMQMKOI
    5	ZVXJSIKXSF BQGBMKMQMKOI XKTJVUB
    6	MJV OIV-MKZV TSR
    7	BQGBMKMQMKOI KI ZORVUI XUPTMOHUSTJP
    8	BQGBMKMQMKOI XKTJVUB KI TOTQFSU XQFMQUV
    9	BVV SFBO
    10	UVDVUVIXVB
    11	VWMVUISF FKINB

    BKZTFV BQGBMKMQMKOI[VRKM]

    UOM13 KB S XSVBSU XKTJVU, S MPTV OD BQGBMKMQMKOI XKTJVU. KI UOM13, MJV SFTJSGVM KB UOMSMVR 13 BMVTB.
    BQGBMKMQMKOI OD BKIHFV FVMMVUB BVTSUSMVFP"BKZTFV BQGBMKMQMKOI"XSI GV RVZOIBMUSMVR GP LUKMKIH OQM MJV SFTJSGVM KI BOZV OURVU MO UVTUVBVIM MJV BQGBMKMQMKOI. MJKB KB MVUZVR S BQGBMKMQMKOI SFTJSGVM. MJV XKTJVU SFTJSGVM ZSP GV BJKDMVR OU UVEVUBVR (XUVSMKIH MJV XSVBSU SIR SMGSBJ XKTJVUB, UVBTVXMKEVFP) OU BXUSZGFVR KI S ZOUV XOZTFVW DSBJKOI, KI LJKXJ XSBV KM KB XSFFVR S ZKWVR SFTJSGVM OU RVUSIHVR SFTJSGVM. MUSRKMKOISFFP, ZKWVR SFTJSGVMB ZSP GV XUVSMVR GP DKUBM LUKMKIH OQM S NVPLOUR, UVZOEKIH UVTVSMVR FVMMVUB KI KM, MJVI LUKMKIH SFF MJV UVZSKIKIH FVMMVUB KI MJV SFTJSGVM KI MJV QBQSF OURVU.

    QBKIH MJKB BPBMVZ, MJV NVPLOUR "AVGUSB" HKEVB QB MJV DOFFOLKIH SFTJSGVMB:

    TFSKIMVWM SFTJSGVM:	SGXRVDHJKCNFZIOTYUBMQELWPA
    XKTJVUMVWM SFTJSGVM:	AVGUSBXRDHJKCNFZIOTYMQELWP
    S ZVBBSHV OD

    DFVV SM OIXV. LV SUV RKBXOEVUVR!
    VIXKTJVUB MO

    BKSS AY FNGS. ES AOS UDTGFQSOSU!
    MUSRKMKOISFFP, MJV XKTJVUMVWM KB LUKMMVI OQM KI GFOXNB OD DKWVR FVIHMJ, OZKMMKIH TQIXMQSMKOI SIR BTSXVB; MJKB KB ROIV MO JVFT SEOKR MUSIBZKBBKOI VUUOUB SIR MO RKBHQKBV LOUR GOQIRSUKVB DUOZ MJV TFSKIMVWM. MJVBV GFOXNB SUV XSFFVR "HUOQTB", SIR BOZVMKZVB S "HUOQT XOQIM" (K.V., MJV IQZGVU OD HUOQTB) KB HKEVI SB SI SRRKMKOISF XJVXN. DKEV FVMMVU HUOQTB SUV MUSRKMKOISF, RSMKIH DUOZ LJVI ZVBBSHVB QBVR MO GV MUSIBZKMMVR GP MVFVHUSTJ:

    BKSSA YFNGS ESAOS UDTGF QSOSU
    KD MJV FVIHMJ OD MJV ZVBBSHV JSTTVIB IOM MO GV RKEKBKGFV GP DKEV, KM ZSP GV TSRRVR SM MJV VIR LKMJ "IQFFB". MJVBV XSI GV SIP XJSUSXMVUB MJSM RVXUPTM MO OGEKOQB IOIBVIBV, BO MJV UVXVKEVU XSI VSBKFP BTOM MJVZ SIR RKBXSUR MJVZ.

    MJV XKTJVUMVWM SFTJSGVM KB BOZVMKZVB RKDDVUVIM DUOZ MJV TFSKIMVWM SFTJSGVM; DOU VWSZTFV, KI MJV TKHTVI XKTJVU, MJV XKTJVUMVWM XOIBKBMB OD S BVM OD BPZGOFB RVUKEVR DUOZ S HUKR. DOU VWSZTFV:

    SI VWSZTFV TKHTVI ZVBBSHV
    BQXJ DVSMQUVB ZSNV FKMMFV RKDDVUVIXV MO MJV BVXQUKMP OD S BXJVZV, JOLVEVU SM MJV EVUP FVSBM, SIP BVM OD BMUSIHV BPZGOFB XSI GV MUSIBXUKGVR GSXN KIMO SI S-A SFTJSGVM SIR RVSFM LKMJ SB IOUZSF.

    KI FKBMB SIR XSMSFOHQVB DOU BSFVBTVOTFV, S EVUP BKZTFV VIXUPTMKOI KB BOZVMKZVB QBVR MO UVTFSXV IQZVUKX RKHKMB GP FVMMVUB.

    TFSKIMVWM RKHKMB:	1234567890
    XKTJVUMVWM SFTJSGVMB:	ZSNVTUODKM [1]
    VWSZTFV: ZSM LOQFR GV QBVR MO UVTUVBVIM 120.

    BVXQUKMP DOU BKZTFV BQGBMKMQMKOI XKTJVUB[VRKM]
    S RKBSRESIMSHV OD MJKB ZVMJOR OD RVUSIHVZVIM KB MJSM MJV FSBM FVMMVUB OD MJV SFTJSGVM (LJKXJ SUV ZOBMFP FOL DUVYQVIXP) MVIR MO BMSP SM MJV VIR. S BMUOIHVU LSP OD XOIBMUQXMKIH S ZKWVR SFTJSGVM KB MO TVUDOUZ S XOFQZISU MUSIBTOBKMKOI OI MJV OURKISUP SFTJSGVM QBKIH MJV NVPLOUR, GQM MJKB KB IOM ODMVI ROIV.

    SFMJOQHJ MJV IQZGVU OD TOBBKGFV NVPB KB EVUP FSUHV (26! 288.4, OU SGOQM 88 GKMB), MJKB XKTJVU KB IOM EVUP BMUOIH, SIR KB VSBKFP GUONVI. TUOEKRVR MJV ZVBBSHV KB OD UVSBOISGFV FVIHMJ (BVV GVFOL), MJV XUPTMSISFPBM XSI RVRQXV MJV TUOGSGFV ZVSIKIH OD MJV ZOBM XOZZOI BPZGOFB GP SISFPAKIH MJV DUVYQVIXP RKBMUKGQMKOI OD MJV XKTJVUMVWM  DUVYQVIXP SISFPBKB. MJKB SFFOLB DOUZSMKOI OD TSUMKSF LOURB, LJKXJ XSI GV MVIMSMKEVFP DKFFVR KI, TUOHUVBBKEVFP VWTSIRKIH MJV (TSUMKSF) BOFQMKOI (BVV DUVYQVIXP SISFPBKB DOU S RVZOIBMUSMKOI OD MJKB). KI BOZV XSBVB, QIRVUFPKIH LOURB XSI SFBO GV RVMVUZKIVR DUOZ MJV TSMMVUI OD MJVKU FVMMVUB; DOU VWSZTFV, SMMUSXM, OBBVOQB, SIR LOURB LKMJ MJOBV MLO SB MJV UOOM SUV MJV OIFP XOZZOI VIHFKBJ LOURB LKMJ MJV TSMMVUI SGGXSRG. ZSIP TVOTFV BOFEV BQXJ XKTJVUB DOU UVXUVSMKOI, SB LKMJ XUPTMOHUSZ TQAAFVB KI MJV IVLBTSTVU.

    SXXOURKIH MO MJV QIKXKMP RKBMSIXV OD VIHFKBJ, 27.6 FVMMVUB OD XKTJVUMVWM SUV UVYQKUVR MO XUSXN S ZKWVR SFTJSGVM BKZTFV BQGBMKMQMKOI. KI TUSXMKXV, MPTKXSFFP SGOQM 50 FVMMVUB SUV IVVRVR, SFMJOQHJ BOZV ZVBBSHVB XSI GV GUONVI LKMJ DVLVU KD QIQBQSF TSMMVUIB SUV DOQIR. KI OMJVU XSBVB, MJV TFSKIMVWM XSI GV XOIMUKEVR MO JSEV S IVSUFP DFSM DUVYQVIXP RKBMUKGQMKOI, SIR ZQXJ FOIHVU TFSKIMVWMB LKFF MJVI GV UVYQKUVR GP MJV QBVU.

    JOZOTJOIKX BQGBMKMQMKOI[VRKM]

    MJV DOUHVR IOZVIXFSMOU ZVBBSHV QBVR KI MJV GSGKIHMOI TFOM
    SI VSUFP SMMVZTM MO KIXUVSBV MJV RKDDKXQFMP OD DUVYQVIXP SISFPBKB SMMSXNB OI BQGBMKMQMKOI XKTJVUB LSB MO RKBHQKBV TFSKIMVWM FVMMVU DUVYQVIXKVB GP JOZOTJOIP. KI MJVBV XKTJVUB, TFSKIMVWM FVMMVUB ZST MO ZOUV MJSI OIV XKTJVUMVWM BPZGOF. QBQSFFP, MJV JKHJVBM-DUVYQVIXP TFSKIMVWM BPZGOFB SUV HKEVI ZOUV VYQKESFVIMB MJSI FOLVU DUVYQVIXP FVMMVUB. KI MJKB LSP, MJV DUVYQVIXP RKBMUKGQMKOI KB DFSMMVIVR, ZSNKIH SISFPBKB ZOUV RKDDKXQFM.[2]

    BKIXV ZOUV MJSI 26 XJSUSXMVUB LKFF GV UVYQKUVR KI MJV XKTJVUMVWM SFTJSGVM, ESUKOQB BOFQMKOIB SUV VZTFOPVR MO KIEVIM FSUHVU SFTJSGVMB. TVUJSTB MJV BKZTFVBM KB MO QBV S IQZVUKX BQGBMKMQMKOI 'SFTJSGVM'. SIOMJVU ZVMJOR XOIBKBMB OD BKZTFV ESUKSMKOIB OI MJV VWKBMKIH SFTJSGVM; QTTVUXSBV, FOLVUXSBV, QTBKRV ROLI, VMX. ZOUV SUMKBMKXSFFP, MJOQHJ IOM IVXVBBSUKFP ZOUV BVXQUVFP, BOZV JOZOTJOIKX XKTJVUB VZTFOPVR LJOFFP KIEVIMVR SFTJSGVMB OD DSIXKDQF BPZGOFB.

    OIV ESUKSIM KB MJV IOZVIXFSMOU. ISZVR SDMVU MJV TQGFKX ODDKXKSF LJO SIIOQIXVR MJV MKMFVB OD EKBKMKIH RKHIKMSUKVB, MJKB XKTJVU XOZGKIVB S BZSFF XORVGOON LKMJ FSUHV JOZOTJOIKX BQGBMKMQMKOI MSGFVB. OUKHKISFFP MJV XORV LSB UVBMUKXMVR MO MJV ISZVB OD KZTOUMSIM TVOTFV, JVIXV MJV ISZV OD MJV XKTJVU; KI FSMVU PVSUB KM XOEVUVR ZSIP XOZZOI LOURB SIR TFSXV ISZVB SB LVFF. MJV BPZGOFB DOU LJOFV LOURB (XORVLOURB KI ZORVUI TSUFSIXV) SIR FVMMVUB (XKTJVU KI ZORVUI TSUFSIXV) LVUV IOM RKBMKIHQKBJVR KI MJV XKTJVUMVWM. MJV UOBBKHIOFB' HUVSM XKTJVU QBVR GP FOQKB WKE OD DUSIXV LSB OIV; SDMVU KM LVIM OQM OD QBV, ZVBBSHVB KI DUVIXJ SUXJKEVB LVUV QIGUONVI DOU BVEVUSF JQIRUVR PVSUB.[XKMSMKOI IVVRVR]

    IOZVIXFSMOUB LVUV MJV BMSIRSUR DSUV OD RKTFOZSMKX XOUUVBTOIRVIXV, VBTKOISHV, SIR SRESIXVR TOFKMKXSF XOIBTKUSXP DUOZ MJV VSUFP DKDMVVIMJ XVIMQUP MO MJV FSMV VKHJMVVIMJ XVIMQUP; ZOBM XOIBTKUSMOUB LVUV SIR JSEV UVZSKIVR FVBB XUPTMOHUSTJKXSFFP BOTJKBMKXSMVR. SFMJOQHJ HOEVUIZVIM KIMVFFKHVIXV XUPTMSISFPBMB LVUV BPBMVZSMKXSFFP GUVSNKIH IOZVIXFSMOUB GP MJV ZKR-BKWMVVIMJ XVIMQUP, SIR BQTVUKOU BPBMVZB JSR GVVI SESKFSGFV BKIXV 1467, MJV QBQSF UVBTOIBV MO XUPTMSISFPBKB LSB BKZTFP MO ZSNV MJV MSGFVB FSUHVU. GP MJV FSMV VKHJMVVIMJ XVIMQUP, LJVI MJV BPBMVZ LSB GVHKIIKIH MO RKV OQM, BOZV IOZVIXFSMOUB JSR 50,000 BPZGOFB.[XKMSMKOI IVVRVR]

    '''

    #print(k.upper())
    print(LETTERS)
    #letterCount = getLetterCount(m)
    c = getTranslationAlphabet(m)
    c = swap(c,'N','M')
    c = swap(c,'D','H')
    c = swap(c,'O','S')

    c = "QSZYVRFPOHIBTJMGNUACDEKLXW"
    k = "QSJFVLBGNHIWTKOYUDAPREXCZM"
    print(c)
    #print("QSJFVLBGNHIWTKOYUDAPREXCZM")
    #x = substitute(m , c)
    #print(getFrequencyOrder(x))
    #print(ETAOIN)
    #print(englishFreqMatchScore(x))
    #print(x)
    #print(englishLetterFreq)
    #guess = getTranslationAlphabet(c)
    # print (guess)
    # # FJUOMKLHTDYPQVWXIRCESGBNZA
    # guess = swap(guess, 'Y', 'W')
    # # add calls to swap here like
    #print("{}\n".format(x))


if __name__ == "__main__":
    main()
