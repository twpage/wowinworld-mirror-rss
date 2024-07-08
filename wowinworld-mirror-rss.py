import requests
import xml.etree.ElementTree as ET
import re, os, copy
# from collections import OrderedDict


RSS_FEED_PATH = r"https://rss.art19.com/wow-in-the-world"


def fetch_and_parse_xml(url):
    try:
        # Fetch the XML data from the remote URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the XML data
        root = ET.fromstring(response.content)
        
        return root
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the XML file: {e}")
    except ET.ParseError as e:
        print(f"Error parsing the XML data: {e}")

def check_filter(xml_element: ET.Element):
    if xml_element.tag != "item": 
        assert 0 == 1
    
    episode_title = xml_element.find('title').text
    if 'Two Whats' in episode_title:
        return True
    
    return False

def prune_xml(xml_root):
    # display(xml_root)
    channel_root = xml_root.find('channel')
    for episode_node in channel_root.findall('.//item'):
        is_filtered_out = check_filter(episode_node)
        if is_filtered_out:
            channel_root.remove(episode_node)
    
    return xml_root

def print_xml_elements(root):
    # Convert the XML element back to a string
    xml_str = ET.tostring(root, encoding='unicode')
    # xml_str = re.sub("ns(\d)\:", "itunes:", xml_str)
    xml_str = xml_str.replace(
        "<title>Wow in the World</title>", 
        "<title>KJ in the World</title>"
    )

    return xml_str

def main():    
    root = fetch_and_parse_xml(RSS_FEED_PATH)

    modified_root = prune_xml(copy.deepcopy(root))

    open(os.path.join(os.getcwd(), "wow-original.rss"), 'w', encoding='utf-8').write(print_xml_elements(root))

    modified_xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + print_xml_elements(modified_root)
    open(os.path.join(os.getcwd(), "wow-modified.rss"), 'w', encoding='utf-8').write(modified_xml_str)
    print("dunzo")
  
if __name__ == '__main__':
    main()
    