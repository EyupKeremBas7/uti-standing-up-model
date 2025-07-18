from sdks.novavision.src.helper.package import PackageHelper
from components.StandingUpModel.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, Recognition, RecognitionConfigs, RecognitionInputs, RecognitionOutputs, RecognitionRequest, RecognitionResponse, OutputDetections


def build_response(context):
    outputDetections = OutputDetections(value=context.image)
    outputs = RecognitionOutputs(outputDetections=outputDetections)
    packageResponse = RecognitionResponse(outputs=outputs)
    packageExecutor = Recognition(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel