import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

def load_model(model_name="CompVis/stable-diffusion-v1-4"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading model on: {device.upper()}")

    pipe = StableDiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    pipe.to(device)
    print("Model loaded successfully.")
    return pipe


def generate_image(pipe, prompt, output_path="output.png", guidance_scale=7.5, num_inference_steps=50):
    print(f"Generating image for prompt: {prompt}")
    image = pipe(prompt, guidance_scale=guidance_scale, num_inference_steps=num_inference_steps).images[0]
    image.save(output_path)
    print(f"Image saved at: {output_path}")
    return image

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate an image from a text prompt using Stable Diffusion")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt to generate the image")
    parser.add_argument("--output", type=str, default="output.png", help="Output image file path")
    parser.add_argument("--steps", type=int, default=50, help="Number of inference steps")
    parser.add_argument("--scale", type=float, default=7.5, help="Guidance scale (higher = more aligned with prompt)")

    args = parser.parse_args()

    model_pipeline = load_model()
    generate_image(model_pipeline, args.prompt, output_path=args.output, 
                   guidance_scale=args.scale, num_inference_steps=args.steps)