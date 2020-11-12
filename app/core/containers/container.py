from typing import Set

import punq


class Container(punq.Container):

    def register_set_dependencies(self, dependencies: Set):
        for dependence in dependencies:
            self.register(dependence)
