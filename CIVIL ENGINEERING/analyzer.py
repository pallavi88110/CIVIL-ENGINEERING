from ultralytics import YOLO
import os

# Use official pretrained YOLO model
model = YOLO("yolov8n.pt")  # Auto-downloads first time


def analyze_image(image_path):
    results = model(image_path)

    detected_objects = []

    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                cls_id = int(box.cls.cpu().numpy()[0])
                label = model.names[cls_id]
                detected_objects.append(label)

    return generate_report(detected_objects)


def generate_report(objects):
    report = "---- Civil Engineering Insight Report ----\n\n"

    unique_objects = list(set(objects))

    if len(unique_objects) == 0:
        report += "No major structural components detected.\n"
    else:
        report += "Detected Objects:\n\n"
        for obj in unique_objects:
            report += f"• {obj}\n"

    return report
