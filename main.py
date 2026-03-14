import flet as ft

def main(page: ft.Page):
    page.title = "RunReward"
    page.bgcolor = "white"
    page.padding = 0
    page.spacing = 0

    content_area = ft.Column(expand=True, scroll="auto")

    # 切换显示逻辑
    def show_content(index):
        content_area.controls.clear()
        if index == 0:
            content_area.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text("RunReward", size=28, weight="bold", color="blue"),
                        ft.Text("Turn every step into rewards", color="grey"),
                        ft.Container(height=20),
                        ft.ElevatedButton("Start New Run", bgcolor="blue", color="white", width=400),
                        ft.Container(height=10),
                        # 手动卡片布局
                        ft.Container(content=ft.Text("Total Distance: 0.0 km"), padding=20, bgcolor="white", border=ft.border.all(1, "grey300")),
                        ft.Container(content=ft.Text("Total Runs: 0"), padding=20, bgcolor="white", border=ft.border.all(1, "grey300")),
                        ft.Container(content=ft.Text("Total Points: 0"), padding=20, bgcolor="white", border=ft.border.all(1, "grey300")),
                    ]),
                    padding=20
                )
            )
        else:
            content_area.controls.append(ft.Container(content=ft.Text(f"页面 {index} 正在开发中...", size=20), padding=40))
        page.update()

    # 导航栏
    nav_bar = ft.Container(
        content=ft.Row(
            alignment="spaceAround",
            controls=[
                ft.TextButton("首页", on_click=lambda e: show_content(0)),
                ft.TextButton("历史", on_click=lambda e: show_content(1)),
                ft.TextButton("排行", on_click=lambda e: show_content(2)),
                ft.TextButton("成就", on_click=lambda e: show_content(3)),
            ],
        ),
        bgcolor="white",
        border=ft.border.only(top=ft.border.BorderSide(1, "grey300")),
    )

    page.add(content_area, nav_bar)
    show_content(0)

if __name__ == "__main__":
    ft.app(target=main)