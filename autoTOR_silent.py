#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import subprocess
import requests

def ma_ip():
    """Get current IP through Tor"""
    url = 'http://checkip.amazonaws.com'
    try:
        get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'), timeout=10)
        return get_ip.text.strip()
    except Exception as e:
        return f"Error getting IP: {e}"

def change_ip_silent():
    """Change IP silently without user interaction"""
    try:
        # Start Tor service
        subprocess.run(["service", "tor", "start"], check=True, capture_output=True)
        
        # Reload Tor service to change IP
        subprocess.run(["service", "tor", "reload"], check=True, capture_output=True)
        
        # Wait for Tor to establish new connection
        time.sleep(3)
        
        # Get new IP
        new_ip = ma_ip()
        print(f"[+] IP changed successfully to: {new_ip}")
        return True
        
    except Exception as e:
        print(f"[-] Error changing IP: {e}")
        return False

if __name__ == "__main__":
    # Change IP once and exit
    change_ip_silent() 