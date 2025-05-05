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
    prompt = f"""
        Generate a detailed description of a planet based on the following information. Keep the description to a couple medium paragraphs, and don't use any unusual formatting. {description}
    """
    return generate_response(prompt)


def generate_star_description(description: str) -> str:
    """
    Generates a description for a star based on the provided description.

    Args:
        description (str): The input description for the star.

    Returns:
        str: The generated star description.
    """
    prompt = f"Generate a detailed description of a star based on the following information. Keep the description to a couple medium paragraphs, and don't use any unusual formatting. {description}"
    return generate_response(prompt)
