import requests

def fetch_customer_profile(email):
    # Hypothetical API endpoint
    api_url = f"https://api.example.com/customer_profile?email={email}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data.get('profile_info', {})
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return {}
