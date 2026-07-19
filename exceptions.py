class LLMError(Exception):
    '''this is the base class for all exceptions'''
class ExecutorError(Exception):
    '''This is the base class for all Executor Error'''
class ConnectionError(LLMError):
    '''this is a connection error'''
class TimeoutError(LLMError):
    '''this is a time out Error'''
class InvalidResponseError(LLMError):
    '''this is a invalid key error'''
class InvalidPlanError(Exception):
    '''This is a Inavlid Plan Error'''
class CircularDependencyError(ExecutorError):
    '''The Result of Dependent task is not found !!!'''
class ToolNotFoundError(Exception):
    '''This is a ToolNotFoundError'''