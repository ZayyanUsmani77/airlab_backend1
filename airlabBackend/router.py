from airlab.viewsets import SignupViewset
from airlab.viewsetslogin import LoginViewset
from airlab.viewsetslab import LabViewset
from airlab.viewsetsservice import ServiceViewset
from airlab.viewsetsbooklab import BookLabViewset
from airlab.viewsetscontactlab import ContactLabViewset
from airlab.viewsetsreview import ReviewViewset
from airlab.viewsetslabimage import LabImageViewset


from rest_framework import routers
router = routers.DefaultRouter()
router.register('signup', SignupViewset)
router.register('login', LoginViewset)
router.register('lab' , LabViewset )
router.register('service' , ServiceViewset)
router.register('booklab' , BookLabViewset)
router.register('contactlab' , ContactLabViewset)
router.register('review' , ReviewViewset)
router.register('labimage' , LabImageViewset)
# localhost:p/api/signup
# localhost:p/api
# GET, POST, PUT, DELETE
#List , retrive