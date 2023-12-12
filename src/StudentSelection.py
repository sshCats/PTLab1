# -*- coding: utf-8 -*-

class StudentSelection:

    def __init__(self, data: dict) -> None:
        self.data: dict = data
        self.elements_in_third_quartile: dict = {}

    def select(self) -> dict:
        values = list(self.data.values())
        sorted_values = sorted(values)
        index_third_quartile = int(0.75 * len(sorted_values))
        third_quartile = sorted_values[index_third_quartile]
        self.elements_in_third_quartile = {key: value for key, value in
                                           self.data.items() if
                                           value >= third_quartile}

        return self.elements_in_third_quartile
