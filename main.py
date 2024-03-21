from openai import OpenAI
import gradio
client = OpenAI(
        api_key = "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"
)
message = [{"role": "system", "content": "You are a chatbot"}]
def chatbot(user_input):
    message.append({"role": "system", "content":user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = message)
    chatgpt_reply = response.choices[0].message.content
    message.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply

demo = gradio.Interface(fn=chatbot, inputs = "text", outputs = "text", title = "Chatbot")

demo.launch(share=True)
