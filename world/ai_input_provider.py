
class AiInputProvider:
    def __init__(self, params):
        self.params = params

    def calculate_ai_input(self, env_values):

        # Values from environment
        T1, T2, T3, T4, Tsource = env_values[0], env_values[1], env_values[2], env_values[3], env_values[4]
        
        # Normalize input data
        T1_norm = (T1-15)/25
        orientation_norm = (T1-self.params.goalT1)/12.5
        Tsource_norm = (Tsource - 15)/25
        
        return [T1_norm, orientation_norm, Tsource_norm]
