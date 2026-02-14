from concurrent.futures import ThreadPoolExecutor
import threading
import data   # uses data.employees


# ---------------------------------
# Deduction Functions (independent)
# ---------------------------------

def sss_deduction(salary):
    print(f"SSS -> {threading.current_thread().name}")
    return salary * 0.045

def philhealth_deduction(salary):
    print(f"PhilHealth -> {threading.current_thread().name}")
    return salary * 0.03

def pagibig_deduction(salary):
    print(f"Pag-IBIG -> {threading.current_thread().name}")
    return salary * 0.02

def tax_deduction(salary):
    print(f"Tax -> {threading.current_thread().name}")
    return salary * 0.10


# ---------------------------------
# Task Parallelism for ONE employee
# ---------------------------------

def compute_deductions(employee):
    name = employee["name"]
    salary = employee["salary"]

    print(f"\nProcessing: {name} | Salary: {salary}")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            "SSS": executor.submit(sss_deduction, salary),
            "PhilHealth": executor.submit(philhealth_deduction, salary),
            "Pag-IBIG": executor.submit(pagibig_deduction, salary),
            "Tax": executor.submit(tax_deduction, salary)
        }

        results = {k: f.result() for k, f in futures.items()}

    total = sum(results.values())

    # display
    print("---- Deductions ----")
    for k, v in results.items():
        print(f"{k:<12}: {v:.2f}")
    print(f"Total        : {total:.2f}")

    return total


# ---------------------------------
# Run for all employees
# ---------------------------------

def main():
    for emp in data.employees:
        compute_deductions(emp)


if __name__ == "__main__":
    main()
#new code for task-parallelism