from jinja2 import (
    Template,
    Environment,
    PackageLoader,
    select_autoescape
)

from core.settings.settings import TEMPLATE_PACKAGE


env_templates = Environment(
    loader=PackageLoader(package_name=TEMPLATE_PACKAGE, package_path="templates"),
    autoescape=select_autoescape(["html", "xml"])
)


class BaseTemplateRender:

    template: str = None

    def get_template(self):

        if self.template is None:
            raise NotImplementedError(
                "You must implement template"
            )

        return env_templates.get_template(self.template)

    def __call__(self, **kwargs) -> Template:
        return self.get_template().render(**kwargs)
