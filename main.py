# Based on the original for udemy course https://www.udemy.com/artificial-intelligence-az/
# Self Driving Car

# Import libraries
import argparse
import os
import time

# Importing Python files
from infra.save_orchestrator import SaveOrchestrator
from infra.score_history import ScoreHistory
from world.ai import SelfDrivingCarAI
from world.ai_input_provider import AiInputProvider
from world.game_updater import GameUpdater
from world.reward_calculator import RewardCalculator
from world.env import environment

TF, KERAS, TF_DOUBLE = ("tf", "keras", "tf_double")

parser = argparse.ArgumentParser(description='Run Pump AI.')
parser.add_argument('-im', help='(im = implement) - Select implementation to run', choices=[TF, KERAS, TF_DOUBLE])
parser.add_argument('-sb', help='(sb = Start Brain) - Name of brain to start with, from saves/brains')
parser.add_argument('-eb', help='(eb = End Brain) - Name of brain to write to after the iterations are done, from saves/brains')
parser.add_argument('-en', type=int, help='(en = eligibility trace steps n) - How many steps should eligiblity trace take (1 is default, is simple one step Q learning)')

args = parser.parse_args()

if args.im == TF:
    from ai.tf.ai_self_tf import Dqn
elif args.im == TF_DOUBLE:
    from ai.tf.ai_self_tf_dualq import Dqn
elif args.im == KERAS:
    from ai.ai_self_keras import Dqn

# Adding this line if we don't want the right click to put a red point
SAVES = "./saves"
SAVES_BRAINS = "%s/brains" % SAVES

def ensure_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

ensure_dir(SAVES)
ensure_dir(SAVES_BRAINS)


n_steps = args.en if args.en else 1

# Gathering all the parameters (that we can modify to explore)
class Params():
    def __init__(self):
		# Parameter of algorithm
        self.lr = 0.001
        self.gamma = 0.9
        self.ER_batch_size = 100
        self.ER_capacity = 100000
        self.input_size = 2
        self.action_size = 3
        self.goalT1 = 27
        self.goalT2 = 0
        self.goalT3 = 0
        self.goalT4 = 0


# Running the whole thing

# Creating Connection for sender and receiver socket
env = environment()
env.createServerSockets()

# Parameters
params = Params()

# Creating score history
score_history = ScoreHistory()

# Creating calculaters
reward_calculator = RewardCalculator(params)
ai_input_provider = AiInputProvider(params)

# Creating brain
ai = SelfDrivingCarAI(params, Dqn)

# Create brain module in folder
save_orchestrator = SaveOrchestrator("saves/", ai.brain)


training = GameUpdater(reward_calculator, ai_input_provider, ai, score_history, env, n_steps)

if args.sb:
    save_orchestrator.load_brain(os.path.join(SAVES_BRAINS, args.sb))

iter = 0

while True:
    print('------------------------------------------------')
    print('iteration ', iter)
    t0 = time.time()
    
    # Sleep in order to make sure Simulink and Python can have a good TCP/IP communication
    time.sleep(0.1)
	
    # Have to send the first communication to Simulink in order to start the simulation
    env.sendAction(0)
    
    # Update brain
    training.update()
    
	# Save brain file and plot
    if iter % 500 == 0:
        save_orchestrator.save_brain(os.path.join(SAVES_BRAINS, args.eb))
        score_history.save_brainplot()
    
    t1 = time.time()
    iter += 1
    print('Full execution time ', t1-t0)


