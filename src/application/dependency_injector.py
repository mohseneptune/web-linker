import inspect


def inject_dependencies(handler, dependencies):
    """
    Inject dependencies into a handler function.
    """
    # Get the handler's parameters.
    params = inspect.signature(handler).parameters
    # Get the dependencies that the handler requires.
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }

    # Define a new function that calls the handler with the dependencies.
    def new_handler(message):
        return handler(message, **deps)

    # Return the new function.
    return new_handler
