https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct-GGUF

```
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release

cd ..
git clone https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct-GGUF 


python3 -m venv venv
source venv/bin/activate
pip install openai

curl --request POST     --url http://localhost:8080/completion     --header "Content-Type: application/json"     --data '{"prompt": "Building a website can be done in 10 simple steps:","n_predict": 128}'

curl http://9.208.244.74:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-VL-2B-Instruct",
    "messages": [
      {
        "role": "user",
        "content": [
          { "type": "text", "text": "请描述这张图片" },
          {
            "type": "image_url",
            "image_url": {
              "url": "http://9.208.244.74:9876/a.jpg"
            }
          }
        ]
      }
    ],
    "max_tokens": 200
  }'

```
