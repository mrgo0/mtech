class Pyramid:
    def __init__(self, pyramid):
        self.pyramid = pyramid

    
    def compress(self):
        return ''.join(sorted(set(self.pyramid)))


def main():
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
    pyramid = Pyramid(data)
    compressed_pyramid = pyramid.compress()
    with open('output.txt', 'w') as file:
        file.write(compressed_pyramid)


if __name__ == "__main__":
    main()
