import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    # Fetch the HTML content from the specified URL
    url = 'https://time.com'
    response = requests.get(url)
    html_content = response.text

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the latest 6 stories based on the HTML structure
    latest_stories = []
    stories_elements = soup.select('.latest-stories .swipe-container .card')

    for story_element in stories_elements[:6]:
        title = story_element.select_one('.headline').get_text(strip=True)
        link = story_element.select_one('a')['href']
        latest_stories.append({'title': title, 'link': link})

    # Return the latest 6 stories as a JSON response
    return jsonify(latest_stories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
