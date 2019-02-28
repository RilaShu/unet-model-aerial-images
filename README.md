# unet-model for aerial images (or other images)
- **Abstract**<br>
U-NET model for RGB images, using aerial images as an example.
- **Codes**<br>
**1. unet_model**<br>
Code for UNET model, includes data enhancement(data.py), model(model.py), train(main.py) and prediction(prediction.py).<br>
**2. post_process(Optional)**<br>
Code for post process, includes smooth(smooth.py) and binary(binary.py), run main.py to use them.<br>
- **Data**<br>
Example data -- https://project.inria.fr/aerialimagelabeling/<br>
Also providing a short code (/data/segmentation256.py) to cut TIFF images to size 256*256.<br>
- **Result**<br>
Acc. -- 94% IOU -- 91
