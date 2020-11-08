from .container import Container


container = Container()
container.add_dependencies_to_container(None)

resolve = container.resolve
