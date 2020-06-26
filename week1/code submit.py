import requests
url='https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'
x=requests.post(url,json={"qconfig":"3 1 6 4 0 7 5 2","userID":694547,"githubLink":""})
print(x.text)