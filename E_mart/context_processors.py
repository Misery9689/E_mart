<<<<<<< HEAD
# Create this file in your E_mart folder (same level as views.py that has your wishlist code)

from app.models import Wishlist  # Import from app.models since your models are in the app folder

def wishlist_context(request):
    """Add wishlist count to all templates"""
    wishlist_count = 0
    
    if request.user.is_authenticated:
        try:
            wishlist_count = Wishlist.objects.filter(user=request.user).count()
        except:
            wishlist_count = 0
    
    return {
        'wishlist_count': wishlist_count
=======
# Create this file in your E_mart folder (same level as views.py that has your wishlist code)

from app.models import Wishlist  # Import from app.models since your models are in the app folder

def wishlist_context(request):
    """Add wishlist count to all templates"""
    wishlist_count = 0
    
    if request.user.is_authenticated:
        try:
            wishlist_count = Wishlist.objects.filter(user=request.user).count()
        except:
            wishlist_count = 0
    
    return {
        'wishlist_count': wishlist_count
>>>>>>> 40351b8156c73bab5e97d8849973739a2a33751e
    }