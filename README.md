# PNG Extractor

Open-source batch background removal tool powered by [BiRefNet](https://github.com/ZhengPeng7/BiRefNet) via [rembg](https://github.com/danielgatis/rembg). Runs locally in Docker with NVIDIA GPU acceleration.

## Features

- GPU-accelerated inference (NVIDIA CUDA)
- Batch processing — drop a folder of images, get PNGs with transparent backgrounds
- Supports JPG, PNG, WEBP, BMP, TIFF
- Auto-deletes originals after successful processing
- Configurable model via environment variable

## Requirements

- Docker with [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
- NVIDIA GPU (tested on RTX 4060)

## Usage

1. Put source images into `input/`
2. Run:

```bash
docker compose up --build
```

3. Get PNGs with transparent background in `output/`

First run downloads the BiRefNet model (~1 GB), subsequent runs use cache.

## Configuration

Change the model via environment variable in `docker-compose.yml`:

```yaml
environment:
  - MODEL=birefnet-massive
```

Available models: `birefnet-general` (default), `birefnet-massive`, `isnet-general-use`, `u2net`

## License

MIT
