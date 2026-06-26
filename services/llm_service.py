from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)


class LLMService:

    def generate(self, system_prompt, user_prompt):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0.3,
            max_tokens=700
        )

        return response.choices[0].message.content