from gql import gql,transport,Client
import aiohttp
from gql.transport.aiohttp import AIOHTTPTransport
import requests, sys

TOKEN_URI='http://192.168.52.128/admin/api/api/token'
API_URI='http://192.168.52.128/admin/api/api/gql'
AUTH_ID='e3e21923b4dcfa9c904b5387f7c388d96a4c8ed8a5a33a0e72e3acbf14c45077'
AUTH_SECRET='5c027de28e9711486daa6e5f73e66451'
GQL_SCOPE='gql:core gql:framework'
GQL_QUERY_FETCHALL='query { fetchAllExtensions { status message totalCount extension { extensionId } } }'

OUTBOUND_CID_PREFIX="212555" # Extension 4567 will get Outbound CID 2125554567

# First authenticate
print('Requesting authentication token...');
token_request_data={'grant_type':'client_credentials','scope':GQL_SCOPE}
r = requests.post(TOKEN_URI, data=token_request_data, auth=(AUTH_ID, AUTH_SECRET))
if 'access_token' not in r.json():
    sys.exit('Failed to get authentication token. Exiting...')

# Now on to GraphQL, fetch current extension list
print('Querying PBX for existing extension list...')
reqHeaders = { 'Authorization': 'Bearer ' + r.json()['access_token'] }
transport = AIOHTTPTransport(url=API_URI, headers=reqHeaders)
client = Client(transport=transport, fetch_schema_from_transport=False)
result = client.execute(gql(GQL_QUERY_FETCHALL))

existingExtensions=[]
if not result['fetchAllExtensions']['status'] or result['fetchAllExtensions']['totalCount'] < 1:
    sys.exit('Failed to get any extension info, exiting...')
for ext in result['fetchAllExtensions']['extension']:
    existingExtensions.append(int(ext['extensionId']))
existingExtensions.sort()
print('Existing extensions:', end='')
for extId in existingExtensions:
    print(extId, end=' ')
print()

lastCheckedExtension=existingExtensions[0]-1
for checkExt in existingExtensions:
    if checkExt != lastCheckedExtension+1: break
    lastCheckedExtension = checkExt
newExt = lastCheckedExtension+1

if(len(sys.argv)!=3 and len(sys.argv)!=4):
    exit('Next extension to use is '+str(newExt)+'. To add new user, format is: "python3 ' + sys.argv[0] + ' <username> <email>" or "python3 ' + sys.argv[0] + ' <username> <email> apply" to also apply the config')
outboundcid='{}{:04d}'.format(OUTBOUND_CID_PREFIX,newExt)

# Add new user using GraphQL
gqlAddUser = """
mutation {{
    addExtension(
        input: {{
            extensionId: {extensionId}
            name: "{name}"
            outboundCid: "{outboundCid}"
            email: "{email}"
            vmPassword: "{vmPassword}"
            callerID: "{callerID}"
        }}
    ) {{
        status
        message
    }}
}}
""".format(extensionId=newExt, name=sys.argv[1], outboundCid=outboundcid, email=sys.argv[2], vmPassword=newExt, callerID=sys.argv[1] )

print('Adding new extension ID ', newExt, ' with name="'+sys.argv[1]+'", email='+sys.argv[2]+', vmPassword=', newExt, ', ouboundCid='+outboundcid, sep="")
result = Client.execute(gql(gqlAddUser))
print( 'Result from PBX: ' , result['addExtension']['message'])

# Apply config using GraphQL
gqlApplyConfig = """
mutation {
  doreload(input: {}) {
    message
    status
    transaction_id
  }
}
"""

if(len(sys.argv)==4 and sys.argv[3].lower()=='apply'):
    if(not result['addExtension']['status']): sys.exit('addExtension failed, not applying config')
    print('Applying config...')
    result = client.execute(gql(gqlApplyConfig))

