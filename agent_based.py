import random as r


class Agent():
    def __init__(self, id, reality_size):
        self.id = id
        self.connections = []
        self.knowledge_state = binary_string(reality_size)

    def say_connections(self):
        print(self.id, self.connections)

    def say_knowledge(self):
        print(self.id, self.knowledge_state)


def binary_string(length):
    end_range = 2**length - 1
    string_root = '{0:0' + str(length) + 'b}'
    return string_root.format(r.randint(0, end_range))


def binary_string_score(string1, string2):
    result_string = ''
    for index, value in enumerate(string1):
        if value == string2[index]:
            result_string += '1'
        else:
            result_string += '0'
    return result_string, result_string.count('1')


def main(reality_size=5):
    reality = binary_string(reality_size)
    agents = {i: Agent(i, reality_size) for i in range(6)}
    for agent in agents:
        print(binary_string_score(reality, agents[agent].knowledge_state))


if __name__ == '__main__':
    main()