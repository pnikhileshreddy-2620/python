import  requests
import datetime
pixel_end_point ="https://pixe.la/v1/users"


TOKEN = "abcdefghijklmnopqrstuv"
USERNAME = "nikhilesh"
GRAPH="graph1"

user_para = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response =requests.post(url=pixel_end_point,json=user_para)
# print(response.text)
# print(response.status_code)
# print(response.json())

post_graph=f"{pixel_end_point}/{USERNAME}/graphs"
graph_post={
                "id":GRAPH,
                "name":"Graph3",
                 "unit":"Minutes",
                  "type":"float",
                  "color":"shibafu"
            }
headers = {
    "X-USER-TOKEN":TOKEN
}
#
# response=requests.post(url=post_graph,json=graph_post,headers=headers)
# print(response.text)

post_2_graph= f"{pixel_end_point}/{USERNAME}/graphs/{GRAPH}"

graph =datetime.datetime.now()
f=graph.strftime("%Y%m%d")
print(f)
post_to_graph={
    "date":f,
    "quantity":"50.5"
}
#

update_quality={
"quantity":"100.0"
}
put_graph=f"{pixel_end_point}/{USERNAME}/graphs/{GRAPH}/{f}"
response = requests.put(url=put_graph,params=update_quality,headers=headers)
print(response.status_code)

#
# response = requests.post(url=post_2_graph,json=post_to_graph, headers=headers)
# print(response.text)


# delete_graph_url=f"{pixel_end_point}/{USERNAME}/graphs/{GRAPH}"
# response = requests.delete(url=delete_graph_url, headers=headers)
# print(response.text)