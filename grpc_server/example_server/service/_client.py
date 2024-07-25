__all__ = ["SaveImageClient"]


class SaveImageClient:
    _image_path: str

    def __init__(self, image_path: str) -> None:
        self._image_path = image_path

    def __call__(self, filename: str, image: bytes) -> None:
        with open(f"{self._image_path}/{filename}", "wb") as file:
            file.write(image)
