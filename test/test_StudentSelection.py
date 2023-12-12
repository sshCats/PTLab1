import pytest
from src.Types import DataType
from src.StudentSelection import StudentSelection


class TestStudentSelection:

    @pytest.fixture()
    def input_data(self) -> DataType:
        data = {
            'Иванов Иван Иванович': 82.0,
            'Петров Петр Петрович': 83.66666666666667
        }
        return data

    def test_find_students_in_third_quartile(self, input_data: DataType):
        students_in_third_quartile = StudentSelection(input_data).select()
        expected_result = {'Петров Петр Петрович': 83.66666666666667}
        assert students_in_third_quartile == expected_result
