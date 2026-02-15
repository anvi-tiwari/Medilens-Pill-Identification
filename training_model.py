
 from ultralytics import YOLO
model = YOLO('yolov8n-cls.pt') 
model.train(
    data='/content/medilens_split', 
    epochs=50, 
    imgsz=224,
    degrees=15.0,   # Rotation
    flipud=0.5,     # Up down 
    fliplr=0.5,     # Left right  
    hsv_v=0.4,      
    hsv_s=0.3        




 

