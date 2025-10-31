from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DetectionHistory
# from .ml_model import detector
import json

def detect_view(request):
    """Main detection page"""
    recent_detections = DetectionHistory.objects.all()[:5]
    return render(request, 'image_detection/detect.html', {
        'recent_detections': recent_detections
    })

@csrf_exempt
def detect_api(request):
    """API endpoint for image detection"""
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            image_file = request.FILES['image']
            
            # Run detection
            # predictions = detector.predict(image_file)
            predictions = [{'id': 'n02123045', 'label': 'tabby', 'confidence': 85.0}]  # Placeholder
            
            # Save to database
            image_file.seek(0)  # Reset file pointer
            detection = DetectionHistory.objects.create(
                image=image_file,
                predictions=predictions
            )
            
            return JsonResponse({
                'success': True,
                'predictions': predictions,
                'image_url': detection.image.url
            })
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    return JsonResponse({
        'success': False,
        'error': 'No image provided'
    }, status=400)

def detection_history(request):
    """View detection history"""
    detections = DetectionHistory.objects.all()
    return render(request, 'image_detection/history.html', {
        'detections': detections
    })