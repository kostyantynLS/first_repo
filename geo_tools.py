from ip2geotools.databases.noncommercial import DbIpCity

ip = '249.129.0.0'
response = DbIpCity.get(ip, api_key='free')
print(response)
#response.city, response.region, response.country('Mountain View', 'California', 'US')
#response.latitude, response.longitude(37.3893889, -122.0832101)
