from typing import Set

import punq


class Container(punq.Container):

    def add_dependencies_to_container(self, injections: Set) -> None:
        for injections in injections:
            self.register(injections)

        return None
