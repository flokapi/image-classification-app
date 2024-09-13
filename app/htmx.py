from functools import wraps
from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse


templates = None


def htmx_init(templates_):
    global templates
    templates = templates_


def _is_hx_request(request: Request) -> bool:
    return "HX-Request" in request.headers


def htmx(template_name):
    def htmx_decorator(func):

        @wraps(func)
        def wrapper(request: Request, *args, **kwargs):
            data = func(request, *args, **kwargs)
            if data == None:
                data = {}

            file_name = f"{template_name}.html"
            context = {"request": request}
            context.update(data)
            return templates.TemplateResponse(file_name, context)

            # if _is_hx_request(request):
            #     if template_name == None:
            #         return HTMLResponse(data)
            #     else:
            #         file_name = f"{template_name}.html"
            #         context = {"request": request}
            #         context.update(data)
            #         return templates.TemplateResponse(file_name, context)
            # else:
            #     return JSONResponse(content=data)

        return wrapper

    return htmx_decorator
