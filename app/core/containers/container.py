from typing import Set

import punq


class Container(punq.Container):

    def register_dependencies(self, dependencies: Set) -> None:
        for dependence in dependencies:
            self.register(dependence)

        return None
