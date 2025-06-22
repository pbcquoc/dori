from dori import OCR
import os
import yaml
from typing import Any, Dict
import argparse

def load_model(model_dir):
    """
    Load OCR model
    """

    det_model = os.path.join(model_dir, "det.onnx")
    rec_model = os.path.join(model_dir, "model.onnx")
    rec_char = os.path.join(model_dir, "chars.txt")
    det_config = os.path.join(model_dir, "config_det.yml")
    det_config = yaml.load(open(det_config, "r"), Loader=yaml.FullLoader)

    model = OCR(
        use_angle_cls=False,
        lang="vi",
        det_model_dir=det_model,
        rec_model_dir=rec_model,
        rec_char_dict_path=rec_char,
        rec_image_shape="3, 32, 400",
        det_db_unclip_ratio=det_config["PostProcess"]["unclip_ratio"],
    )

    print("Model loaded successfully!")
    return model

def predict(
    model,
    file: str,
    det: bool =True,
    rec: bool = True,
    cls: bool = False
) -> Dict[str, Any]:
    """
    Predict text from image
    """
    image_bytes = open(file, "rb").read()

    # Create param dict for OCR
    params = {"det": det, "rec": rec, "cls": cls}

    model_output = model.ocr(image_bytes, **params)[0]
    if det and rec:
        output_data = [
            {
                "points": points,
                "text": text,
                "prob": prob,
                "block_type": block_type,
                "parent": parent_id,
            }
            for points, (text, prob), block_type, parent_id in model_output
        ]
    else:
        output_data = [
            {
                "text":text,
                "prob": prob
            }
            for text, prob in model_output
            ]

    return output_data

def main(model_dir, file):
    model = load_model(model_dir)
    output_data = predict(model, file)
    print(output_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, default="test.jpg")
    parser.add_argument("--model_dir", type=str, default="model")
    args = parser.parse_args()
    main(args.model_dir, args.file)