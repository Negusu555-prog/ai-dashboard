
from tavily import TavilyClient
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str) -> str:
    """
    מחפש מידע באינטרנט על בסיס שאלה.
    מחזיר תקציר של התוצאות.
    """
    results = tavily.search(query=query, max_results=3)
    
    output = ""
    for r in results["results"]:
        output += f"כותרת: {r['title']}\n"
        output += f"תוכן: {r['content']}\n\n"
    
    return output


def summarize_url(url: str) -> str:
    """
    מושך את תוכן דף האינטרנט מה-URL ומחזיר את הטקסט.
    """
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # שולף רק את הטקסט, בלי HTML
    text = soup.get_text(separator="\n", strip=True)
    
    # מחזיר רק 3000 תווים ראשונים כדי לא להציף את ה-LLM
    return text[:3000]