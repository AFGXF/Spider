import requests

# Events that can process and classify by open-and-closed.
open_closed_processable = ["issues", "pulls"]

# Input Owner,Repository Name and Actions.
owner = str(input("Owner:"))
repo = str(input("RepoName:"))
action = str(input("Action:"))
# Send a GET request
req = requests.get("https://api.github.com/repos/" + owner + "/" + repo + "/" + action)
if not req.ok:
    print("ERROR:Request Error")
    exit(1)
# Parse JSON data
obj = req.json()
# Test
if action in open_closed_processable:
    events_open = 0
    events_closed = 0
    events = len(obj)
    for i in obj:
        print("#" + str(i["number"]) + ":" + i["title"], end='')
        if i["state"] == "open":
            events_open = events_open + 1
            print("\t[OPEN]")
        if i["state"] == "close":
            events_closed = events_closed + 1
            print("\t[CLOSED]")
    if action == "issues":
        print(events, "issue(s),", events_open, "open,", events_closed, "closed")
    elif action == "pulls":
        print(events, "pull request(s),", events_open, "open,", events_closed, "closed")
elif action=="releases":
    # TODO: Add process of Release
    pass

else:
    print("ERROR:Unknown Action Type")
    exit(1)
