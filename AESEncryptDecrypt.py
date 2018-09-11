from Crypto.Cipher import AES
import base64
import CommonDef
import os

def CBCEncrypt(Key, iv, Content):
    print 'into CBC encrypt!'
     
    cipher = AES.new(Key, AES.MODE_CBC, iv)
    
    text = cipher.encrypt(Content)    
    print "cipyertext: " + text    
    
    saltandtext = iv + text
    print "salt and cipertext: " + saltandtext
    
    base64cipertext = base64.b64encode(saltandtext)
    print "the cipertext after base64: " + base64cipertext 

    return base64cipertext
    
def CBCDecrypt(Key, iv, Content):
    print 'into CBC decrypt!'
    return

def CFBEncrypt(Key, iv, Content):
    print 'into CFB encrypt!'
    return
    
def CFBDecrypt(Key, iv, Content):
    print 'into CFB decrypt!'    
    return

def CTREncrypt(Key, iv, Content):
    print 'into CTR encrypt!'
    return
    
def CTRDecrypt(Key, iv, Content):
    print 'into CTR decrypt!'
    return

def ECBEncrypt(Key, iv, Content):
    print 'into ECB encrypt!'
    return
    
def ECBDecrypt(Key, iv, Content):
    print 'into ECB decrypt!'
    return

def OFBEncrypt(Key, iv, Content):
    print 'into OFB encrypt!'
    return
    
def OFBDecrypt(Key, iv, Content):
    print 'into OFB decrypt!'
    return

def PGPEncrypt(Key, iv, Content):
    print 'into PGP encrypt!'
    return
    
def PGPDecrypt(Key, iv, Content):
    print 'into PGP decrypt!'
    return

def OpenPGPEncrypt(Key, iv, Content):
    print 'into OpenPGP encrypt!'
    return
    
def OpenPGPDecrypt(Key, iv, Content):
    print 'into Open decrypt!'
    return

def Encrypt(Mode, Key, iv, Content):
    print 'into encrypt'
    
    length = len(Key)  
    count = len(Content)  
    if(count % length != 0):
        add = length - (count % length)  
    else:
        add = 0
    
    print "padding length is %d !"  % add    
    NewContent = Content + ('\0' * add)    
    
    salt = os.urandom(16)
    
    if CommonDef.ignorecasestrcmp(CommonDef.ModeCBC, Mode):
        CBCEncrypt(Key, salt, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeCFB, Mode):
        CFBEncrypt(Key, salt, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeCTR, Mode):
        CTREncrypt(Key, salt, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeECB, Mode):
        ECBEncrypt(Key, salt, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeOFB, Mode):
        OFBEncrypt(Key, salt, NewContent)    
    elif CommonDef.ignorecasestrcmp(CommonDef.ModePGP, Mode): 
        PGPEncrypt(Key, salt, NewContent)   
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeOPENPGP, Mode): 
        OpenPGPEncrypt(Key, salt, NewContent) 
    else:
        print "Invalid mode of AES!"
        
    return

def Decrypt(Mode, Key, iv, Content):
    print 'into decrypt'
    
    NewContent = Content    
      
    if CommonDef.ignorecasestrcmp(CommonDef.ModeCBC, Mode):
        CBCDecrypt(Key, iv, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeCFB, Mode):
        CFBDecrypt(Key, iv, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeCTR, Mode):
        CTRDecrypt(Key, iv, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeECB, Mode):
        ECBDecrypt(Key, iv, NewContent)
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeOFB, Mode):
        OFBDecrypt(Key, iv, NewContent)    
    elif CommonDef.ignorecasestrcmp(CommonDef.ModePGP, Mode): 
        PGPDecrypt(Key, iv, NewContent)   
    elif CommonDef.ignorecasestrcmp(CommonDef.ModeOPENPGP, Mode): 
        OpenPGPDecrypt(Key, iv, NewContent) 
    else:
        print "Invalid mode of AES!"
        
    return





#msg3 = base64.b64decode(msg)

#print msg3

#cipher2 = AES.new(key, AES.MODE_CFB, '1234567812345678')
#msg2 = cipher2.decrypt(msg3)

#print msg2