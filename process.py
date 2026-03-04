import os
import sys
from pathlib import Path

from PIL import Image
from rembg import remove, new_session

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"
MODEL = os.environ.get("MODEL", "birefnet-general")
SUPPORTED = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def main():
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)

    if not input_path.exists():
        print(f"Input directory not found: {INPUT_DIR}")
        sys.exit(1)

    output_path.mkdir(parents=True, exist_ok=True)

    files = [f for f in input_path.iterdir() if f.suffix.lower() in SUPPORTED]

    if not files:
        print("No images found in input directory.")
        sys.exit(0)

    print(f"Found {len(files)} images. Model: {MODEL}")
    print("Loading model...")

    session = new_session(MODEL)

    print("Starting background removal...")

    for i, file in enumerate(sorted(files), 1):
        print(f"[{i}/{len(files)}] {file.name}", end=" ... ", flush=True)
        try:
            img = Image.open(file)
            result = remove(img, session=session)
            out_file = output_path / f"{file.stem}.png"
            result.save(out_file, "PNG")
            print("done")
        except Exception as e:
            print(f"error: {e}")
            continue
        file.unlink()

    print(f"\nFinished. Results saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
