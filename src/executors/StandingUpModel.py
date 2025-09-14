import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.StandingUpModel.src.utils.response import build_response
from components.StandingUpModel.src.models.PackageModel import PackageModel
from components.StandingUpModel.src.utils.utils import load_models

class StandingUpModel(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        model = load_models()
        print("Model loaded successfully")  
        return {"model" : model}

    def recognition(self, image):
        """
        image: numpy array (cv2 image)
        Returns image with confidence written on it after inference
        """
        # Modeli bootstrap'tan al
        model = self.bootstrap_data.get("model", None)
        if model is None:
            raise ValueError("Model is not loaded in bootstrap data")
        prediction = model.predict(image)  

        label = prediction.get("label", "unknown")
        confidence = prediction.get("confidence", 0.0)

        text = f"{label}: {confidence:.2f}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2
        color = (0, 255, 0) 
        position = (20, 40)

        image = cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

        return image

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.recognition(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
