class School:
    school_name = "ABC School"
    
    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return 'A+'
        else:
            return 'F'
print(School.calculate_grade(95))