from pydantic import validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config, Detection

class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image],Image]
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

class CustomDetection(Detection):
    imgUID: str

class OutputDetections(Output):
    name: Literal["outputDetections"] = "outputDetections"
    value: List[CustomDetection]
    type: Literal["list"] = "list"

    class Config:
        title = "Detections"

class StandingUpModelExecutorInputs(Inputs):
    inputImage: InputImage

class StandingUpModelExecutorConfigs(Configs):
    pass

class StandingUpModelExecutorRequest(Request):
    inputs: Optional[StandingUpModelExecutorInputs]
    configs: Optional[StandingUpModelExecutorConfigs]

    class Config:
        json_schema_extra = {
            "target": "configs"
        }

class StandingUpModelExecutorOutputs(Outputs):
    outputDetections: OutputDetections

class StandingUpModelExecutorResponse(Response):
    outputs: StandingUpModelExecutorOutputs

class StandingUpModelExecutor(Config):
    name: Literal["StandingUpModelExecutor"] = "StandingUpModelExecutor"
    value: Union[StandingUpModelExecutorRequest, StandingUpModelExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Standing Up Model"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: StandingUpModelExecutor
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
