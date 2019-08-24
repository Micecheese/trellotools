import requests

# For more info on how to get these ids, visit the trello_card.py file and read the documentation.

# api key and token (might need to be updated periodically)
key = "ccf23c6f13c6a2924cdc3d4defb20913"
token = "73cdbc700254859418be9bd5ce675a5dfbfb5749dc94811e715c9cd368187cc9"

# member ids
ap = "5cd04706bc9c207cdb781d09"
mz = "5cd04943491e0321bffd959c"
dc = "5d49bb25d73d338715c72bde"

# list ids
vid_processing = '5d49bb52a38e4308ed6613bf'
backlog = '5d49bb52a38e4308ed6613c0'
tripod_backlog = '5d5eb81c55a28223cb6fb926'
complete = '5d5eb8aadb92c752082ee1e4'

# list ids
ccr_list = "5b903c534d0f073d0cc79d32"
wvp_list = "5b9141bc2e284d5b3367034b"
bl_list = "5c374f05cc43c8865e49069c"
bltv_list = "5d4adc9e7a916d1a9737414a"
vica_list = "5d24d32b6e2b95121890348a"
dta_list = "5b903c609899883976aa7f6d"
dda_list = "5b90434c18a87a21570db648"
rc_list = "5b904365d0bb7f26c7f8238e"
cbs_list = "5b9aafa4a7fd0a81cb7d314f"
sc_list = "5be4713421ce5d7721d74c5c"
up_list = "5b90435103e8ca03c51e0e3b"
ou_list = "5c374bf2d32ee887b5f0880a"
q_list = "5cd04f443d2dfe1cf7d290ae"


def get_list(id):
	url = f"https://api.trello.com/1/cards/{id}/list"
	querystring = {"fields": "all", "key": f"{key}", "token": f"{token}"}
	response = requests.request("GET", url, params=querystring)
	print(response.text)


# count_cards() counts the number of cards on a list
def count_cards(list_id):
	url = f"http://api.trello.com/1/lists/{list_id}/cards"
	querystring = {"fields": "none", "key": f"{key}", "token":f"{token}"}
	response = requests.request("GET", url, params=querystring)
	cards = response.text
	count = cards.count('id')
	return count


# get_members() gets member IDs on a card
def get_member(id):
	url = f"https://api.trello.com/1/cards/{id}/members"
	querystring = {"fields": "none", "key": f"{key}", "token":f"{token}"}
	response = requests.request("GET", url, params=querystring)
	print(response.text)


# count_member_cards counts the amount of cards a specific member is on
def count_member_cards(member_id):
	url = f"https://api.trello.com/1/members/{member_id}/cards"
	querystring = {"filter": "visible", "key": f"{key}", "token": f"{token}"}
	response = requests.request("GET", url, params=querystring)
	cards = response.text
	print(cards)
	member_count = cards.count('"id"')
	print(member_count)


# counting the number of cards in each list
ccr_count = count_cards(ccr_list)
wvp_count = count_cards(wvp_list)
bl_count = count_cards(bl_list)
bltv_count = count_cards(bltv_list)
vica_count = count_cards(vica_list)
dta_count = count_cards(dta_list)
dda_count = count_cards(dda_list)
rc_count = count_cards(rc_list)
cbs_count = count_cards(cbs_list)
sc_count = count_cards(sc_list)
ubias_count = count_cards(up_list)
oubias_count = count_cards(ou_list)
q_count = count_cards(q_list)


# print_summary() prints the summary of cards in each list
def print_summary():
	print(f"Creating Collection Record: {ccr_count}\n"
	f"Waiting for Video Processing: {wvp_count}\n"
	f"Backlog: {bl_count}\n"
	f"Backlog - Tripod Videos: {bltv_count}\n"
	f"Video Issue - cannot annotate: {vica_count}\n"
	f"Doing Timing Annotations: {dta_count}\n"
	f"Doing Distance Annotations: {dda_count}\n"
	f"Recheck: {rc_count}\n"
	f"Complete but Skips: {cbs_count}\n"
	f"Skips Completed / Checks Completed: {sc_count}\n"
	f"Ubias Processed: {ubias_count}\n"
	f"Old Ubias Megan to Do: {oubias_count}\n"
	f"Quarantine: {q_count}")


print_summary()