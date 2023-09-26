import requests
from requests.exceptions import HTTPError
from pprint import pprint

def analyse_status_code_with_exception(response):
    try:
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as ex:
        print(f"HTTP error occurred: {ex}")
    except Exception as ex:
        print(f"Other error occurred: {ex}")
    else:
        print(f"All good : code {response.status_code}")

def analyse_status_code(response):
    print(response)
    if 200 <= response.status_code <= 208:
        print(f"All good : code {response.status_code}")
    elif 400 <= response.status_code <= 451:
        print(f"Error from your HTTP request : code {response.status_code}")
    elif 500 <= response.status_code <= 511:
        print(f"Error from the server : code {response.status_code}")
    else:
        print(f"code {response.status_code}")

def get_data_from_github():
    response = requests.get(
        "https://api.github.com",
        params={"repo": ""}
    )
    analyse_status_code(response)
    analyse_status_code_with_exception(response)

    # pprint(response.content) # Bytes of content
    # pprint(response.text)    # Content in text format (utf-8)
    pprint(response.json())  # Content in JSON format
    pprint(response.headers) # Headers contain all request"s info

    response = requests.get(
        "https://api.github.com/search/users",
        params={"q": "Rekoc"}
    )
    # pprint(response.json())
    json_content = response.json()
    pprint(json_content)
    for user in json_content["items"]:
        name, url = user["login"], user["repos_url"]
        print(f"Username: {name} --> {url}")

def main():
    response = requests.get("https://httpbin.org/get")
    # pprint(response.json())
    response = requests.post(
        "https://httpbin.org/post",
        data={
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }
    )
    pprint(response.json())
    response = requests.put(
        "https://httpbin.org/put",
        data={
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }
    )
    # pprint(response.json())
    response = requests.delete("https://httpbin.org/delete")
    # pprint(response.json())
    response = requests.head("https://httpbin.org/get")
    # pprint(response.json())
    response = requests.patch(
        "https://httpbin.org/patch",
        data={"key2": "1234"}
    )
    # pprint(response.json())
    response = requests.options("https://httpbin.org/get")
    # pprint(response.json())

if __name__ == "__main__":
    get_data_from_github()
    # main()