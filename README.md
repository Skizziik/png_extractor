# PNG Extractor

Removes background from images using [rembg](https://github.com/danielgatis/rembg) (U2Net model). Runs in Docker.

## Usage

1. Put source images into `input/` folder
2. Run:

```bash
docker compose up --build
```

3. Get PNGs with transparent background in `output/`
