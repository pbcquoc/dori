# dori
This is inference library for DORI https://dorify.net/
## Install dori inference
```
pip install https://vocr.vn/data/dori-2.0-py3-none-any.whl
```
## Example for running recognition model
To run the recognition model, you can use the `rec.py` script.

### Usage
```bash
python rec.py [image_file] --model_dir [path_to_model_directory]
```

### Arguments
- `image_file`: Path to the image you want to process.
- `--model_dir`: Path to the directory containing the model files. Defaults to `model`.

### Example
```bash
python rec.py my_image.jpg --model_dir ./models
```

The script will print the recognition results to the console. The output will be a list of dictionaries, where each dictionary contains the recognized text, its probability, and other information.
