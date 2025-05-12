class EmployeeManagement:
    def __init__(self):
        self.employees = []

    # Add Employees
    def add_employee(self, emp_id, name, department):
        for emp in self.employees:
            if emp['id'] == emp_id:
                print(f"Employee {name} with ID {emp_id} already exists.")
                return
        self.employees.append({
            'id': emp_id,
            'name': name,
            'department': department
        })
        print(f"Employee {name} with Employee ID {emp_id} has been added successfully.")

    # Update Employees
    def update_employee(self, emp_id, name=None, department=None):
        for emp in self.employees:
            if emp['id'] == emp_id:
                if name:
                    emp['name'] = name
                if department:
                    emp['department'] = department 
                print(f"Employee {emp_id} updated successfully.")
                return
        print(f"Employee with ID {emp_id} not found.")  

    # Delete Employees
    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp['id'] == emp_id:
                self.employees.remove(emp)
                print(f"Employee {emp_id} removed successfully.")
                return
        print(f"Employee {emp_id} does not exist.") \
    # Display Employees
    def display_employee(self):
        if not self.employees:
            print("No Employees to display.")
            return
        print("Employee Details are below:")
        for emp in self.employees:
            print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}")

#usage
def main():
    manager = EmployeeManagement()
    manager.add_employee(1, "Alice", "HR")
    manager.add_employee(2, "Bob", "IT")
    manager.add_employee(3, "Charlie", "Finance")

    # Updating employees
    manager.update_employee(2, department="Finance")

    # Deleting employees
    manager.delete_employee(3)

    #  remaining employees
    manager.display_employee()

if __name__ == "__main__":
    main()
