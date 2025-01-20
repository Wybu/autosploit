import shodan
import yaml

def load_config():
    with open('config/setting.yaml') as f:
        return yaml.safe_load(f)
    
def shodan_search(query):
    config = load_config()
    api_key = config['shodan']['RXZwXHR29sggO5GJzAbqF6kUfp2ZrkOM']
    api = shodan.Shodan(api_key)
    
    try:
        print('Searching for: {}'.format(query))
        results = api.search(query)
        for result in results['matches']:
            print(f"IP: {result['ip_srt']} \nPort: {result['port']} \nData: {result['data']}")
        return results['matches']
    except Exception as e:
        print('Error: {}'.format(e))
        return None
    
            