from src.pre_built.sorting import sort_by

mock = [
        {"date_posted": "2022-02-01", "max_salary": 2000, "min_salary": 3000},
        {"date_posted": "2021-03-05", "max_salary": 2500, "min_salary": 5000},
        {"date_posted": "2023-01-01", "max_salary": 1500, "min_salary": 4000},
    ]

mock_date = [mock[2], mock[0], mock[1]]
mock_max = [mock[1], mock[0], mock[2]]
mock_min = mock


def test_sort_by_criteria():
    sort_by(mock, "date_posted")
    assert mock == mock_date

    sort_by(mock, "max_salary")
    assert mock == mock_max

    sort_by(mock, "min_salary")
    assert mock == mock_min
