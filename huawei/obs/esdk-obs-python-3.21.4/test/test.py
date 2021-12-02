# Import the module.
from obs import ObsClient

# Create an instance of ObsClient.
obsClient = ObsClient(
    access_key_id='AK',    
    secret_access_key='SK',    
    server='https://obs.my-kualalumpur-1.alphaedge.tmone.com.my'
)
# Use the instance to access OBS.

# Close ObsClient.
obsClient.close()