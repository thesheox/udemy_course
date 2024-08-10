import requests
from datetime import datetime

USERNAME = "thesheox"

GRAPH_ID="graph1"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

api_headers={
    "X-USER-TOKEN":TOKEN
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

pixel_create_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime(year=2024,month=8,day=7)
today_time=today.strftime("%Y%m%d")

pixel_data={
    "date":today_time,
    "quantity":"9"
}


# response=requests.post(url=pixel_create_endpoint,json=pixel_data,headers=api_headers)
# print(response.text)


update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_time}"

new_pixel_data={
    "quantity":"15"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=api_headers)
# print(response.text)


delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_time}"


response=requests.delete(url=delete_endpoint,headers=api_headers)
print(response.text)


