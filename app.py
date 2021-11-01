import streamlit as st
from model import LeNet

from PIL import Image

import torch
import torchvision.transforms as T

import json
# import io
# import joblib

# load class info
class_json_path = './class_indices.json'
json_file = open(class_json_path, 'rb')
class_indict = json.load(json_file)

def image_transform(image_byte):
    my_transform = T.Compose(
        [
            T.Resize((225, 225)),
            T.ToTensor(),
            T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ]
    )

    return my_transform(image_byte)

st.title("my app")
st.write('\n')

# create model
model = LeNet()
weights_path = './Lenet.pth'
model.load_state_dict(torch.load(weights_path))
model.eval()

image = Image.open('images/images.jpeg')
show = st.image(image, use_column_width = True)

st.sidebar.title("Upload Image")
uploaded_file = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg'] )

if uploaded_file is not None:
    u_img = Image.open(uploaded_file)  #Image.open(io.BytesIO(uploaded_file)) #
    show.image(u_img, use_column_width = True)


# For newline
st.sidebar.write('\n')
a_buttom = st.sidebar.button("Click Here to Classify")

if a_buttom:
    if uploaded_file is None:
        st.sidebar.write("please upload a flower picture")
    else:
        # image process for fitting in the algorithm
        tensor = image_transform(u_img).unsqueeze(0)
        outputs = torch.softmax(model.forward(tensor).squeeze(), dim=0)
        prediction = outputs.detach().cpu().numpy()

        index_pre = [(class_indict[str(index)], float(p)) for index, p in enumerate(prediction)]
        index_pre.sort(key=lambda x: x[1], reverse=True)
        # print(index_pre)
        #template = "class:{:<15} probability:{:.3f}"
        template = "{:<15} {:.3f}"
        texts = [template.format(k, v) for k, v in index_pre]
        for text in texts:
            st.sidebar.write(text)