from fastapi.templating import Jinja2Templates

from ..htmx import htmx_init


templates = Jinja2Templates(directory="app/templates/")

htmx_init(templates)
