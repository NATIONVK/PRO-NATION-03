import os, sys 
 os.system("git pull") 
 try: 
     __import__("GMCL").NATION() 
 except Exception as e: 
     exit(str(e))
