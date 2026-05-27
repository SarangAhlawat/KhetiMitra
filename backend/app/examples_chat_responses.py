"""
Example Scenarios - Agriculture Chat System

This file demonstrates how the enhanced agriculture chat system 
responds to various questions.
"""

# ============================================================================
# SCENARIO 1: Valid Agriculture Question - Soil Management
# ============================================================================

REQUEST_1 = {
    "user_id": 1,
    "message": "How can I improve my soil quality for better crop yield?"
}

RESPONSE_1 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

Advice: 
1. Add organic compost annually to improve soil structure and nutrient content
2. Perform soil testing to understand pH and nutrient levels
3. Practice crop rotation yearly to prevent nutrient depletion
4. Reduce chemical usage and use balanced NPK fertilizers based on soil test results

Reason: These practices build sustainable soil health, increase productivity, 
and reduce dependency on expensive chemical inputs while following government 
sustainable farming guidelines.
"""

# ============================================================================
# SCENARIO 2: Valid Agriculture Question - Pest Management
# ============================================================================

REQUEST_2 = {
    "user_id": 2,
    "message": "What natural methods can I use to manage pests in my rice field?"
}

RESPONSE_2 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

Advice:
1. Use Integrated Pest Management (IPM): Release natural predators like ladybugs
2. Spray neem oil solution early morning or evening for organic pest control
3. Practice companion planting with aromatic plants like garlic to repel pests
4. Maintain proper water and spacing to reduce pest habitat

Reason: Natural pest control is cost-effective, environmentally sustainable, 
safe for crops, and reduces chemical residue in food - aligning with modern 
agricultural standards.
"""

# ============================================================================
# SCENARIO 3: Valid Agriculture Question - Irrigation
# ============================================================================

REQUEST_3 = {
    "user_id": 3,
    "message": "Tell me about drip irrigation and its benefits"
}

RESPONSE_3 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

Advice:
1. Drip irrigation delivers water directly to roots, reducing waste by 50%
2. Set timers for early morning/evening to minimize evaporation losses
3. Monitor soil moisture with simple soil moisture meters
4. Combine with mulch to retain soil moisture and regulate temperature

Reason: Drip irrigation saves water, reduces fertilizer waste, prevents disease 
spread, and improves yield consistency - crucial for sustainable farming in 
water-scarce regions like Punjab.
"""

# ============================================================================
# SCENARIO 4: INVALID Question - Non-Agricultural (Politics)
# ============================================================================

REQUEST_4 = {
    "user_id": 4,
    "message": "What do you think about the current government policies?"
}

RESPONSE_4 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

I'm specifically designed to assist with agriculture-related questions only. 
Please ask about farming, crops, soil, water, irrigation, pests, diseases, 
or agricultural practices.
"""

# ============================================================================
# SCENARIO 5: INVALID Question - Non-Agricultural (General Knowledge)
# ============================================================================

REQUEST_5 = {
    "user_id": 5,
    "message": "What is the capital of France?"
}

RESPONSE_5 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

I'm specifically designed to assist with agriculture-related questions only. 
Please ask about farming, crops, soil, water, irrigation, pests, diseases, 
or agricultural practices.
"""

# ============================================================================
# SCENARIO 6: Valid Agriculture Question - Fertilizer Management
# ============================================================================

REQUEST_6 = {
    "user_id": 6,
    "message": "What's the right amount of fertilizer for wheat farming?"
}

RESPONSE_6 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

Advice:
1. First conduct a soil test to know current nutrient levels (N, P, K)
2. For wheat: Use 120 kg N, 60 kg P2O5, 60 kg K2O per hectare (recommended)
3. Split nitrogen application: 50% at planting, 25% at tillering, 25% at boot stage
4. Adjust based on soil test results and previous crop residues

Reason: Balanced fertilization maximizes wheat yield while preventing nutrient 
deficiency, reduces environmental pollution, and optimizes farmer investment 
in inputs.
"""

# ============================================================================
# SCENARIO 7: Valid Agriculture Question - Crop Selection
# ============================================================================

REQUEST_7 = {
    "user_id": 7,
    "message": "Which crops are best for clayey soil in Punjab?"
}

RESPONSE_7 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

Advice:
1. Recommended crops: Rice, wheat, sugarcane, and cotton perform well in clay soil
2. Before planting, add organic matter (compost) to improve drainage
3. Ensure proper water management with controlled irrigation
4. Avoid crops like maize which prefer loamy soils

Reason: Clay soil retains moisture and nutrients well but needs careful 
management of water to prevent waterlogging. These recommended crops are 
adapted to Punjab's climate and soil conditions.
"""

# ============================================================================
# SCENARIO 8: INVALID Question - Non-Agricultural (Cooking)
# ============================================================================

REQUEST_8 = {
    "user_id": 8,
    "message": "How do I cook traditional Indian rice dishes?"
}

RESPONSE_8 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

I'm specifically designed to assist with agriculture-related questions only. 
Please ask about farming, crops, soil, water, irrigation, pests, diseases, 
or agricultural practices.
"""

# ============================================================================
# SCENARIO 9: Valid Agriculture Question - Government Schemes
# ============================================================================

REQUEST_9 = {
    "user_id": 9,
    "message": "What agricultural schemes and subsidies are available for farmers?"
}

RESPONSE_9 = """
INSTRUCTIONS: I'm an Agriculture Assistant capable of helping with:
✓ Crop selection and recommendations
✓ Soil health and management  
✓ Water and irrigation planning
✓ Pest and disease management
✓ Fertilizer and nutrition advice
✓ Sustainable farming practices
✓ Government agricultural schemes
✓ Yield improvement tips
✓ Weather-based advisory

Please ask any agriculture-related question and I'll provide practical advice!

---

Advice:
1. Check PM-KISAN scheme for direct income support (₹2000/quarter)
2. Explore Soil Health Card initiative for free soil testing and recommendations
3. Apply for Pradhan Mantri Krishi Sinchayee Yojana for irrigation infrastructure
4. Visit your local agricultural office or https://agricoop.nic.in/ for latest schemes

Reason: Government schemes are designed to support farmer income, reduce input 
costs, and promote sustainable practices - farmers should leverage these benefits 
for better farm economics.
"""

# ============================================================================
# Key Observations
# ============================================================================

"""
OBSERVATIONS:

1. All valid agriculture questions:
   - Show instructions first
   - Provide practical, actionable advice
   - Explain the reasoning
   - Include sustainable practices

2. All invalid (non-agriculture) questions:
   - Show instructions first
   - Politely redirect to agriculture topics
   - Maintain consistency

3. Instructions are ALWAYS shown:
   - Consistent format
   - Clear capabilities listed
   - Encourages agriculture-related questions

4. Response Quality:
   - Questions get deep, context-aware responses
   - Includes local context (Punjab-specific advice)
   - References sustainable practices
   - Provides government scheme information

5. System Behavior:
   - Fast responses for common queries (water, soil, crop, etc.)
   - Context retrieval for detailed questions
   - Fallback knowledge base if Gemini API unavailable
   - Comprehensive error handling
"""

print(__doc__)
print("\n" + "="*80)
print("EXAMPLE SCENARIOS DEFINED")
print("="*80)
print("\nUse these scenarios to test:")
print("  python -c \"from examples import REQUEST_1, RESPONSE_1\"")
print("  or test with actual API calls using the requests above")
