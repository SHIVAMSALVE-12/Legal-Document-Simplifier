from llama_cpp import Llama

llm = Llama(
    model_path="C:\Projects\legal-document-simplifier\models\qwen2.5-7b-instruct-q4_k_m.gguf",
    n_gpu_layers=-1,
    n_ctx=4096
)