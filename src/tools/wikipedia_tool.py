from crewai.tools import BaseTool
import requests

# Tool utilizada pelo o agente pesquisador para buscar informações na Wikipedia.
class WikipediaTool(BaseTool):
    name: str = "WikipediaTool"
    description: str = "Busca informações relevantes na Wikipedia em português para o artigo especificado."

    def _run(self, query: str) -> str:
        try:
            url = (
                "https://pt.wikipedia.org/w/api.php"
                "?action=query&prop=extracts&explaintext=1"
                f"&titles={query}&format=json&utf8=1&redirects=1"
            )
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; CrewAI-Bot/1.0; +https://wikipedia.org)"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            text = next(iter(pages.values())).get("extract", "")
            return text[:16000] if text else "Nenhum resultado encontrado."
        except Exception as e:
            return f"Erro ao buscar informações na Wikipedia: {e}"