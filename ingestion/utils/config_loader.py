import yaml

class ConfigLoader:
    
    @staticmethod
    def load_config(file_path:str) -> dict:
        '''
        Load configuration from a YAML file
        '''
        
        try:
            with open(file_path, 'r') as file:
                config = yaml.safe_load(file)
            return config
        except FileNotFoundError:
            print(f"Configuration file not found: {file_path}") 
            raise

        except Exception as error:
            print(f"Error loading configuration: {error}")
            raise


