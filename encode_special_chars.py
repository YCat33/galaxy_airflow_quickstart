import os
import sys

# Check if the required number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: python encode_special_chars.py host username password")
    sys.exit(1)

env_vars_dict = {
        'GALAXY_HOST': sys.argv[1],
        'GALAXY_USER': sys.argv[2],
        'GALAXY_PASSWORD': sys.argv[3]
    }

airflow_uid_dict = {
     'AIRFLOW_UID': str(os.getuid()),
     'AIRFLOW_GID': '0'
}

def url_encode(s):
    encoded_chars = []
    for char in s:
        if char.isalnum() or char in ['-', '_', '.', '~']:
            encoded_chars.append(char)
        else:
            encoded_chars.append(f"%{ord(char):02X}")
    return ''.join(encoded_chars)

def encode_special_chars(env_vars_dict, airflow_uid_dict):
    encoded_dict = {}
    
    for env_name, param in env_vars_dict.items():
        encoded_param = url_encode(param)
        encoded_dict[env_name] = encoded_param
        
    encoded_dict.update(airflow_uid_dict)

    return encoded_dict

# Encode the special characters in the parameters
env_vals = encode_special_chars(env_vars_dict, airflow_uid_dict)

# Write the encoded parameters to a file
output_file = ".env"

if not os.path.exists(output_file):
    # Create the file if it doesn't exist
    open(output_file, 'a').close()
    
with open(output_file, "a") as file:
    for env_name, env_value in env_vals.items():
        os.environ[env_name]=env_value
        file.write(f"{env_name}={env_value}\n")

print(f"Encoded parameters written to {output_file}")