import os
# 升级方舟 SDK 到最新版本 pip install -U 'volcengine-python-sdk[ark]'
from volcenginesdkarkruntime import Ark
import sys
# 获取当前文件的绝对路径，然后获取其上一级目录（项目根目录）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 现在可以导入 config 里的内容
from config.config import ARK_API_KEY


client = Ark(
    # 从环境变量中读取您的方舟API Key
    api_key=ARK_API_KEY, 
    # 深度推理模型耗费时间会较长，请您设置较大的超时时间，避免超时，推荐30分钟以上
    timeout=1800,
    )
response = client.chat.completions.create(
    # 替换 <Model> 为模型的Model ID
    model="deepseek-r1-distill-qwen-32b-250120",
    messages=[
        {"role": "user", "content": "我要有研究推理模型与非推理模型区别的课题，怎么体现我的专业性"}
    ]
)
# 当触发深度推理时，打印思维链内容
if hasattr(response.choices[0].message, 'reasoning_content'):
    print(response.choices[0].message.reasoning_content)
print(response.choices[0].message.content)