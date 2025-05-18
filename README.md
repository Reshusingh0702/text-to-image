# text-to-image
# 🖼️ Text-to-Image Generation using Stable Diffusion

This project demonstrates how to generate high-quality images from text prompts using the Stable Diffusion v1.4 model via Hugging Face's `diffusers` library.

---
## 🚀 Features

- 🔁 Command-line interface for easy control
- 🧠 Customizable parameters (`guidance_scale`, `inference_steps`)
- ⚡ GPU-accelerated generation (if available)
- 📦 Lightweight and minimal codebase
- 💡 Evaluation-ready for parameter sensitivity and pipeline understanding

---

## 📂 Project Structure

text-to-image-sd/
├── text_to_image.py      # Main script
├── README.md             # Project documentation
└── output.png            # (Generated image will appear here)

---

2. Install dependencies
Ensure you have Python 3.8+ installed. 
 
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install diffusers transformers accelerate scipy safetensors

3.Usage

python text_to_image.py --prompt "a shark in ocean" --output "shark.png" --steps 50 --scale 8.5

ARGUMENTS 

| Argument   | Type    | Description                                          |
| ---------- | ------- | ---------------------------------------------------- |
| `--prompt` | `str`   | The text prompt to describe the image                |
| `--output` | `str`   | File name for the output image (default: output.png) |
| `--steps`  | `int`   | Number of denoising steps (quality control)          |
| `--scale`  | `float` | Guidance scale (alignment with prompt)               |

EVALUATION CRITERIA MAPPING 

| Criteria                    | How It's Handled                                |
| --------------------------- | ----------------------------------------------- |
| **Parameter usage**         | You control `steps`, `guidance_scale`, `prompt` |
| **Diffusers understanding** | Uses `StableDiffusionPipeline` efficiently      |
| **Output generation**       | Saves a `.png` image based on the input prompt  |


Example Output
Prompt: "a shark in ocean"
Steps: 50
Scale: 8.5

![shark](https://github.com/user-attachments/assets/cf3bb6c3-9bfc-48cc-9990-e464971006a3)

Notes
 *If your system doesn't have a CUDA-compatible GPU, the script will default to CPU, which may be very slow.

*First-time model loading may take 1–2 minutes as it downloads from Hugging Face.

*You can extend this project to a web UI using Gradio or Streamlit.

License

This project is open-source under the MIT License.

Author
Made by Reshu Singh
Feel free to contribute, report issues, or fork the repo!





