def transform_employee(employee):
    
    transformed = {}

    transformed['emp_id'] = employee['empId']

    transformed['name'] = (
        employee['name'].upper()
    )

    new_salary = (
        employee['salary'] * 1.10
    )

    transformed['salary'] = (
        round(new_salary, 2)
    )

    transformed['bonus'] = (
        round(new_salary * 0.10, 2)
    )

    transformed['department'] = (
        employee['department']
    )

    return transformed