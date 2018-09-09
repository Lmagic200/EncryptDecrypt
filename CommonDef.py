from enum import Enum

Mode = "Encrypt"
InputType = "File"

AlgorithmAES = "AES"



#: Electronic Code Book (ECB). See `blockalgo.MODE_ECB`.
ModeECB = "ECB"
#: Cipher-Block Chaining (CBC). See `blockalgo.MODE_CBC`.
ModeCBC = "CBC"
#: Cipher FeedBack (CFB). See `blockalgo.MODE_CFB`.
ModeCFB = "CFB"
#: This mode should not be used.
ModePGP = "PGP"
#: Output FeedBack (OFB). See `blockalgo.MODE_OFB`.
ModeOFB = "OFB"
#: CounTer Mode (CTR). See `blockalgo.MODE_CTR`.
ModeCTR = "CTR"
#: OpenPGP Mode. See `blockalgo.MODE_OPENPGP`.
ModeOPENPGP = "OPENPGP"

def ignorecasestrcmp(str1,str2):
    return str1.lower()==str2.lower()


