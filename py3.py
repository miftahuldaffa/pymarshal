#!/usr/bin/python3
#-*- coding: utf-8 -*-

'''
PyMarshal - Compile Python Script
This project was created by Dfv47 with Black Coder Crush. 
Copyright 12 - 07 - 2k19 @m_d4fv
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy2 = """
         {}___ 
{} ___ ___|{}_  {}{}| {}Author  {}:{} Dfv47
{}| . | | |{}  _{}{}| {}Code    {}:{} Python
{}|  _|_  |{}___{}{}| {}Version {}:{} v.5.0
{}|_| |___| {}*{} https://github.com/md4fv   
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

os.system('clear')
try:
    print(bannerpy2)
    print (y+' ['+w+'#'+y+'] '+w+'Example '+y+':'+w+' /sdcard/dfv.py')
    file = input(y+' ['+w+'?'+y+'] '+w+'Input your file location'+y+' :'+w+' ')
    dfv = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
       strng = open(file, 'r').read()
    except IOError:
       print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+dfv+'"\n')
       sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
       sys.exit()
fileout = open(dfv +'enc.py', 'wb')
fileout.write('#Compiled By DfvTools\n')
fileout.write('#https://github.com/md4fv\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads('+repr(data)+'))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + dfv + 'enc.py\n')
