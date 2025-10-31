# import tensorflow as tf
# from tf.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
# from tf.keras.preprocessing import image
# from tf.keras.appllications import mobilenet_v2

# import numpy as np
# from PIL import Image
# import io

# class ImageDetector:
#     def __init__(self):
#         # Load pre-trained MobileNetV2 model
#         self.model = MobileNetV2(weights='imagenet')
    
#     def predict(self, img_file):
#         """
#         Predict objects in the image
#         Args:
#             img_file: File object from request.FILES
#         Returns:
#             list of predictions with label, description, and confidence
#         """
#         try:
#             # Read image file
#             img = Image.open(img_file)
            
#             # Convert to RGB if needed
#             if img.mode != 'RGB':
#                 img = img.convert('RGB')
            
#             # Resize to 224x224 (MobileNetV2 input size)
#             img = img.resize((224, 224))
            
#             # Convert to array
#             img_array = image.img_to_array(img)
#             img_array = np.expand_dims(img_array, axis=0)
#             img_array = preprocess_input(img_array)
            
#             # Make prediction
#             predictions = self.model.predict(img_array)
#             decoded_predictions = decode_predictions(predictions, top=5)[0]
            
#             # Format results
#             results = []
#             for pred in decoded_predictions:
#                 results.append({
#                     'id': pred[0],
#                     'label': pred[1],
#                     'confidence': float(pred[2] * 100)
#                 })
            
#             return results
        
#         except Exception as e:
#             print(f"Error in prediction: {str(e)}")
#             return []

# # Global instance
# detector = ImageDetector()