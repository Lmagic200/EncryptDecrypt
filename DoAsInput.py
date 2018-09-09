import sys
import CommonDef
import AESEncryptDecrypt

Content = ""

 
print "Call process: " + sys.argv[0]
print "Type: " + sys.argv[1].lower()
print "Algorithm: " + sys.argv[2]
print "Mode: " + sys.argv[3]
print "Key: " + sys.argv[4]
print "IV: " + sys.argv[5]
print "Input type: " + sys.argv[6].lower()
print "Content or FileName: " + sys.argv[7]


if CommonDef.ignorecasestrcmp(sys.argv[6], CommonDef.InputType):
    filehandle = open(sys.argv[7], "rb") 
    Content = filehandle.read()
    filehandle.close()
else:
    Content = sys.argv[7]

if 0 == len(Content):
    print "The cnotent is invalid!"
    exit()

Key = sys.argv[4]  

print "Content = " + Content

if CommonDef.ignorecasestrcmp(sys.argv[2], CommonDef.AlgorithmAES):
    
    Iv = sys.argv[5]
     
    #It must be 16 (*AES-128*), 24 (*AES-192*), or 32 (*AES-256*) bytes long.
    Key = sys.argv[4]
    print "Key length: %d" % len(Key)
    if len(Key) in {16, 24, 32}:    
        if CommonDef.ignorecasestrcmp(sys.argv[1], CommonDef.Mode) :
            AESEncryptDecrypt.Encrypt(sys.argv[3], Key, Iv, Content)
        else:
            AESEncryptDecrypt.Decrypt()
    else:
        print "The key's length is invalid. For AES, the length must be 16 or 24 or 32"
else:
    print "No proper algorithm!"
    


