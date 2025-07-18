from sdks.novavision.src.helper.package import PackageHelper
from components.StandingUpModel.src.models.PackageModel import (PackageModel, PackageConfigs, ConfigExecutor, StandingUpModel,StandingUpModelResponse, StandingUpModelOutputs, OutputDetections)

def build_response(context):
    outputDetections = OutputDetections(value=context.image)
    outputs = StandingUpModelOutputs(outputDetections=outputDetections)
    packageResponse = StandingUpModelResponse(outputs=outputs)
    packageExecutor = StandingUpModel(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel