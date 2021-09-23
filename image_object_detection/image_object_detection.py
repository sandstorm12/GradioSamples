import cv2
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
    x = np.random.randint(0, image.shape[1] // 2)
    y = np.random.randint(0, image.shape[0] // 2)
    
    width = np.random.randint(
        image.shape[1] // 4, image.shape[1] // 2
    )
    height = np.random.randint(
        image.shape[1] // 4, image.shape[0] // 2
    )

    cv2.rectangle(
        image, (x, y), (x + width, y + height), (0, 0, 255), 10
    )

    cv2.putText(
        image,
        'Cat',
        (x, y + height),
        cv2.FONT_HERSHEY_SIMPLEX, 
        5, (0, 0, 0), 10, cv2.LINE_AA
    )
    
    return image


input_image = gradio.inputs.Image(
    shape=None,
    image_mode="RGB",
    invert_colors=False,
    source="upload",
    tool="editor",
    type="numpy",
    label="Image for object detection",
    optional=False
)

output_image = gradio.outputs.Image(
    type="auto", labeled_segments=False, label="Annotated image"
)

iface = gradio.Interface(
    fn=process,
    inputs=input_image,
    outputs=output_image
)
iface.launch()
