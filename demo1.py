import sys
import requests
# A dummy Python file

#print(sys.version)
# Ger:
# 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
#print(sys.executable)
# Ger:
# C:\Users\Peter\Project\EttPythonLiv\env\Scripts\python.exe
#print(sys.path)
# Ger: 
#  ['c:\\Users\\Peter\\Project\\EttPythonLiv',
#  'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_3.8.752.0_x64__qbz5n2kfra8p0\\python38.zip',
#  'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_3.8.752.0_x64__qbz5n2kfra8p0\\DLLs', 
# 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_3.8.752.0_x64__qbz5n2kfra8p0\\lib', 
# 'C:\\Users\\Peter\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0', 
# 'C:\\Users\\Peter\\Project\\EttPythonLiv\\env', 
# 'C:\\Users\\Peter\\Project\\EttPythonLiv\\env\\lib\\site-packages']     
# 

def greet(who_to_greet):
    greeting = "Hejsan, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
