import twitter
import time
from time import ctime
import smtplib
from threading import Timer
import networkx as nx
import matplotlib.pyplot as plt
import pandas

#Connect with Twitter
CONSUMER_KEY = "YOUR KEY"
CONSUMER_SECRET = "YOUR SECRET"
ACCESS_TOKEN = "YOUR TOKEN"
ACCESS_TOKEN_SECRET = "YOUR SECRET"
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET,
                  tweet_mode='extended')

print("CONNECTED...")


def make_edgelist(user, nodelist, user2=None):
	edgelist = []
	i = 0
	while i < len(nodelist) - 1:
		edgelist.append((nodelist[i], user))
		if user2:
			edgelist.append((nodelist[i], user2))
		i += 1
	return edgelist


def map(user1_sn, user2_sn):

	u1_color = 'b'
	u2_color = 'g'
	common_color = 'y'

	user1 = api.GetUser(screen_name=user1_sn)
	user2 = api.GetUser(screen_name=user2_sn)
	u1_friends = api.GetFriends(screen_name=user1_sn)
	u2_friends = api.GetFriends(screen_name=user2_sn)
	u1_friend_names = [friend.screen_name for friend in u1_friends]
	u2_friend_names = [friend.screen_name for friend in u2_friends]
	user1_edgelist = make_edgelist(user1_sn, u1_friend_names)
	user2_edgelist = make_edgelist(user2_sn,u2_friend_names)

	# Create Graph
	g = nx.Graph()
	g.add_node(user1.screen_name)
	g.add_node(user2.screen_name)

	common_friends = []

	for friend in u1_friends:
		if friend.screen_name in u2_friend_names:
			common_friends.append(friend.screen_name)
		g.add_node(friend.screen_name)
		g.add_edge(user1.screen_name, friend.screen_name)

	for friend in u2_friends:
		g.add_node(friend.screen_name)
		g.add_edge(user2.screen_name, friend.screen_name)

	
	common_edges = make_edgelist(user1_sn, common_friends, user2=user2_sn)
	pos = nx.random_layout(g)
	# nx.draw_networkx_nodes(g, pos, nodelist=u1_friend_names, node_color='b')
	# nx.draw_networkx_nodes(g, pos, nodelist=u2_friend_names, node_color='g')
	nx.draw_networkx_nodes(g, pos, nodelist=common_friends, node_color='y')
	nx.draw_networkx_nodes(g, pos, nodelist=[user1.screen_name], node_color='r')
	nx.draw_networkx_nodes(g, pos, nodelist=[user2.screen_name], node_color='r')
	nx.draw_networkx_labels(g, pos, font_size=7)
	nx.draw_networkx_edges(g, pos, edgelist=common_edges, edge_color='b', width=.7, alpha=.4)
	#nx.draw_networkx_edges(g, pos, edgelist=user2_edgelist, edge_color='g', width=.7, alpha=.4)

	plt.title("Relational map of {} and {}".format(user1_sn, user2_sn))
	plt.show()

map('JMUCCM', 'BishopBurbidge')
