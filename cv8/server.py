from xmlrpc.server import SimpleXMLRPCServer

class ImageProcessing:
    def __init__(self, size=None, data=None):
        self.size = size
        self.data = data

    def upload_image(self, img):
        self.size = img["size"]
        self.data = img["data"]
        return True

    def download_image(self):
        my_result = {"size": self.size, "data": self.data}
        return my_result

    def invert_image(self):
        if self.data is None:
            raise Exception('Image not uploaded')
        else:
            counter = 0
            for p in self.data:
                self.data[counter] = 255 - p
                counter += 1
            return True

    def edge_detect(self):
        if self.data is None:
            raise Exception('Image not uploaded')
        my_result = []
        width = self.size[0]

        for p, item in enumerate(self.data):
            if p - 1 < 0 or p - width < 0 or p % width == 0:
                e = 0
            else:
                fx = self.data[p] - self.data[p - 1]
                fy = self.data[p] - self.data[p - width]
                e = max(abs(fx), abs(fy))
            my_result.append(e)

        self.data = my_result
        return True




def main():
    server_address = ('localhost', 10001)
    server = SimpleXMLRPCServer(server_address)
    server.register_instance(ImageProcessing())
    server.register_introspection_functions()
    print("Starting Image Processing server, use <Ctrl-C> to stop")
    server.serve_forever()
    
if __name__ == "__main__":
    main()
