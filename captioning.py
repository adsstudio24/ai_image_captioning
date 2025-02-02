import openai

openai.api_key = "your-api-key-here"

def generate_caption(image_url):
    prompt = f"Опиши це зображення: {image_url}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response["choices"][0]["text"].strip()

image = "https://example.com/image.jpg"
print("Опис зображення:", generate_caption(image))
