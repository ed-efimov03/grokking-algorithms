cache = {}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
        
def get_data_from_server(url):
    return f"Стартовая страница {url}" 

if __name__ == "__main__":
    print(get_page("google.com"))
    print(get_page("google.com"))
