../llama.cpp/build/bin/llama-mtmd-cli \
  -m Qwen3-VL-2B-Instruct-GGUF/Qwen3VL-2B-Instruct-Q8_0.gguf \
  --mmproj Qwen3-VL-2B-Instruct-GGUF/mmproj-Qwen3VL-2B-Instruct-F16.gguf \
  --image a.jpg \
  -p "What is the publisher name of the newspaper?" \
  --temp 0.7 --top-k 20 --top-p 0.8 -n 1024
