import json
import time


class PerformanceProfiler:
    def __init__(self):
        """
        Constructor
        """
        self.data = {
            "init_time_processor_clock": self.get_processor_clock(),
            "init_time_wall_clock": self.get_wall_clock(),
            "times": {},
        }

    def get_wall_clock(self):
        """
        External clock time. Includes timer.sleep() and other external time.
        """
        return time.perf_counter()

    def get_processor_clock(self):
        """
        Processor time. Only includes cpu cycles
        """
        return time.process_time()

    def set_start(self, name):
        self.data["times"][name] = {
            "name": name,
            "start_wall_clock": self.get_wall_clock(),
            "start_processor_clock": self.get_processor_clock(),
        }

    def set_final_times(self):
        end_wall_clock = self.get_wall_clock()
        end_processor_clock = self.get_processor_clock()

        self.data["final_time_processor_clock"] = end_processor_clock
        self.data["final_time_wall_clock"] = end_wall_clock

        self.data["total_time_processor_clock"] = (
            end_processor_clock - self.data["init_time_processor_clock"]
        )
        self.data["total_time_wall_clock"] = end_wall_clock - self.data["init_time_wall_clock"]

    def to_json(self):
        return json.dumps(self.data, default=str)

    def to_dict(self):
        return self.data

    def set_end(self, name, params):
        end_wall_clock = self.get_wall_clock()
        end_processor_clock = self.get_processor_clock()

        self.data["times"][name]["end_wall_clock"] = end_wall_clock
        self.data["times"][name]["end_processor_clock"] = end_processor_clock

        self.data["times"][name]["runtime_wall_clock"] = (
            end_wall_clock - self.data["times"][name]["start_wall_clock"]
        )
        self.data["times"][name]["runtime_processor_clock"] = (
            end_processor_clock - self.data["times"][name]["start_processor_clock"]
        )
        self.data["times"][name][
            "description"
        ] = f'{name} code block ran in {self.data["times"][name]["runtime_wall_clock"]} wall clock seconds'
        self.data["times"][name]["params"] = params