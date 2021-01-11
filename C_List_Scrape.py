from craigslist import CraigslistForSale
cl_h = CraigslistForSale(site ='orangecounty', category = 'free-stuff', filters={'posted_today': True, 'has_image': True, 'max_price': 0})

for result in cl_h.get_results(sort_by='newest', limit=30):
    print(result)
