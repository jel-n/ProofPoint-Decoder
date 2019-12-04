# Decode ProofPoint URL Defense encoded links
# November 11th, 2019
import requests
import json
import sys
import re

def intro():
    print("\nProofPoint URL Defense decoder")
    print("Enter the encoded URL and press 'Enter'")
    print("Type 'exit' to exit")
    main()

def main():
    headers = {
        "Content-Type": "application/json"
    }

    print("""
Encoded URL: 
------------""")

    try: 
        url = input()

        if (url == "exit") or (url == "Exit"):
            sys.exit()
        
        elif re.search("https://urldefense\.proofpoint\.com/", url):

            data = {"urls": [url]}

            r = requests.post("https://tap-api-v2.proofpoint.com/v2/url/decode", headers=headers, json=data)
            json_data = json.loads(r.text)

            for item in json_data["urls"]:
                for k,v in item.items():
                    if k == "decodedUrl":
                        print(f"""
Decoded URL:
------------
{v}""")
                        main()
                    else:
                        continue
        
        else:
            print(f"{url} is not an encoded URL")
            main()

    except KeyboardInterrupt:
        sys.exit()
    
    except Exception as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    intro()