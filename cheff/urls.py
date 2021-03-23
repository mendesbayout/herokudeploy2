from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Cheff API backend exam WORKALOVE",
      
      default_version='beta backend',
      description="Esta interface é a conexão entre você e dois dos melhores cheff's do mundo, um é especialista em FastFood, seu nome é Vinsmoke, o outro, é especialista em receitas demoradas, ele se chama Zeff, você comprou esse contato direto com eles por 5 milhões de dolares. Essa API fornece também a possibilidade de integração com Qualquer sistema de frontend.Caso tenha algum problema, acesse o dominio http://127.0.0.1:8000/admin/, as credenciais devem ser criadass",
      terms_of_service="https://github.com/mendesbayout",
      contact=openapi.Contact(email="mendesbayout@gmail.com"),
      license=openapi.License(name="Como o test é de backend voltado para Django Rest, acho que um Swagger funcional pode ser chamado de CRUD Interface"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
