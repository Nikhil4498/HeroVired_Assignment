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

