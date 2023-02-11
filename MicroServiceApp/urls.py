from .views import Account_Viewset,Customer_Viewset,Cutomer_Account_Viewset
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()

routes.register('account', Account_Viewset, basename = 'account')
routes.register('customer', Customer_Viewset, basename = 'customer')
routes.register('details', Cutomer_Account_Viewset, basename = 'details')

urlpatterns = [
    
    
]

urlpatterns += routes.urls