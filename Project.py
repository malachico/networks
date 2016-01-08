from imdb import IMDb
import networkx as nx
import matplotlib.pyplot as plt

ia = IMDb()
top_100_actors = [
	'Leonardo DiCaprio',
	'Harrison Ford',
	'Johnny Depp',
	'Tom Cruise',
	'Brad Pitt',
	'Christian Bale',
	'Samuel L. Jackson',
	'Matt Damon',
	'Tom Hanks',
	'Will Smith',
	'Robert De Niro',
	'Benicio Del Toro',
	'Christoph Waltz',
	'Denzel Washington',
	'Ralph Fiennes',
	'Liam Neeson',
	'Matthew McConaughey',
	'Robert Downey Jr.',
	'Hugh Jackman',
	'Alec Guinness',
	'Clint Eastwood',
	'Jim Carrey',
	'Mel Gibson',
	'Heath Ledger',
	'Jack Nicholson',
	'Robert Redford',
	'Russell Crowe',
	'Al Pacino',
	'Javier Bardem',
	'Robin Williams',
	'Anthony Hopkins',
	'George Clooney',
	'Colin Firth',
	'Sean Connery',
	'Marlon Brando',
	'Daniel Day-Lewis',
	'Christopher Plummer',
	'Morgan Freeman',
	'Ian McKellen',
	'Kevin Costner',
	'Gary Oldman',
	'Joaquin Phoenix',
	'Bill Murray',
	'Edward Norton',
	'Kevin Spacey',
	'Ben Kingsley',
	'Jon Voight',
	'Joe Pesci',
	'James Stewart',
	'Philip Seymour Hoffman',
	'Michael Caine',
	'Michael Douglas',
	'Geoffrey Rush',
	'Sean Penn',
	'Jeff Bridges',
	'Paul Newman',
	'Christopher Walken',
	'Cary Grant',
	'Dustin Hoffman',
	'John Wayne',
	'Jeremy Irons',
	'Tommy Lee Jones',
	'Kirk Douglas',
	'Robert Duvall',
	'Tim Robbins',
	'Steve McQueen',
	'Jamie Foxx',
	'James Dean',
	'Forest Whitaker',
	'Ed Harris',
	'Gene Hackman',
	'Kevin Kline',
	'Charles Chaplin',
	'John Malkovich',
	'Gene Kelly',
	'Martin Sheen',
	"Peter O'Toole",
	'Charlton Heston',
	'Gregory Peck',
	'Don Cheadle',
	'Jack Lemmon',
	'F. Murray Abraham',
	'Laurence Olivier',
	'Orson Welles',
	'Humphrey Bogart',
	'Alan Arkin',
	'Clark Gable',
	'William Holden',
	'Robert Mitchum',
	'Peter Sellers',
	'Richard Burton',
	'Sidney Poitier',
	'Henry Fonda',
	'George C. Scott',
	'Burt Lancaster',
	'Gary Cooper',
	'Jason Robards',
	'Spencer Tracy',
	'James Cagney',
	'Peter Finch',
]
print len(top_100_actors)


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