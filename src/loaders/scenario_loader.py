from myelin import ScenarioLoader
import json

class MyScenarioLoader(ScenarioLoader):
    default_id = '100_time_units'

    def load(self, scenario_id: str):
        data = json.load(open(f'scenarios/{scenario_id}.json'))
        return {
            'dt': data['dt'],
            'duration': data['duration'],
            'target': data['target'],
            'state0': tuple(data['state0'])
        }