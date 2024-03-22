from openai import OpenAI

client = OpenAI(api_key="none", base_url="http://222.20.126.133:8000/v1")
response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {
            "role": "user",
            "content": "请回答我这条短信是否是垃圾短信，短信内容在后面的花括号中，{ 阳山碑材利用该处山体中完整性好又十分巨大的栖霞灰岩开凿出 }，你的回答只能是“是”或者“不是”。在你回答是或者不是之后，请不要再生成任何内容。你必须严格遵守我的要求，包括告诉我的任何附加信息都不要生成。",
        }
    ],
)
print(response.choices[0].message.content)
