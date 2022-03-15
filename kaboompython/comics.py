from .base import Base

class ComicsClient(Base):
    def get_comics(self, **kwargs):
        return self.request(endpoint='v1/comics/series/', params=kwargs)

    def add(self, **kwargs):
        return self.request(endpoint='v1/comics/series/', method='POST', data=kwargs)
    
    def detail(self, comic_id: int):
        return self.request(endpoint=f'v1/comics/series/{comic_id}/')
    
    def update(self, comic_id: int, **kwargs):
        return self.request(endpoint=f'v1/comics/series/{comic_id}/', method='PATCH', data=kwargs)