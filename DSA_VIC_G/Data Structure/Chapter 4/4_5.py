class Escape:
    def __init__(self, width, height, map_data):
        self.width = width
        self.height = height
        self.grid = map_data.split(",")
        self.start = None

    
    def valid_map(self):
        #to ensure user didn't provide broken map: input maps w*h and provided map
        if len(self.grid) != self.height:
            return False
        found_F = False

        #to locate his F location
        for y in range(self.height):
            #check y-axis if it has same w or not
            if len(self.grid[y]) != self.width:
                return False
            
            for x in range(self.width):
                if self.grid[y][x] == 'F':
                    self.start = (x, y) #save F location
                    found_F = True
        return found_F

    def solve(self):
        if not self.valid_map():
            print("Invalid map input.")
            return
        
        queue = [self.start]
        visited = set() #location already visited
        visited.add(self.start)
        #Modifiers for North, East, South, West
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] 

        while len(queue) > 0:
            print(f"Queue: {queue}")
            current_x, current_y = queue.pop(0)

            #checking adjacent directions
            for dx, dy in directions:
                nx, ny = current_x + dx, current_y + dy
                #check next location is within boundaries
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) not in visited:
                        cell = self.grid[ny][nx]
                        if cell == 'O':
                            print("Found the exit portal.")
                            return
                        elif cell =='_':
                            visited.add((nx, ny))
                            queue.append((nx, ny))
        print("Cannot reach the exit portal.")
        
User_input = input("Enter width, height, and room: ")

try:
    parts = User_input.split(' ')
    w = int(parts[0])
    h = int(parts[1])
    map_info = parts[2]
    game = Escape(w, h, map_info)
    game.solve()

except(IndexError, ValueError):
    print("Invalid map input.")