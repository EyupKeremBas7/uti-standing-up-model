from pydantic import validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Detection, Package, Inputs, Configs, Outputs, Response, Request, Output, Input, Config,Image


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"

class Detection(Detection):
    imgUID: str

class OutputDetections(Output):
    name: Literal["outputDetections"] = "outputDetections"
    value: List[Detection]
    type: Literal["list"] = "list"

    class Config:
        title = "Detections"



class RecognitionInputs(Inputs):
    inputImage: InputImage

class RecognitionOutputs(Outputs):
    outputDetections: OutputDetections


class RecognitionRequest(Request):
    inputs: Optional[RecognitionInputs]
    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class RecognitionResponse(Response):
    outputs: RecognitionOutputs


class Recognition(Config):
    name: Literal["Recognition"] = "Recognition"
    value: Union[RecognitionRequest, RecognitionResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Recognition"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[Recognition]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["StandingUpModel"] = "StandingUpModel"
