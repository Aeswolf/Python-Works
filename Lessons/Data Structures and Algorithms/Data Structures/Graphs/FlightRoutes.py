"""
Implementing a graph for flight routes
"""


# A class for the flight graph
class FlightGraph:
    # The init method for creating an instance of the class
    def __init__(self, routes, is_directed):
        self.flight_routes = routes
        self.is_directed = is_directed

    # Creating flight_dictionary to provide an adjacency list representation for the flights available
    def flight_dictionary(self):
        # creating a dictionary to hold routes
        adjacency_dictionary = {take_off_location[0]: [] for take_off_location in self.flight_routes}

        # Assigning each take_off_locations to the respective final destinations using a for loop
        for edge in self.flight_routes:
            # Creating two final destination variables for the final destination each take_off_location
            final_destination_one, final_destination_two = edge[0], edge[1]
            if final_destination_two not in adjacency_dictionary[final_destination_one]:
                adjacency_dictionary[final_destination_one].append(final_destination_two)
            # Handling a scenario if the graph created is a directed or undirected graph
            if not self.is_directed:
                adjacency_dictionary[final_destination_two].append(final_destination_one)
        return adjacency_dictionary


route = [("Accra", "Takoradi"), ("Accra", "Kumasi"), ("Kumasi", "Takoradi"), ("Accra", "New York"), ("Accra", "Paris"),
         ("Paris", "Accra"), ("New York", "Accra"), ("Paris", "New York"), ("Takoradi", "Accra"),
         ("Takoradi", "Kumasi")]
flights = FlightGraph(route, False)
print(flights.flight_dictionary())
