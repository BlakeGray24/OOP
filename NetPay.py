import PayrollDeductionClass as prd
import EmployeeClass as e


employee = e.Employee('Jimmy Smith',58475,'Information Systems','Developer', 6800)

deduct1 = prd.Payroll('Food Court','8/14/2022', 22.50, 39119)
deduct2 = prd.Payroll('Gift Contribution','8/12/2022', 25.00, 58475)
deduct3 = prd.Payroll('food Court','8/17/2022', 15.25, 21547)
deduct4 = prd.Payroll('Vending Machine','8/22/2022', 3.00, 58475)
deduct5 = prd.Payroll('Vending Machine','8/14/2022', 2.75, 58475)


#######  Report printing ################


print('*** Employee pay ***')
print('Name:',employee.get_name())
print('ID number:',employee.get_id())
print('Department:',employee.get_dept())
print('Gross pay: ',float(employee.get_salary()),sep='')
print('Net Pay: $',employee.get_salary()-deduct2.get_charge()-deduct4.get_charge()-deduct5.get_charge(),sep='')
