from llama_cpp import Llama

llm = Llama(
    model_path="ADD YOUR PATH OF THE DOWNLOADED MODEL",
    n_gpu_layers=-1,
    n_ctx=4096
)
