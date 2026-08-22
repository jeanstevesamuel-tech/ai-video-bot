from google import genai
import os


def main():
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    prompt = """
Tu es le premier agent de notre AI Video Bot.

Crée une idée de vidéo YouTube courte et intéressante.
Donne :
1. Le titre
2. Le concept
3. Le scénario
4. Les scènes
5. Une description YouTube

Sujet : Les inventions qui ont changé le monde.
"""

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    print(response.text)


if __name__ == "__main__":
    main()
