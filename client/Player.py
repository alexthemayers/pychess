class Player(): 
    
    def __init__(self, side: str, name: str): 
        if side == "white" or "black":
            self.side = side
        else:
            print("invalid side selected")
            exit(1)
        
    