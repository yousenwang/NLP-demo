import requests

r = requests.post(
    url='http://127.0.0.1:8000',
    json = {
        "user_input": "What is the work station?"
    }
    )
# r = requests.get('http://127.0.0.1:8000')

print(r.content)