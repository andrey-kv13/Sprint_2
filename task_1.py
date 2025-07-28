class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")
 # напиши свой код здесь
class ExtendedCase(Case):
   def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
       self.precondition = precondition
       self.environment = environment
       super().__init__(test_case_id, name, step_description, expected_result)
   
   def print_test_case_info(self):
       print(f"ID тест-кейса:  {self.test_case_id}"
             f"\nНазвание: {self.name}"
             f"\nОкружение: {self.environment}"
             f"\nПредусловие: {self.precondition}"
             f"\nОписание шага: {self.step_description}"
             f"\nОжидаемый результат: {self.expected_result}")

case = ExtendedCase(
    precondition="Открыть сервис",
    environment="Яндекс Браузер",
    test_case_id="1",
    name="Наличие кнопки Принять",
    step_description="1. Открыть вкладку приёма документов 2. Проверить наличие кнопки",
    expected_result="Кнопка доступна"
)

case.print_test_case_info()