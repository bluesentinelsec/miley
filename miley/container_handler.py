import json
import logging
import os
import tarfile
import docker

logging.basicConfig(level=logging.INFO)

class Container:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.image_name = ""
        self.downloaded_image = ""
        self.export_path = "/tmp/image.tar"
        self.extracted_path = "/tmp/unpacked_image/"
        # https://docker-py.readthedocs.io/en/stable/api.html

    def get(self, img):
        logging.info(f"getting container image: {img}")
        self.image_name = img

        try:
            self.downloaded_image = self.docker_client.images.pull(self.image_name)
            with open(self.export_path, "wb") as f:
                for chunk in self.downloaded_image.save():
                    f.write(chunk)
                f.close()
        except Exception as e:
            logging.error(e)
            return

    def unpack_container_archive(self):
        image = tarfile.open(self.export_path)
        manifest = json.loads(image.extractfile('manifest.json').read())
        for layer in manifest[0]['Layers']:
            logging.info('Found layer: %s' % layer)
            layer_tar = tarfile.open(fileobj=image.extractfile(layer))

            for tarinfo in layer_tar:
                if tarinfo.isdev():
                    continue

                dest = os.path.join(self.extracted_path, tarinfo.name)
                if not tarinfo.isdir() and os.path.exists(dest):
                    os.unlink(dest)

                layer_tar.extract(tarinfo, path=self.extracted_path)
