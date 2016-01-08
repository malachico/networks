from imdb import IMDb
import networkx as nx
import matplotlib.pyplot as plt

ia = IMDb()
top_100_actors = [
	'Jack Nicholson',
	'Marlon Brando',
	'Robert De Niro',
	'Al Pacino',
	'Daniel Day-Lewis',
	'Dustin Hoffman',
	'Tom Hanks',
	'Anthony Hopkins',
	'Paul Newman',
	'Denzel Washington',
	'Jeff Bridges',
	'James Stewart',
	'Laurence Olivier',
	'Michael Caine',
	'Morgan Freeman',
	'Clint Eastwood',
	'Sean Penn',
	'Robert Duvall',
	'Robin Williams',
	'Russell Crowe',
	'Philip Seymour Hoffman',
	'Robin Williams',
	'Johnny Depp',
	'Leonardo DiCaprio',
	'Ben Kingsley',
	'Tommy Lee Jones',
	'Sidney Poitier',
	'Gene Hackman',
	"Peter O'Toole",
	'Alec Guinness',
	'Kevin Spacey',
	'Spencer Tracy',
	'Gregory Peck',
	'Humphrey Bogart',
	'Clark Gable',
	'Jack Lemmon',
	'George C. Scott',
	'Gary Cooper',
	'Jason Robards',
	'James Dean',
	'Peter Sellers',
	'Charles Chaplin',
	'Peter Finch',
	'James Cagney',
	'Henry Fonda',
	'Burt Lancaster',
	'Kirk Douglas',
	'Cary Grant',
	'Geoffrey Rush',
	'Richard Burton',
	'Christopher Plummer',
	'William Holden',
	'John Wayne',
	'Alan Arkin',
	'Sean Connery',
	'Christopher Walken',
	'Joe Pesci',
	'Heath Ledger',
	'Javier Bardem',
	'Christoph Waltz',
	'Ralph Fiennes',
	'Jamie Foxx',
	'Joaquin Phoenix',
	'Colin Firth',
	'Matthew McConaughey',
	'Hugh Jackman',
	'Benicio Del Toro',
	'Gary Oldman',
	'Edward Norton',
	'Christian Bale',
	'John Malkovich',
	'Ian McKellen',
	'F. Murray Abraham',
	'Jon Voight',
	'Liam Neeson',
	'Michael Douglas',
	'Harrison Ford',
	'Forest Whitaker',
	'Kevin Kline',
	'Jeremy Irons',
	'Brad Pitt',
	'Robert Downey Jr.',
	'George Clooney',
	'Matt Damon',
	'Samuel L. Jackson',
	'Mel Gibson',
	'Don Cheadle',
	'Ed Harris',
	'Tim Robbins',
	'Robert Redford',
	'Orson Welles',
	'Steve McQueen',
	'Charlton Heston',
	'Gene Kelly',
	'Robert Mitchum',
	'Bill Murray',
	'Jim Carrey',
	'Tom Cruise',
	'Will Smith',
	'Martin Sheen',
	'Kevin Costner'
]


# ## Generate edges ###
# Each edge is in the format : (movie : actor)
edges = []

for actor in top_100_actors:
	print actor
	actor = ia.search_person(actor)[0]
	full_person = ia.get_person(actor.getID(), info=["filmography"])
	for movie in full_person["actor"]:
		edges.append((movie['title'], actor['name']))

# ## Generate graph that represents which actor played in which movie ###
G = nx.Graph()

# add edges and nodes
G.add_edges_from(edges)

nx.write_gml(G, "actor_to_movie_all_movies.gml")

nodes_to_remove = []
for node in G.nodes():
	if G.degree(node) == 1:
		nodes_to_remove.append(node)

G.remove_nodes_from(nodes_to_remove)

nx.write_gml(G, "actor_to_movie_common_movies.gml")

for node in G.nodes():
	for node2 in G.nodes():
		if len(list(nx.common_neighbors(G, node, node2))) > 0:
			G.add_edge(node, node2)

movies = []
for node in G.nodes():
	if node not in top_100_actors:
		movies.append(node)

G.remove_nodes_from(movies)

nx.draw(G, with_labels=True)
plt.show()
nx.write_gml(G, "actor_to_actor.gml")