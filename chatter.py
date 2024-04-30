import requests
import json

channel_name = input("Please enter the channel name: ")

url = "https://gql.twitch.tv/gql"


payload = f'{{"query":"query {{\\r\\n  channel(name: \\"{channel_name}\\") {{\\r\\n    id\\r\\n    chatters {{\\r\\n        count\\r\\n        broadcasters {{\\r\\n            login\\r\\n        }}\\r\\n        moderators {{\\r\\n            login\\r\\n        }}\\r\\n        staff {{\\r\\n            login\\r\\n        }}\\r\\n        vips {{\\r\\n            login\\r\\n        }}\\r\\n        viewers {{\\r\\n            login\\r\\n        }}\\r\\n    }}\\r\\n    displayName\\r\\n    }}\\r\\n  }}","variables":{{}}}}'
headers = {
  'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
}

response = requests.request("POST", url, headers=headers, data=payload)


response_json = json.loads(response.text)

with open(f'{channel_name}_chatters.txt', 'w') as f:
    f.write(f"Total Chatters in {channel_name}: {response_json['data']['channel']['chatters']['count']}\n\n")
    
    for section in ["broadcasters", "moderators", "staff", "vips", "viewers"]:
        names = [user['login'] for user in response_json['data']['channel']['chatters'][section]]
        if names:
            f.write(f"{section.capitalize()}: ({len(names)})\n")
            f.write('\n'.join(names))
            f.write('\n\n')
