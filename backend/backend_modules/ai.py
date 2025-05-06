from backend.constants import AI_API_KEY
import google.generativeai as genai

genai.configure(api_key=AI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_response(prompt: str) -> str:
    """
    Generates a response from the AI model based on the provided prompt.

    Args:
        prompt (str): The input prompt for the AI model.

    Returns:
        str: The generated response from the AI model.
    """
    response = model.generate_content(prompt)
    return response.text

def generate_planet_description(description: str) -> str:
    """
    Generates a description for a planet based on the provided description.

    Args:
        description (str): The input description for the planet.

    Returns:
        str: The generated planet description.
    """
    prompt = f"Summarize the given exoplanet data into a single, concise descriptive paragraph. Include the planet's name, location , size compared to Earth, likely classification (e.g., super-Earth, mini-Neptune), orbital period, estimated temperature, and habitability potential. Compare the planet to Earth and at least one other well-known planet (such as Mercury, Neptune, or Jupiter) to highlight key differences. Use metric units and Celsius for temperature. Keep the tone clear, scientific, and suitable for a general audience. Limit the paragraph to 6-7 sentences: {description} if there is information that you do not have do not make it up, and do not mention it in the response. Do not use any formatting other than a standard single paragraph structure. Do not reference the planet by id or system id."
    return generate_response(prompt)


def generate_star_description(description: str) -> str:
    """
    Generates a description for a star based on the provided description.

    Args:
        description (str): The input description for the star.

    Returns:
        str: The generated star description.
    """
    prompt = f"Summarize the given star data into a single, concise descriptive paragraph. Include the stars's name, location , size compared to our sun, likely classification (e.g., red dwarf), orbital period, estimated temperature, and habitability zone potential. Compare the star to the sun and at least one other well-known star or even a fictional star from popular media to highlight key differences. Use metric units and Celsius for temperature. Keep the tone clear, scientific, and suitable for a general audience. Limit the paragraph to 6-7 sentences: {description} if there is information that you do not have do not make it up, and do not mention it in the response. Do not use any formatting other than a standard single paragraph structure. Do not reference the star by id or system id."
    return generate_response(prompt)
