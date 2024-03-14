'''
Adapted from Professor Watters' code

Complete the homework by changing the code in the HW1 class.

'''

import sys 
sys.path.append('aima-python')
from agents import *

class HW1:

    def problem_a(self):
        '''
        Call the run() method with the reflex agent and the trivial vac environment 
        and return the environment status
        '''
        agent = ReflexVacuumAgent()
        TraceAgent(agent)
        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    def problem_b(self):
        '''
        Call the run() method with the model based agent and the trivial vac environment
        and return the environment status
        '''
        agent = ModelBasedVacuumAgent()
        TraceAgent(agent)
        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    def problem_c(self):
        '''
        Call the run() method with the random agent and the trivial vac environment
        and return the environment status
        '''
        agent = RandomVacuumAgent()
        TraceAgent(agent)
        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status
        return None 

    def problem_d(self):
        '''
        Compare the performance of the reflex agent, the model based agent, and random agent in the trivial vac environment.
        You will have to pass the agents and the environment to the comparison function, 
        this will require reviewing the documentation because the process is a little different.
        '''
        Environment = TrivialVacuumEnvironment
        agent_list = [ReflexVacuumAgent, ModelBasedVacuumAgent, RandomVacuumAgent]
        return compare_agents(Environment, agent_list)


def main():
    hw1 = HW1()
    print("Problem a:", hw1.problem_a())
    print("Problem b:", hw1.problem_b())
    print("Problem c:", hw1.problem_c())
    print("Problem d:", hw1.problem_d())

if __name__ == '__main__':
    main()
