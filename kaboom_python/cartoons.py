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

    def subscriptions(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/subscriptions/', params=kwargs)

    def subscribe(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/subscriptions/', method='POST', data=kwargs)

    def unsubscribe(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/subscriptions/', method='DELETE', data=kwargs)

    def rate(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/subscriptions/rate/', method='POST', data=kwargs)

class EpisodesClient(Base):
    def get_episodes(self, **kwargs):
        return self.request(endpoint='v1/cartoons/episodes/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/cartoons/episodes/', method='POST', data=kwargs)
    
    def detail(self, episode_id: int):
        return self.request(endpoint=f'v1/cartoons/episodes/{episode_id}/')
    
    def update(self, episode_id:int, **kwargs):
        return self.request(endpoint=f'v1/cartoons/episodes/{episode_id}/', method='PATCH', data=kwargs)

    def get_watched(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/episodes/', params=kwargs)

    def watch(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/episodes/', method='POST', data=kwargs)

    def unwatch(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/episodes/', method='DELETE', data=kwargs)

    def clean(self, **kwargs):
        return self.request(endpoint='v1/accounts/cartoons/episodes/clean/', method='DELETE', data=kwargs)

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

class GenresClient(Base):
    def get_genres(self, **kwargs):
        return self.request(endpoint='v1/cartoons/genres/', params=kwargs)
    
    def detail(self, genre_id: int):
        return self.request(endpoint=f'v1/cartoons/genres/{genre_id}/')