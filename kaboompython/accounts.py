from .base import Base

class UsersClient(Base):
    def get_users(self, **kwargs):
        return self.request(endpoint='v1/accounts/users/', params=kwargs)
    
    def detail(self, username: str):
        return self.request(endpoint=f'v1/accounts/users/{username}/')
    
    def update(self, username: str, **kwargs):
        return self.request(endpoint=f'v1/accounts/users/{username}/', method='PATCH', data=kwargs)
    
    def report(self, **kwargs):
        return self.request(endpoint=f'v1/accounts/report/', method='POST', data=kwargs)

class ImageClient(Base):
    def upload(self, file, **kwargs):
        return self.request(endpoint='v1/accounts/upload/', method='POST', data=kwargs, file=file)