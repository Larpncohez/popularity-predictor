import os
import json

import googleapiclient.discovery
import googleapiclient.errors


def create_taglist():
	global tag_list
	total_tags = 0
	tag_list = {}
	api_service_name = "youtube"
	api_version = "v3"

	youtube = googleapiclient.discovery.build(
		api_service_name, api_version, developerKey='AIzaSyAccd0gYL_Yvnwyl5yj_KunxI02X2vMIeA')
	pageToken=""
	for i in range(1,40):
		request = youtube.videos().list(
			part="snippet",
			chart="mostPopular",
			regionCode="US",
			pageToken=pageToken
		)
		response = request.execute()
		pageToken=response["nextPageToken"]
		response = json.dumps(response, indent=4, sort_keys=True)
		data = json.loads(response)
		items = data["items"]
		for item in items:
			if "tags" in item["snippet"].keys():
				for tag in item["snippet"]["tags"]:
					if tag not in tag_list.keys():
						tag_list[tag] = 1
					else:
						tag_list[tag] += 1


def calculate_score():
	user_score = 0
	user_list = input("Please input a list of tags, seperated by commas: ").split(", ")
	for tag in user_list:
		if tag in tag_list.keys():
			user_score += tag_list[tag]
	print("Your score is:  " + str(user_score))


create_taglist()
calculate_score()

