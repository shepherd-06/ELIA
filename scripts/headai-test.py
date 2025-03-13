import requests

def send_post_request(url, api_key):
    headers = {
        '$API-key': f'{api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "token": api_key,
  "language": "en",
  "ontology": "headai",
  "dataset": "https://google.com/",
  "legend": "Graph legend",
  "search_text": "Graph legend",
  "search_year": 2024,
  "search_month": 1,
  "search_day": 1,
  "word_type": "only_compounds",
  "country": "fi",
  "city": "Pori",
  "size": 10,
  "weighted_search_output": False,
  "affiliation": "",
  "additional_data": False,
  "output": "json",
  "update": False,
  "use_stored_noise": False,
  "noise_list": ""
}
    
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    return response.json()

# Example usage
url = 'https://megatron.headai.com/TextToGraph'  # Replace with the actual URL
api_key = 'FD2y2ABxIGi9TW4oiDClG3GaDiAP5htO'  # Replace with your actual API key
result = send_post_request(url, api_key)
print(result)
