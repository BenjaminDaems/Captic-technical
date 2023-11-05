import json
import pathlib
import sys

import cv2


def save_metadata(filepath, image):
	metadata = {
		"filename": filepath.name,
		"width": image.shape[1],
		"height": image.shape[0],
		"channels": image.shape[2],
		"filetype": filepath.suffix.replace(".", ""),
		"filesize": filepath.stat().st_size,
	}

	metadata_filepath = pathlib.Path("/app/output", f"{filepath.stem}.json")
	with open(metadata_filepath, "w") as f:
		json.dump(metadata, f)




def main():
	args = sys.argv[1:]
	if len(args) != 1:
		print("Usage: python main.py <filepath>")
		sys.exit(1)
	try:
		filepath = pathlib.Path(f"/app/images/{args[0]}").resolve(strict=True)
	except FileNotFoundError:
		print("File not found")
		sys.exit(1)

	image = cv2.imread(str(filepath))
	save_metadata(filepath, image)


if __name__ == "__main__":
	main()
