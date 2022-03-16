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

class IssuesClient(Base):
    def get_issues(self, **kwargs):
        return self.request(endpoint='v1/comics/issues/', params=kwargs)

    def add(self, **kwargs):
        return self.request(endpoint='v1/comics/issues/', method='POST', data=kwargs)
    
    def detail(self, issue_id: int):
        return self.request(endpoint=f'v1/comics/issues/{issue_id}/')
    
    def update(self, issue_id: int, **kwargs):
        return self.request(endpoint=f'v1/comics/issues/{issue_id}/', method='PATCH', data=kwargs)

class PublishersClient(Base):
    def get_publishers(self, **kwargs):
        return self.request(endpoint='v1/comics/publishers/', params=kwargs)

    def add(self, **kwargs):
        return self.request(endpoint='v1/comics/publishers/', method='POST', data=kwargs)
    
    def detail(self, publisher_id: int):
        return self.request(endpoint=f'v1/comics/publishers/{publisher_id}/')
    
    def update(self, publisher_id: int, **kwargs):
        return self.request(endpoint=f'v1/comics/publishers/{publisher_id}/', method='PATCH', data=kwargs)

class StaffClient(Base):
    def get_staff(self, **kwargs):
        return self.request(endpoint='v1/comics/staff/', params=kwargs)

    def add(self, **kwargs):
        return self.request(endpoint='v1/comics/staff/', method='POST', data=kwargs)
    
    def detail(self, staff_id: int):
        return self.request(endpoint=f'v1/comics/staff/{staff_id}/')
    
    def update(self, staff_id: int, **kwargs):
        return self.request(endpoint=f'v1/comics/staff/{staff_id}/', method='PATCH', data=kwargs)
