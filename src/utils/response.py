from sdks.novavision.src.helper.package import PackageHelper
from components.StandingUpModel.src.models.PackageModel import (PackageModel, PackageConfigs, ConfigExecutor, StandingUpModelExecutor,StandingUpModelExecutorResponse, StandingUpModelExecutorOutputs, OutputDetections)

def build_response(context):
    outputDetections = OutputDetections(value=context.image)
    outputs = StandingUpModelExecutorOutputs(outputDetections=outputDetections)
    packageResponse = StandingUpModelExecutorResponse(outputs=outputs)
    packageExecutor = StandingUpModelExecutor(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
