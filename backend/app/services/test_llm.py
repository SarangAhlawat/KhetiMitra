from app.services.llm_service import generate_response

def test_llm():
    print(generate_response("Explain drip irrigation in simple terms."))

if __name__ == "__main__":
    test_llm()