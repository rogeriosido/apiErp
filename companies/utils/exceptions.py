from rest_framework.exceptions import APIException

class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = 'Funcionario não encontrado'
    default_code = 'not_found_employee'

class NotFoundGroup(APIException):
    status_code = 404
    default_detail = 'Grupo não encontrado'
    default_code = 'not_found_group'

class RequiredFields(APIException):
    status_code = 400
    default_detail = 'Envie os campos no padrão correto'
    default_code = 'error_required_field'

class NotFoundTaskStatus(APIException):
    status_code = 404
    default_detail = 'Status da tarefa não encontrado'
    default_code = 'not_found_task_status'

class NotFoundTask(APIException):
    status_code = 404
    default_detail = 'Tarefa não encontrado'
    default_code = 'not_found_task'

