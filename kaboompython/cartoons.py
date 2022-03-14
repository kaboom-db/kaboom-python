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

class NetworksClient(Base):
    def get_networks(self, **kwargs):
        return self.request(endpoint='v1/cartoons/networks/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/networks/', method='POST', data=kwargs)
    
    def detail(self, network_id: int):
        return self.request(endpoint=f'v1/cartoons/networks/{network_id}/')
    
    def update(self, network_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/networks/{network_id}/', method='PATCH', data=kwargs)

class ActorsClient(Base):
    def get_voiceactors(self, **kwargs):
        return self.request(endpoint='v1/cartoons/actors/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/actors/', method='POST', data=kwargs)
    
    def detail(self, actor_id: int):
        return self.request(endpoint=f'v1/cartoons/actors/{actor_id}/')
    
    def update(self, actor_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/actors/{actor_id}/', method='PATCH', data=kwargs)

class TeamsClient(Base):
    def get_teams(self, **kwargs):
        return self.request(endpoint='v1/cartoons/teams/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/teams/', method='POST', data=kwargs)
    
    def detail(self, team_id: int):
        return self.request(endpoint=f'v1/cartoons/teams/{team_id}/')
    
    def update(self, team_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/teams/{team_id}/', method='PATCH', data=kwargs)

class LocationsClient(Base):
    def get_locations(self, **kwargs):
        return self.request(endpoint='v1/cartoons/locations/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/locations/', method='POST', data=kwargs)
    
    def detail(self, location_id: int):
        return self.request(endpoint=f'v1/cartoons/locations/{location_id}/')
    
    def update(self, location_id: int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/locations/{location_id}/', method='PATCH', data=kwargs)
