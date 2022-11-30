from mesa import Agent

class Car_Agent(Agent):
    """
    Car Agent: Use a* to find the shortest (and fastest) path to a given random destination.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.in_traffic = False

    def move(self):
        """ 
        Determines if the agent can move in the direction that was chosen
        """
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True, # Boolean for whether to use Moore neighborhood (including diagonals) or Von Neumann (only up/down/left/right).
            include_center=True) 
        
        # Checks which grid cells are empty
        freeSpaces = list(map(self.model.grid.is_cell_empty, possible_steps))

        next_moves = [p for p,f in zip(possible_steps, freeSpaces) if f == True]
       
        next_move = self.random.choice(next_moves)
        # Now move:
        if self.random.random() < 0.1:
            self.model.grid.move_agent(self, next_move)
            self.steps_taken+=1

    def step(self):
        """ 
        Determines the new direction it will take, and then moves
        """
        pass

class Traffic_Light_Agent(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid.
    """
    def __init__(self, unique_id, model, state = False, timeToChange = 10):
        super().__init__(unique_id, model)
        self.state = state
        self.timeToChange = timeToChange

    def step(self):
        # if self.model.schedule.steps % self.timeToChange == 0:
        #     self.state = not self.state
        pass

class Destination_Agent(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.arrivals = 0

    def step(self):
        pass

class Building_Agent(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        pass

class Road_Agent(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid.
    """
    def __init__(self, unique_id, model, direction="Left"):
        super().__init__(unique_id, model)
        self.direction = direction

    def step(self):
        pass

class Car_Spawner_Agent(Agent):
    """
    Car spawner agent. Spawns cars regularly in a given position.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.spawned = 0
    
    def step(self):
        # If this cell does not have a car, spawn one after n steps
        cell_content = self.model.grid.get_cell_list_contents([self.pos])
        for agent in cell_content:
            if isinstance(agent, Car_Agent):
                print("There is already a car in the spawner")
                return
