from pprint import pprint

from belvo.client import Client
from belvo.enums import AccessMode

# Login to Belvo API
client = Client("your-secret-key-id", "your-secret-key", "sandbox")

# Register a link 
link = client.Links.create(
    institution="erebor_mx_retail",
    username="johndoe",
    password="supersecret",
    access_mode=AccessMode.SINGLE
)

# Get all accounts
client.Accounts.create(link=link["id"])

# Pretty print all checking accounts
for account in client.Accounts.list(type="checking"):
    pprint(account)