from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse


templates = None


def htmx_init(templates_):
    global templates
    templates = templates_


def htmx(template_name):
    def htmx_decorator(func):

        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            data = await func(request, *args, **kwargs)
            if data == None:
                data = {}

            file_name = f"{template_name}.html"
            context = {"request": request}
            context.update(data)
            return templates.TemplateResponse(file_name, context)

        return wrapper

    return htmx_decorator
