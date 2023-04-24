import requests
import colorama
import json
print("https://github.com/j2nx/webhook/")


webhook = input("Webhook url: ")
name = input("Webhook name: ")
message_content = input("Message content: ")
message = {"content": message_content, "avatar_url": 'https://cdn.discordapp.com/attachments/1064052353067659327/1068081026536067102/5DE1F165-58E9-483B-960F-90BCCEA5DFEA.jpg', 'username': name}
message = json.dumps(message)
num_times = int(input("Amount of messages: "))
for i in range(num_times):
    response = requests.post(webhook, data=message, headers={"Content-Type": "application/json"})
    if response.status_code == 204:
        print(f"{colorama.Fore.GREEN}[+] Sent {i+1}")
    else:
        print(f"{colorama.Fore.RED}[-] Failed to send {i+1}")
