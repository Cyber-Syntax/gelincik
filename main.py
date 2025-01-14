# The program that finds the final grade required to pass the final of the course whose midterm grade is known
# Written by CyberSyntax
# Created on 24.12.2022

# Türkiye AOF grade points:
# 84,00-100   – AA (passed)
# 77,00-83,99 – AB (passed)
# 71,00-76,99 – BA (passed)
# 66,00-70,99 – BB (passed)
# 61,00-65,99 – BC (passed)
# 56,00-60,99 – CB (passed)
# 50,00-55,99 – CC (passed)
# 46,00-49,99 – CD (GPA: Pass if above 2.00)
# 40,00-45,99 – DC (GPA: Pass if above 2.00)
# 33,00-39,99 – DD (GPA: Pass if above 2.00)
# 0-32,99     – FF (failed to pass)
# midterm 0.30, final 0.70 taken basis.


def main():
    midterm = get_midterm()
    calculate_final_grade(midterm)


def calculate_final_grade(midterm):
    """
    Calculate the required final exam grades to achieve each letter grade.
    """
    grades = {
        "AA": 84.00,
        "AB": 77.00,
        "BA": 71.00,
        "BB": 66.00,
        "BC": 61.00,
        "CB": 56.00,
        "CC": 50.00,
        "CD": 46.00,
        "DC": 40.00,
        "DD": 33.00,
        "FF": 0.00,
    }
    # threshold: Refers to a boundary or minimum value you need to cross to achieve a certain result.
    print("\nRequired final grades based on your midterm:")
    for grade, threshold in grades.items():
        required_final = (threshold - (midterm * 0.30)) / 0.70
        required_final = max(0, round(required_final, 2))  # Ensure no negative scores
        print(
            f"To achieve a grade of {grade}, you need a final exam score of at least: {required_final:.2f}"
        )


def get_midterm():
    """
    Prompt the user for the midterm grade, validating the input.
    """
    while True:
        try:
            midterm = float(input("Enter your midterm grade (0-100): "))
            if 0 <= midterm <= 100:
                return midterm
            else:
                print("Midterm grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()
