from llama_cpp import Llama

llm = Llama(
    model_path="models/qwen2.5-7b-instruct-q4_k_m.gguf",
    n_gpu_layers=-1,
    n_ctx=4096,
    verbose=False
)

def generate_response(prompt):

    response = llm.create_chat_completion(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a legal document analysis assistant. "
                    "Give concise answers. "
                    "Do not repeat sentences."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=200,
        stop=[
            "<|im_end|>",
            "<|endoftext|>"
        ]
    )

    return response["choices"][0]["message"]["content"]