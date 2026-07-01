from abc import ABC, abstractmethod

#ABC : Abstract Base Class
class BaseIngestor(ABC):
    @abstractmethod
    def fetch_products(self,search_term:str):
        '''
        Fetch products from the source based on the search term
        '''
        pass

    @abstractmethod
    def save_raw(self, data:dict):
        '''
        Save raw source data
        '''
        pass
    
    @abstractmethod
    def validate_response(self, data:dict):
        '''
        Validate the response from the source
        '''
        pass
