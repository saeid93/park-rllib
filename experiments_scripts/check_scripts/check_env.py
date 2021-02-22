import park
import click
from park.param import parser


class CheckScripts:

    def __init__(self):
        """
        working now:
        1. load_balance
        2. abr_sim
        3. switch_scheduling
        4. simple_queue
        5. region_assignment

        not working:
        1. abr
        2. aqm
        3. congestion_control
        4. spark_sim
        5. query_optimizer
        6. cache
        7. tf_placement
        8. circuit_three_stage_transimpedance
        9. tf_placement_sim
        10. multi_dim_index
        11. spark

        """
        self.env = park.make('region_assignment')

    def check_env(self):
        i = 0
        obs = self.env.reset()
        while i < 20000:
            done = False
            self.env.reset()
            while not done:
                print(f"\niteration {i}:")
                action = self.env.action_space.sample()
                obs, reward, done, info = self.env.step(action)
                print(f"obs: {obs}, action: {action}, reward: {reward}"
                    f", done: {done}, info: {info}")
                i += 1

def main():
    """
    pass
    """
    ins = CheckScripts()
    ins.check_env()


if __name__ == "__main__":
    main()
