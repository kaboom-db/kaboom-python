from .base import Base

class CartoonsClient(Base):
    def get_cartoons(self, **kwargs):
        return self.request(endpoint='v1/cartoons/series/', params=kwargs)

    def add_cartoons(self, **kwargs):
        return self.request(endpoint='v1/cartoons/series/', method='POST', data=kwargs)
    
    def detail(self, cartoon_id: int):
        return self.request(endpoint=f'v1/cartoons/series/{cartoon_id}/')
    
    def update(self, cartoon_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/series/{cartoon_id}/', method='PATCH', data=kwargs)