from rest_framework import routers
from . import views

app_name = "pokeapi"

router = routers.SimpleRouter()
router.register(r'', views.PokemonViewSet, basename="pokemon")

urlpatterns = []

urlpatterns += router.urls
