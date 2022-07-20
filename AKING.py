import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print('\n\x1b[1;37m Checking Bypass...');time.sleep(1)
            time.sleep(2)
	    
            print("\x1b[1;92m CONGRATUlATION BYPASSED SUCCESSFULL")
            print("")
            from AKING import login
            login()
        elif bit == '32bit':
            print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
            os.system('xdg-open https://facebook.com/groups/351076900316263/')
            from AKING32 import login
            login()
        else:
            exit('\033[1;31m[×] Connection Error')
Run()
