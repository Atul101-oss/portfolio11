
from django.contrib import admin
from .models import DetectionHistory

@admin.register(DetectionHistory)
class DetectionHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'get_top_prediction')
    list_filter = ('uploaded_at',)
    readonly_fields = ('image', 'predictions', 'uploaded_at')
    
    def get_top_prediction(self, obj):
        if obj.predictions and len(obj.predictions) > 0:
            top = obj.predictions[0]
            return f"{top['label']} ({top['confidence']:.2f}%)"
        return "No predictions"
    get_top_prediction.short_description = 'Top Prediction'