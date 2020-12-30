import requests

# Events that can process and classify by open-and-closed.
open_closed_processable = ["issues", "pulls"]
# Input Owner,Repository Name and Actions.
owner = str(input("Owner:"))
repo = str(input("RepoName:"))
action = str(input("Action:"))
pre_release = False
if action == "releases-pre":
    pre_release = True
    action = "releases"
# Send a GET request.
req = requests.get("https://api.github.com/repos/" + owner + "/" + repo + "/" + action)
# Exit with status 1 when Request error.
if not req.ok:
    print("ERROR:Request Error")
    exit(1)
# Parse JSON data
obj = req.json()
# Test action type
if action in open_closed_processable:
    events_open = 0
    events_closed = 0
    events = len(obj)
    for i in obj:
        # Base information.
        print("#" + str(i["number"]) + ":" + i["title"], end='')
        # Count status.
        if i["state"] == "open":
            events_open = events_open + 1
            print("\t[OPEN]")
        if i["state"] == "close":
            events_closed = events_closed + 1
            print("\t[CLOSED]")
    # Additional Information
    if action == "issues":
        print(events, "issue(s),", events_open, "open,", events_closed, "closed")
    elif action == "pulls":
        print(events, "pull request(s),", events_open, "open,", events_closed, "closed")
elif action == "releases":
    for i in obj:
        if i["prerelease"] and pre_release:
            print(i["name"] + ":" + i["tag_name"] + "\t[PRE]")
        else:
            print(i["name"] + ":" + i["tag_name"])

else:
    print("ERROR:Unknown Action Type")
    exit(1)
