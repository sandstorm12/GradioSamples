import gradio
import numpy as np


NUM_TOP_CLASSES = 5
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
    detection_results = {}

    labels = np.random.choice(LABELS, size=NUM_TOP_CLASSES)

    detection_results = {
        labels[i]: np.random.rand() for i in range(NUM_TOP_CLASSES)
    }
    
    return detection_results


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

output_label = gradio.outputs.Label(
    num_top_classes=NUM_TOP_CLASSES,
    type="auto",
    label="Classification results"
)

iface = gradio.Interface(
    fn=process,
    inputs=input_image,
    outputs=output_label
)
iface.launch()
