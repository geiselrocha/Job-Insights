from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    results = []
    for job in jobs_list:
        if (
            job["max_salary"] not in results
            and job["max_salary"].isdigit()
        ):
            results.append(int(job["max_salary"]))
    return max(results)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    results = []
    for job in jobs_list:
        if (
            job["min_salary"] not in results
            and job["min_salary"].isdigit()
        ):
            results.append(int(job["min_salary"]))
    return min(results)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        int_salary = int(salary)
    except Exception:
        raise ValueError

    if min_salary > max_salary:
        raise ValueError
    else:
        return min_salary <= int_salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    results = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                results.append(job)
        except ValueError:
            pass
    return results
