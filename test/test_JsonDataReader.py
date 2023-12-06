import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader


class TestJsonDataReader:

    @pytest.fixture()
    def mock_data(self) -> tuple[str, DataType]:
        json_content = """
        {
            "Иванов Иван Иванович":
          {
            "математика":80,
            "программирование":90,
            "литература":76
          },
            "Петров Петр Петрович":
          {
            "математика": 100,
            "социология": 90,
            "химия": 61
          }
        }
        """
        data = {
            'Иванов Иван Иванович':
                [('математика', 80), ('программирование', 90), ('литература', 76)],
            'Петров Петр Петрович':
                [('математика', 100), ('социология', 90), ('химия', 61)]
        }
        return json_content, data

    @pytest.fixture()
    def path_to_json(self,
                     mock_data, tmpdir) \
            -> tuple[str, DataType]:
        json_file = tmpdir.mkdir("datadir").join("my_data.json")
        json_file.write_text(mock_data[0], encoding='utf-8')
        return str(json_file), mock_data[1]

    def test_read_json(self,
                       path_to_json) \
            -> None:
        json_data = JsonDataReader().read(path_to_json[0])
        assert json_data == path_to_json[1]
