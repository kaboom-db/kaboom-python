from .base import Base

class CartoonsClient(Base):
    def get_cartoons(self, **kwargs):
        return self.request(endpoint='v1/cartoons/series/', params=kwargs)

    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/series/', method='POST', data=kwargs)
    
    def detail(self, cartoon_id: int):
        return self.request(endpoint=f'v1/cartoons/series/{cartoon_id}/')
    
    def update(self, cartoon_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/series/{cartoon_id}/', method='PATCH', data=kwargs)

class EpisodesClient(Base):
    def get_episodes(self, **kwargs):
        return self.request(endpoint='v1/cartoons/episodes/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/episodes/', method='POST', data=kwargs)
    
    def detail(self, episode_id: int):
        return self.request(endpoint=f'v1/cartoons/episodes/{episode_id}/')
    
    def update(self, episode_id:int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/episodes/{episode_id}/', method='PATCH', data=kwargs)

class CharactersClient(Base):
    def get_characters(self, **kwargs):
        return self.request(endpoint='v1/cartoons/characters/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/characters/', method='POST', data=kwargs)
    
    def detail(self, character_id: int):
        return self.request(endpoint=f'v1/cartoons/characters/{character_id}/')
    
    def update(self, character_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/characters/{character_id}/', method='PATCH', data=kwargs)
