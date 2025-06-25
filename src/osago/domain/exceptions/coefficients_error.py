from osago.domain.base_exceptions import ApplicationError, DomainError


class NotFoundError(ApplicationError):
    @property
    def title(self) -> str:
        return "Not found. Try other parameters."


class IncorrectParamsError(DomainError):
    parameter_name: str
    ge: int = 0

    @property
    def title(self) -> str:
        return f"Error occurred {self.parameter_name}, lower than {self.ge}"
