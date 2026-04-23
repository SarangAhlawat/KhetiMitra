import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def test_llm():

    payload = {
        "model": "phi3",
        "prompt": "Explain drip irrigation in simple terms.",
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    result = response.json()

    print(result["response"])

if __name__ == "__main__":
    test_llm()