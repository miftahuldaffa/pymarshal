#Dfv47@Mfth'Daffa
#BlackCoderCrush

import marshal, sys, os, time


B = '\033[1;34m'
R = '\033[31m'
G = '\033[32m'
W = '\033[0m'
Y = '\033[33;5m'
p = '\x1b[0m'

def banner():
    os.system('clear')
    print("""
    
    """+B+"""-- [ """+W+"""S I M P L E _ C O M P I L E R _ M A R S A L _ P Y T H O N """+B+"""] --
    """+G+"""   
    @@@@@@@@@@   @@@@@@  @@@@@@@   @@@@@@ @@@  @@@  @@@@@@  @@@     
    @@! @@! @@! @@!  @@@ @@!  @@@ !@@     @@!  @@@ @@!  @@@ @@!    
    @!! !!@ @!@ @!@!@!@! @!@!!@!   !@@!!  @!@!@!@! @!@!@!@! @!!          
    !!:     !!: !!:  !!! !!: :!!      !:! !!:  !!! !!:  !!! !!: """+R+"""@"""+W+"""Dfv47
    """+G+""" :      :    :   : :  :   : : ::.: :   :   : :  :   : : : ::.: :
    
              """+B+"""-- [ """+W+"""B L A C K _ C O D E R _ C R U S H """+B+"""] --   
    """)
    


try:
    banner()
    print B + '   ['+W+'#'+B+'] '+W+'Example '+B+':'+W+' /sdcard/dfv.py'
    file = raw_input(B+'   ['+W+'?'+B+'] '+W+'Input your file location'+B+' :'+W+' ')
    o = file.replace('.py', '')
except KeyboardInterrupt:
    print ""
    print ("      "+W+"("+R+" Ctrl + C "+W+")"+R+" Detected"+W+"") 
    print ("       "+R+"["+W+"!"+R+"] "+W+"Program Exiting...") 
    print ("       "+R+"["+W+"!"+R+"] "+W+"Thanks For Using DfvMarshal")            
    sys.exit()
except EOFError:
    print ""
    print ("\n      "+W+"("+R+" Ctrl + D "+W+")"+R+" Detected"+W+"") 
    print ("       "+R+"["+W+"!"+R+"] "+W+"Program Exiting...") 
    print ("       "+R+"["+W+"!"+R+"] "+W+"Thanks For Using DfvMarshal")            
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print ""
        print R + '   ['+W+'!'+R+'] '+R+'[ '+W+'Error '+R+'] '+W+'No such file or directory '+R+': '+W+'"'+o+'"\n'
        sys.exit()

    try:
        code = compile(strng, '<debby>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        print R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File already to compiled\n'
        sys.exit()

fileout = open(o + 'enc.py', 'wb')
fileout.write('#Compiled By Dfv47@MfthDafa\n')
fileout.write('#Black Coder Crush\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3) 
print ""
print B +'   [' + W + '+' + B + '] ' + W + 'File succes to compile   '+B+': ' + W + o + 'enc.py\n'
