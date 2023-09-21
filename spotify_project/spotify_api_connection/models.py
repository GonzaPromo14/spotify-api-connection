from django.db import models

# Create your models here.
class Authenticate(models.Model):
    access_token = models.CharField(max_length=100)
    is_expired = models.BooleanField(default=False)

    def set_access_token(self, access_token: str) -> None:
        self.access_token = access_token

    def get_access_token(self) -> str:
        return self.access_token
    
    def set_is_expired(self, is_expired: bool) -> None:
        self.is_expired = is_expired

    def get_is_expired(self) -> bool:
        return self.is_expired
    
