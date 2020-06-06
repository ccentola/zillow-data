
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
from settings import ZWSID

zillow_data = ZillowWrapper(ZWSID)

deep_search_response = zillow_data.get_deep_search_results('26122 N 121ST AVE,', '85383',True)

result = GetDeepSearchResults(deep_search_response)

print(result.bedrooms)
print(result.bathrooms)
print(result.home_size)
