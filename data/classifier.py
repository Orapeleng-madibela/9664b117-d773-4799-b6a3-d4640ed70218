import ast

from PIL import Image

import torchvision.transforms as transforms
import torchvision.models as models

from torch import __version__
from torch.autograd import Variable


# Load pretrained CNN models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models_dic = {
    'resnet': resnet18,
    'alexnet': alexnet,
    'vgg': vgg16
}


# Load ImageNet class labels
with open('imagenet1000_clsid_to_human.txt', 'r') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(
        imagenet_classes_file.read()
    )


def classifier(img_path, model_name):
    """
    Classifies an image using a pretrained CNN model.

    Parameters:
        img_path (str): Path to image.
        model_name (str): Model architecture.

    Returns:
        str: Predicted ImageNet class label.
    """

    # Load image
    img_pil = Image.open(img_path)

    # Define preprocessing
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # Preprocess image
    img_tensor = preprocess(img_pil)

    # Add batch dimension
    img_tensor.unsqueeze_(0)

    # Determine PyTorch version
    pytorch_ver = __version__.split('.')

    # PyTorch 0.4 and newer
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:

        img_tensor.requires_grad_(False)

        data = img_tensor

    # PyTorch versions older than 0.4
    else:

        data = Variable(
            img_tensor,
            volatile=True
        )

    # Get requested model
    if model_name not in models_dic:
        raise ValueError(
            "Invalid model architecture. "
            "Choose from: resnet, alexnet, vgg."
        )

    model = models_dic[model_name]

    # Set model to evaluation mode
    model = model.eval()

    # Classify image
    output = model(data)

    # Get predicted class index
    pred_idx = output.data.numpy().argmax()

    # Return predicted class label
    return imagenet_classes_dict[pred_idx]
