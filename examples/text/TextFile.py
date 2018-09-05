class TextFile:
    count = 0
    def __init__(self, file: str) -> None:
        self.file = file

    def read(self) -> list:
        with open(self.file) as f:
            self.string = f.read()
        TextFile.count += 1

    def reset(self) -> None:
        del self.string
        TextFile.count -= 1
