import logging

import docker

class Container:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.image_name = ""
        self.downloaded_image = ""

    def get(self, img):
        logging.info(f"getting container image: {img}")
        self.image_name = img

        try:
            self.downloaded_image = self.docker_client.images.pull(self.image_name)
            with open("/tmp/image.tar", "wb") as f:
                for chunk in self.downloaded_image.save():
                    f.write(chunk)
                f.close()
        except Exception as e:
            logging.error(e)

        # https://docker-py.readthedocs.io/en/stable/api.html
        self.docker_client.api.get_archive()
