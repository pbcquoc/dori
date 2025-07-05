# DORI
This is inference library for [DORI](https://dorify.net/)
<div align="center">
  <a href="https://www.youtube.com/watch?v=gEOR42B4KzY">
    <img src="https://img.youtube.com/vi/gEOR42B4KzY/maxresdefault.jpg" alt="Watch the video" width="640">
    <br>
    ▶️ Watch Demo
  </a>
</div>

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
python rec.py test.jpg --model_dir ./models
```

The script will print the recognition results to the console. The output will be a list of dictionaries, where each dictionary contains the recognized text, its probability, and other information.

## Docker Usage

### Building the Docker Image
```bash
docker build -t dori-inference .
```

### Running with Docker
Run the container with the default test image:
```bash
docker run --rm dori-inference
```

To process your own image and model directory:
```bash
docker run --rm -v "$(pwd)":/app dori-inference /app/path/to/image.jpg --model_dir /app/model
```

### Using Docker Compose
Alternatively, you can use Docker Compose to build and run the service:
```bash
docker-compose up --build
```

To run inference on a custom image using Docker Compose:
```bash
docker-compose run --rm dori-inference python rec.py /app/your_image.jpg --model_dir /app/model
```
