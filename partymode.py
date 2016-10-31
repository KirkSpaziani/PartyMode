import argparse
import json
import requests
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Start the Party.")
    parser.add_argument('ip', help='IP Address of Hue Bridge.')
    parser.add_argument('username', help='Username for the API.')
    parser.add_argument('lights', help='Comma separated list of lights 1,2,3,4')
    parser.add_argument('--disable', help='Disable Partymode', action='store_true')
    parser.add_argument('--delay', type=int, help='Seconds between each request.')
    args = parser.parse_args()
    print args.lights

    lights = [int(light) for light in args.lights.split(',')]
    print lights 

    url = 'http://{ip}/api/{username}/lights/{light}/state'
    body = json.dumps({'effect': 'none' if args.disable else 'colorloop'})
    for light in lights:
        light_url = url.format(ip=args.ip, username=args.username, light=light)
        response = requests.put(light_url, data=body)
        print response.text
        if args.delay:
            time.sleep(args.delay)

