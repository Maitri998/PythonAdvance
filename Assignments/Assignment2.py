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
                    emp['department'] = department  # Fixed: use = instead of ==
                print(f"Employee {emp_id} updated successfully.")
                return
        print(f"Employee with ID {emp_id} not found.")  # Moved outside loop

    # Delete Employees
    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp['id'] == emp_id:
                self.employees.remove(emp)
                print(f"Employee {emp_id} removed successfully.")
                return
        print(f"Employee {emp_id} does not exist.")  # Moved outside loop

    # Display Employees
    def display_employee(self):
        if not self.employees:
            print("No Employees to display.")
            return
        print("Employee Details are below:")
        for emp in self.employees:
            print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}")

# Example usage
def main():
    manager = EmployeeManagement()
    #add employees
    manager.add_employee(1, "Alice", "HR")
    manager.add_employee(2, "Bob", "IT")
    manager.add_employee(3, "Charlie", "Finance")
    manager.add_employee(4, "AliceA", "HR")
    manager.add_employee(5, "BobB", "Admin")
    manager.add_employee(6, "CharlieC", "Finance")
    #display added employees
    manager.display_employee()
    # Updating employees
    manager.update_employee(6, department="IT")
    
    #display updated employees
    manager.display_employee()

    # Deleting employees
    manager.delete_employee(3)

    # Displaying all remaining employees
    manager.display_employee()

if __name__ == "__main__":
    main()
