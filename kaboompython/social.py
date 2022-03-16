from .base import Base

class ThoughtsClient(Base):
    def get_thoughts(self, **kwargs):
        return self.request(endpoint='v1/social/thoughts/', params=kwargs)
    
    def add(self, **kwargs):
        return self.request(endpoint='v1/social/thoughts/', method='POST', data=kwargs)
    
    def detail(self, thought_id: int):
        return self.request(endpoint=f'v1/social/thoughts/{thought_id}/')
    
    def update(self, thought_id: int, **kwargs):
        return self.request(endpoint=f'v1/social/thoughts/{thought_id}/', method='PATCH', data=kwargs)

    def get_comments(self, thought_id: int, **kwargs):
        return self.request(endpoint=f'v1/social/thoughts/{thought_id}/comments/', params=kwargs)
    
    def add_comment(self, thought_id: int, **kwargs):
        return self.request(endpoint=f'v1/social/thoughts/{thought_id}/comments/', method='POST', data=kwargs)
    
    def detail_comment(self, comment_id: int):
        return self.request(endpoint=f'v1/social/comments/{comment_id}/')
    
    def update_comment(self, comment_id: int, **kwargs):
        return self.request(endpoint=f'v1/social/comments/{comment_id}/', method='PATCH', data=kwargs)
