# -*- coding: utf-8 -*-
from src.Types import DataType
from src.DataReader import DataReader
import json


class JsonDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            self.students = json.load(file)

            # Convert to tuples in the data
            for student, subjects in self.students.items():
                self.students[student] = [tuple(subject) for subject
                                          in subjects.items()]

        return self.students
