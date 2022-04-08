from storages.backends.azure_storage import AzureStorage

class PublicAzureStorage(AzureStorage):
    account_name = 'plantitastorage'
    # account_key = 'gcQuJCurRiiVlJcbIIinxVXVAPYXX15WVZbh8JaSG/sPMRDfL+w4S1X8NJBluG6eRkpwf9uQv0BWU857xbrESQ=='
    azure_container = 'media'
    expiration_secs = None
    location = 'media'
    file_overwrite = False