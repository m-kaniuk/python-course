import json

import requests

headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json",
}
response = requests.get("https://app.eu0.signalfx.com/v2/chart", headers=headers)
print(response.text)


body = {"name": "my_dashboard_group_1"}
response = requests.post(
    "https://app.eu0.signalfx.com/v2/dashboardgroup",
    headers=headers,
    data=json.dumps(body),
)
print(response.status_code)
print(response.text)

body = {"name": "my_dashboard_1", "groupId": "GUxl1WMAEAA"}
response = requests.post(
    "https://app.eu0.signalfx.com/v2/dashboard", headers=headers, data=json.dumps(body)
)
print(response.status_code)
print(response.text)

body = {
    "name": "my_chart_restarts",
    "programText": "A = data('k8s.container.restarts').publish(label='A')",
}
response = requests.post(
    "https://app.eu0.signalfx.com/v2/chart", headers=headers, data=json.dumps(body)
)
print(response.status_code)
print(response.text)

body = {
    "name": "my_chart_restarts",
    "charts": [
        {"chartId": "GUxsrRZAEAA", "column": 0, "height": 2, "row": 3, "width": 6}
    ],
    "groupId": "GUxl1WMAEAA",
}
response = requests.put(
    "https://app.eu0.signalfx.com/v2/dashboard/GUxl1XmAIAA",
    headers=headers,
    data=json.dumps(body),
)
print(response.status_code)
print(response.text)
