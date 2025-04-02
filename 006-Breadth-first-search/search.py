from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " продавец манго!")
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

def person_is_seller(seller):
    return seller[-1] == "m"

graph = {}
graph["вы"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

if __name__ == "__main__":
    search("вы")
