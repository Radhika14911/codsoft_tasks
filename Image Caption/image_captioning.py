from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("Loading AI model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded successfully!")

while True:
    image_path = input("Enter image path (q to quit): ")

    if image_path.lower() == "q":
        break

    image = Image.open(image_path)

    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=30)

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    print("Caption:", caption)