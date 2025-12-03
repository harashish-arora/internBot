import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 en.example.com/6cFT3415_3.9.2 (BA700, Android 10, Ordering)'
}

response = requests.get('https://www.google.com', headers = header)

soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text().strip().split()

genai.configure(api_key = "API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')
