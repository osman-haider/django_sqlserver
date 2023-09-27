from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from sql_server import get_connection

def employee_list(request):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    connection.close()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Employees (EmployeeID, FirstName, LastName) VALUES (?, ?, ?)",
                       (employee_id, first_name, last_name))
        connection.commit()
        connection.close()
        return redirect('employee_list')
    return render(request, 'employee_create.html')

def employee_update(request, employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Write your update query with placeholders
        update_query = """
        UPDATE Employees
        SET FirstName = ?, LastName = ?
        WHERE EmployeeID = ?
        """
        
        # Execute the query with parameters
        cursor.execute(update_query, [first_name, last_name, employee_id])
        connection.commit()  # Commit the transaction

        return redirect('employee_list')

    return render(request, 'employee_update.html')

def employee_delete(request, employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    if request.method == 'POST':
        # Execute the DELETE query
        with connection.cursor() as cursor:
            delete_query = """
            DELETE FROM employees
            WHERE EmployeeID = ?
            """
            cursor.execute(delete_query, [employee_id])

        # Commit the transaction
        connection.commit()

        return redirect('employee_list')

    return render(request, 'employee_delete.html')
