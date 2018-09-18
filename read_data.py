def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def read_data(folder: str):
    if not folder.endswith('/'):
        folder = folder+'/'
    return [read_file(folder+file) for file in os.listdir(folder)]