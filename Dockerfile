FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 libgl1-mesa-glx libglib2.0-0 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install DORI inference library and PyYAML
RUN pip install --no-cache-dir torch https://vocr.vn/data/dori-2.0-py3-none-any.whl pyyaml colorama
RUN pip install --no-cache-dir anytree tokenizers six transformers onnxruntime
# Copy application files
COPY . /app

# Default entrypoint to run the recognition script
ENTRYPOINT ["python", "/app/rec.py"]
# Default arguments: image file and model directory
CMD ["test.jpg", "--model_dir", "model"]
