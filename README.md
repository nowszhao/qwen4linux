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

```
