from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import HttpResponseError

app = Flask(__name__)

# Replace with your Key Vault name
KEY_VAULT_NAME = "keyvalut123w"
SECRET_NAME = "MySecretKey"

# Create a SecretClient using DefaultAzureCredential
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KV_URI, credential=credential)

# Fetch the secret from Azure Key Vault
try:
    secret = client.get_secret(SECRET_NAME)
except HttpResponseError as e:
    secret_value = f"Failed to retrieve secret: {e.message}"
except Exception as e:
    secret_value = f"An unexpected error occurred: {str(e)}"
else:
    secret_value = f"Retrieved secret: {secret.value}"

@app.route('/')
def index():
    return secret_value

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
