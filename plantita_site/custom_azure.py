from storages.backends.azure_storage import AzureStorage

class PublicAzureStorage(AzureStorage):
    location = 'uploads'
    file_overwrite = False