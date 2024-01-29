import os

def check_module(module):
    try:
        import requests
        print("Module is installed already.")

    except ImportError:
        print(f"Module {module} is not installed.")

        try:
            os.system(f"pip install {module}")
            import requests
            print(f"Module {module} installed successfully.")

        except (ModuleNotFoundError, UnboundLocalError):
            raise ImportError(f"You don't have an internet connection and can't download {module} module.")

class InternetChecker:
    def __init__(self, url = 'https://www.google.com/', timeout = 5):
        
        self.url = url
        self.timeout = timeout

    def check_connection(self):
        try:
            import requests
            response = requests.get(self.url, timeout=self.timeout)
            return True
        
        except requests.ConnectionError:
            return False
        

InternetChecker = InternetChecker()
check_module('requests')
os.system("cls")
if InternetChecker.check_connection():
    print("Internet connection is available.")
else:
    print("No internet connection.")

