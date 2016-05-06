# I want to define a bunch of agents
# They could be objects or functions?
# They all need to have attributes that describe their connections
import random as r


class Agent():
	def __init__(self, id):
		self.id = id
		self.connections = []
		self.knowledge_state = '{0:05b}'.format(r.randint(0, 31))

	def say_connections(self):
		print(self.id, self.connections)

	def say_knowledge(self):
		print(self.id, self.knowledge_state)


def main():
	agents = {i: Agent(i) for i in range(6)}
	for agent in agents:
		agents[agent].say_knowledge()


if __name__ == '__main__':
	main()