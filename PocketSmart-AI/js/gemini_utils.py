import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def get_home_recommendations(budget, room, style):
    prompt = f"""
    You are PocketSmart AI.

    User Budget: ₹{budget}
    Room: {room}
    Style: {style}

    Give budget-friendly home interior recommendations.

    Include:
    1. Product name
    2. Category
    3. Approximate price
    4. Reason for recommendation

    Keep the total estimated cost within the user's budget.
    """

    response = model.generate_content(prompt)

    return response.text


def get_party_recommendations(budget, guests, event_type, venue):
    prompt = f"""
    You are PocketSmart AI.

    Budget: ₹{budget}
    Guests: {guests}
    Event Type: {event_type}
    Venue: {venue}

    Create a party budget plan.

    Include:
    1. Food
    2. Decoration
    3. Entertainment
    4. Venue
    5. Estimated cost

    Keep the total cost within the given budget.
    """

    response = model.generate_content(prompt)

    return response.text


def get_jewelry_recommendations(budget, occasion, style):
    prompt = f"""
    You are PocketSmart AI.

    Budget: ₹{budget}
    Occasion: {occasion}
    Style: {style}

    Recommend suitable jewelry.

    Include:
    1. Jewelry type
    2. Style
    3. Approximate price
    4. Reason

    Keep recommendations within the budget.
    """

    response = model.generate_content(prompt)

    return response.text