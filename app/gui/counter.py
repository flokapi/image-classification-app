import flet as ft
import asyncio


class Counter(ft.Column):
    def __init__(self, api):
        super().__init__()
        self.api = api

        self.txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100)

        self.controls = [
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=self.minus),
                    self.txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=self.plus),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.ElevatedButton('Publish', on_click=self.publish)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]

    def minus(self, *args):
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.update()

    def plus(self, *args):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.update()

    async def publish(self, *args):
        await self.api['set_value'](int(self.txt_number.value))

    async def loop(self):
        while True:
            self.plus()
            await asyncio.sleep(5)
