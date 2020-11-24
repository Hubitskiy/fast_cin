from .container import Container

from users.injections import dependencies as user_dependencies
from core.injections import dependencies as core_dependencies

_dependencies = set()

_dependencies.update(user_dependencies)
_dependencies.update(core_dependencies)

container = Container()
container.register_set_dependencies(_dependencies)

resolve = container.resolve
