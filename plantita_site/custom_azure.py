from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    location = 'uploads'
    file_overwrite = False