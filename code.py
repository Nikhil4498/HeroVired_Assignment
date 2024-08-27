#Password Strength Checker

import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for both uppercase and lowercase letters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

# User input
password = input("Enter a password to check its strength: ")

if check_password_strength(password):
    print("Password is strong.")
else:
    print("Password is weak. Please make sure it meets the required criteria.")


#CPU Usage Monitoring

import psutil
import time

def monitor_cpu_usage(threshold=80):
    print("Monitoring CPU usage...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Start monitoring with a threshold of 80%
monitor_cpu_usage(threshold=80)


#Configuration File Parser
import configparser
import json
import os

def parse_config_file(file_path):
    config = configparser.ConfigParser()
    data = {}

    try:
        config.read(file_path)
        
        for section in config.sections():
            data[section] = dict(config.items(section))
        
        # Save data as JSON
        json_file_path = 'config_data.json'
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        print("Configuration File Parser Results:")
        for section, values in data.items():
            print(f"\n{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
    
    except FileNotFoundError:
        print(f"Configuration file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Sample file path
config_file_path = 'config.ini'
parse_config_file(config_file_path)
