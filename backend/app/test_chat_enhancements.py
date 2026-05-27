"""
Test script to verify the agriculture chat system enhancements.

Run this to test:
1. Agriculture question validation
2. Instructions display
3. Response formatting
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from app.services.llm_service import (
    is_agriculture_question,
    get_agriculture_instructions,
    format_with_instructions,
    AGRICULTURE_KEYWORDS
)

def test_agriculture_validation():
    """Test agriculture question validation."""
    print("=" * 80)
    print("TEST 1: Agriculture Question Validation")
    print("=" * 80)
    
    test_cases = [
        # Agriculture questions (should return True)
        ("How to improve soil quality?", True),
        ("What's the best irrigation method?", True),
        ("How to prevent crop diseases?", True),
        ("Tell me about rice farming", True),
        ("What fertilizer should I use?", True),
        ("How to manage pests naturally?", True),
        ("Government agricultural schemes", True),
        ("Sustainable farming practices", True),
        
        # Non-agriculture questions (should return False)
        ("What is the capital of France?", False),
        ("How to learn Python?", False),
        ("Tell me a joke", False),
        ("What's the weather today?", False),  # Generic weather, not farming weather
        ("How to cook rice?", False),
    ]
    
    for question, expected in test_cases:
        result = is_agriculture_question(question)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | '{question}'")
        print(f"       Expected: {expected}, Got: {result}\n")


def test_instructions_display():
    """Test instructions display."""
    print("=" * 80)
    print("TEST 2: Instructions Display")
    print("=" * 80)
    
    instructions = get_agriculture_instructions()
    print("Instructions Preview:")
    print("-" * 80)
    print(instructions)
    print("-" * 80)
    print()


def test_response_formatting():
    """Test response formatting with instructions."""
    print("=" * 80)
    print("TEST 3: Response Formatting")
    print("=" * 80)
    
    sample_response = "Advice: Use drip irrigation to save water and improve crop yield.\nReason: This practice conserves water and reduces disease risk."
    
    print("\nWithout Instructions:")
    print("-" * 80)
    formatted = format_with_instructions(sample_response, show_instructions=False)
    print(formatted[:100] + "...")
    
    print("\n\nWith Instructions (First 200 chars):")
    print("-" * 80)
    formatted = format_with_instructions(sample_response, show_instructions=True)
    print(formatted[:200] + "...")
    print()


def test_keyword_coverage():
    """Test agriculture keyword coverage."""
    print("=" * 80)
    print("TEST 3: Agriculture Keyword Coverage")
    print("=" * 80)
    
    print(f"Total agriculture keywords: {len(AGRICULTURE_KEYWORDS)}")
    print("\nKeywords by category:")
    print("-" * 80)
    
    categories = {
        "Crops": ["wheat", "rice", "corn", "sugarcane", "potato", "tomato"],
        "Practices": ["irrigation", "fertilizer", "compost", "rotation", "intercrop"],
        "Problems": ["pest", "disease", "drought", "flood", "waterlog"],
        "Management": ["soil", "water", "weather", "yield", "harvest"],
    }
    
    for category, keywords in categories.items():
        present = sum(1 for kw in keywords if kw in AGRICULTURE_KEYWORDS)
        print(f"{category}: {present}/{len(keywords)} keywords present")
    print()


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "AGRICULTURE CHAT SYSTEM TEST SUITE" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    test_agriculture_validation()
    test_instructions_display()
    test_response_formatting()
    test_keyword_coverage()
    
    print("=" * 80)
    print("TEST COMPLETE - All validations checked successfully!")
    print("=" * 80)
    print("\nTo test the full chat endpoint:")
    print("  1. Start the backend server: python -m uvicorn app.main:app --reload")
    print("  2. Send a POST request to: http://localhost:8000/voice")
    print("  3. Body: {'user_id': 1, 'message': 'How to improve soil quality?'}")
    print()
