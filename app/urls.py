from django.conf.urls import url
from app import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('bookapi', views.BookViewSet)
router.register('ratingapi',views.RatViewSet)
urlpatterns = router.urls
# urlpatterns += [
	
		# url(r'^book/', views.BookDetailsViewSet, name='book'),
		# url(r'^rating/', views.RatingViewSet, name='rating'),
		# ]