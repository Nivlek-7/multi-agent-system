# Sistema Multiagentes para Geração de Artigos Utilizando CrewAI 

Este projeto implementa um sistema multiagente para geração de artigos utilizando a **CrewAI** com o uso da LLM do **Gemini**, onde o usuário informa um tópico através da API desenvolvida com a **FastAPI** e é devolvido à ele um artigo de opinião para ser publicado em um website. O sistema conta com 3 agentes: pesquisador, escritor e revisador.

O projeto inclui uma ferramenta personalizada (`WikipediaTool`) que permite ao agente buscar informações atualizadas na **Wikipedia**.

---

## Visão Geral

A aplicação tem o seguinte fluxo de trabalho:

1. O **usuário** faz uma requisição HTTP `GET /artigo?topico=...` para a API.  
2. A rota solicitada (em `routes.py`) envia o tópico para o serviço `crew_service.py`.  
3. O serviço instancia e aciona a tripulação, composto pelos os seguintes agentes com suas respectivas tarefas:  
   - **Pesquisador:** faz uma busca com `WikipediaTool`, analisa e retorna dados relevantes. 
   - **Escritor:** usa esses dados, e retorna o texto base do artigo.
   - **Revisador:** reinforça alguns pontos e melhora a estrutura do texto.
4. O artigo final é consolidado e retornado como **resposta JSON** ao usuário com o uso do pydantic.

---

## Estrutura do Projeto

```
multi_agent_system/
│
├── src/
│   ├── agents/                     # Contém os agentes e as tarefas que compõem o sistema multiagente CrewAI
│   │   ├── escritor_agent.py
│   │   ├── pesquisador_agent.py
│   │   └── revisor_agent.py
│   │
│   ├── api/
│   │   └── routes.py               # Define as rotas FastAPI (/, /artigo)
│   │
│   ├── models/
│   │   └── artigo_model.py         # Define o modelo de dados, a estrutura do artigo
│   │
│   ├── services/
│   │   └── crew_service.py         # Centraliza a lógica de criação e execução do CrewAI
│   │
│   └── tools/
│       └── wikipedia_tool.py       # Tool personalizada para consultas à API da Wikipedia.
│
├── .env                            # Configurações de ambiente e chaves de API.
├── main.py                         # Ponto de entrada do app (instancia a FastAPI e inclui as rotas)
└── pyproject.toml                  # Configuração do projeto e dependências.
```

---

## Dependências Principais

- **Python 3.10+**
- **FastAPI**
- **CrewAI**
- **google-generativeai**
- **Uvicorn**

---

## Instalação

```bash
git clone https://github.com/Nivlek-7/multi-agent-system.git
cd multi-agent-system
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
pip install -e .
```

---

## Configuração do Ambiente

Crie um arquivo `.env` na raiz:

```env
LLM_PROVIDER=google
GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
CREWAI_LLM=google/gemini-2.5-flash
```

---

## Execução da API

```bash
uvicorn src.main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

---

## Endpoints

### **GET /**

```bash
curl http://127.0.0.1:8000/
```

**Resposta:**
```json
{"message": "Gerador de Artigo CrewAI está online!"}
```

---

### **GET /artigo**

```bash
curl "http://127.0.0.1:8000/artigo?topico=África"
```

**Resposta:**
```json
{
  "title": "África",
  "content": "A África é o segundo maior continente em extensão territorial..."
}
```
