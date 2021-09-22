import gradio
import numpy as np


LABELS = [
    "Cat",
    "Dog",
    "Car",
    "Person",
    "Building",
    "Bag",
    "Truck",
    "Flower"
]


def process(image):
    random_choice = np.random.choice(LABELS)
    caption = "There is a {} in this image".format(
        random_choice
    )
    
    return caption


input_image = gradio.inputs.Image(
    shape=None,
    image_mode="RGB",
    invert_colors=False,
    source="upload",
    tool="editor",
    type="numpy",
    label="Image to be classified",
    optional=False
)

output_text = gradio.outputs.Textbox(
    type="auto", label="Caption"
)

iface = gradio.Interface(
    fn=process,
    inputs=input_image,
    outputs=output_text
)
iface.launch()
