from django.urls import path
from .views import FormulaPage, FormulaDetail, CalculateAPI, FunksionalHolatPage

app_name = "formula"
urlpatterns = [
    path('', FormulaPage.as_view(), name='formula'),
    path('funksional-holatni-aniqlash', FunksionalHolatPage.as_view(), name='funksional-holat'),
    path('<int:pk>/', FormulaDetail.as_view(), name='detail'),
    path('api/<int:id>/', CalculateAPI.as_view(), name='calculate-api'),
    
    
]