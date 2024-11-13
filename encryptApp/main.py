import flet as ft
from flet import (FilePickerResultEvent,FilePicker)
from assets.scripts.stegano import encode,decode
from assets.scripts.imageStegano import img_decrypt,img_encrypt,compress_image,remove_background
from assets.scripts.aes import encrypt,decrypt
from assets.scripts.folderzip import compress_file,zip_folder
from assets.scripts.image2pdf import images_to_pdf
import os 

def main(page: ft.Page): 

    
    page.title = "Encryption System"
    page.bgcolor = "#F5F5F5"
    
    # RESOLUTIONS
    page.window_min_width = 375
    page.window_min_height = 812
    page.window_max_height = 896
    page.window_max_width = 414 
    page.window_width = 414
    page.window_height = 896
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_full_screen = True,


    # THEME
    theme_color = "#663399"
    bg_color = "#F5FFFA"
    secondary_color = "#E6E6FA"

    page.theme_mode = ft.ThemeMode.LIGHT

    # COLORS



    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [   
                    home,
                ],
            )
        )

        if page.route == "/stegno":
            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("HIDE IMAGE OR TEXT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ],
                            ),
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.TEXT_FIELDS_OUTLINED),
                                                        title=ft.Text("Hide Text In Image",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Image Stegnography"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Hide Text",color=ft.colors.BLACK,on_click=lambda _:page.go('/hide-text')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.HIDE_IMAGE_SHARP),
                                                        title=ft.Text("Show Text From Image",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Image Stegnography"),
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Reveal Text",color=ft.colors.BLACK,on_click=lambda _:page.go('/show-text')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.HIDE_IMAGE_SHARP),
                                                        title=ft.Text("Hide Image In Image",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Image Stegnography"),
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Hide Image",color=ft.colors.BLACK,on_click=lambda _:page.go('/hide-image')),

                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.HIDE_IMAGE_SHARP),
                                                        title=ft.Text("Show Image From Image",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Image Stegnography"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Reveal Image",color=ft.colors.BLACK,on_click=lambda _:page.go('/show-image')), 
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('"Please use jpeg or png files as image."',weight=ft.FontWeight.BOLD),
                                                height=60, 
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )

        if page.route == "/hide-text":

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )

            def text_stegno_input(e):
                check = encode(select_image_path.value,data.value,save_file_path.value)
                print(check)
                if check == True:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True 
                    page.update()
                else:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                data.value = ""

            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_image_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.png'):
                    save_file_path.value += ".png"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])

            data = ft.TextField(
                label="Enter Data To Hide",
                border_color=theme_color,
                border_width=3,
                border_radius=15,
                multiline=True,
                )
            

            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("HIDE TEXT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/stegno'), 
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                data,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Image",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_image_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=text_stegno_input,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )

        if page.route == "/show-text":
            def text_stegno_output(e):
                check = decode(select_image_path.value)
                print(check)
                if check == False:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                else:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True
                    show_text_stegno.value=check
                    page.update()
                    

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("The given Image contain no Hidden Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )


            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_image_path.update()
                page.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            

            page.overlay.extend([pick_files_dialog])

            show_text_stegno = ft.Text(color=ft.colors.BLACK,weight=ft.FontWeight.W_300,selectable=True)

            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("SHOW TEXT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/stegno'), 
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Image",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_image_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=text_stegno_output,
                                ),
                                ft.Container(
                                    content=show_text_stegno,
                                    bgcolor=secondary_color,
                                    width=414,
                                    expand=True,
                                )
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )

        if page.route == "/hide-image":

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                dlg_modal_work_img.open = False
                dlg_modal_error_img.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )

            dlg_modal_work_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )

            dlg_modal_error_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )

            def image_stegno_input(e):

                check = img_encrypt(select_image_path.value,save_file_path.value)
                print(f'Error is : {check}')
                if check == True:
                    print('check work') 
                    page.dialog = dlg_modal_work_img
                    dlg_modal_work_img.open = True 
                    page.update()
                else:
                    page.dialog = dlg_modal_error_img
                    dlg_modal_error_img.open = True
                    page.update()

            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_image_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.png'):
                    save_file_path.value += ".png"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])
            

            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("HIDE IMAGE",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.HOME_OUTLINED,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Image To Hide",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_image_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=image_stegno_input,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )

        if page.route == "/show-image":

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                dlg_modal_work_img.open = False
                dlg_modal_error_img.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )

            dlg_modal_work_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )

            dlg_modal_error_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )
            
            def image_stegno_output(e):

                check = img_decrypt(select_image_path.value,save_file_path.value)
                print(f'Error is : {check}')
                if check == True:
                    print('check work')
                    page.dialog = dlg_modal_work_img
                    dlg_modal_work_img.open = True 
                    page.update()
                else:
                    page.dialog = dlg_modal_error_img
                    dlg_modal_error_img.open = True
                    page.update()

            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!" 
                )

                select_image_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.png'):
                    save_file_path.value += ".png"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])
            

            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("REVEAL IMAGE",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/stegno'), 
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Image To Show",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_image_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=image_stegno_output,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )
        
        if page.route == "/encrypt":

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                # on_dismiss=lambda e: page.go("/encrypt-home"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/stegno"),
            )


            def pick_files_result(e: FilePickerResultEvent):
                select_file_path.disabled = False
                select_file_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_file_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.bin'):
                    save_file_path.value += ".bin"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            key = ft.Text('',selectable=True,weight=ft.FontWeight.W_300)  


            def encrypt_file(e):
                key_value = encrypt(select_file_path.value,save_file_path.value)
                if key_value == False:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                else:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True
                    key.value = key_value 
                    page.update()
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])

            page.views.append(
                ft.View(
                    '/encrypt',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("ENCRYPT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/encrypt-home'),
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select File To Encrypt",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                key,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=encrypt_file,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                    ]
                )
            )
        
        if page.route == "/decrypt":
            extension = ft.Dropdown(
                options=[
                    ft.dropdown.Option('.jpg'),
                    ft.dropdown.Option('.txt'),
                ],
                label="Select Extension"
            )

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/encrypt-home"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/encrypt-home"),
            )

            def decrypt_file(e):
                key_val = eval(data.value)
                check = decrypt(select_image_path.value,save_file_path.value,key_val)
                if check == True:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True 
                    page.update()
                else:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                data.value = ""
            
            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_image_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                save_file_path.value += extension.value
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])

            data = ft.TextField(
                label="Enter Key",
                border_color=ft.colors.BLACK,
                border_radius=5,
                multiline=True,
                )
            
            page.views.append(
                ft.View(
                    '/decrypt',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("DECRYPT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/encrypt-home'),
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                data,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Encrypted File",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_image_path,
                                extension,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=decrypt_file,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )

        if page.route == '/encrypt-home':
            page.views.append(
                ft.View(
                    '/encrypt-home',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("ENCRYPT IMAGE OR TEXT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ]
                            ),
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.NO_ENCRYPTION),
                                                        title=ft.Text("Encrypt",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("File Encryption"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Secure File",color=ft.colors.BLACK,on_click=lambda _:page.go('/encrypt')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.LOCK_OPEN),
                                                        title=ft.Text("Decrypt",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("File Decryption"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("See File",color=ft.colors.BLACK,on_click=lambda _:page.go('/decrypt')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.LOOKS_TWO_SHARP),
                                                        title=ft.Text("2 Factor Encryption",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("AWS with Stegnography"),
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Hide Data",color=ft.colors.BLACK,on_click=lambda _:page.go('/two-factor-encrypt')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.LOOKS_TWO_SHARP),
                                                        title=ft.Text("2 Factor Decryption",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("AWS with Stegnography"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Reveal Data",color=ft.colors.BLACK,on_click=lambda _:page.go('/two-factor-decrypt')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END, 
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ), 
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('"You can encrypt image and txt file type"',weight=ft.FontWeight.BOLD),
                                                height=60, 
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    ),
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('"Use jpg, png files"',weight=ft.FontWeight.BOLD),
                                                height=60, 
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        
        if page.route == '/compress-home':
            page.views.append(
                ft.View(
                    '/compress-home',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("COMPRESS",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ]
                            ),
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.NO_ENCRYPTION),
                                                        title=ft.Text("Compress Image",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Image Compression"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Compress Image",color=ft.colors.BLACK,on_click=lambda _:page.go('/compress-img')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.LOCK_OPEN),
                                                        title=ft.Text("Compress Text",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Text Compression"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Compress Text",color=ft.colors.BLACK,on_click=lambda _:page.go('/compress-file')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('"You can compress image and txt"',weight=ft.FontWeight.BOLD),
                                                height=60, 
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    )
                                ]
                            )
                        )     
                    ]
                )
            )
        
        if page.route == '/two-factor-encrypt':

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/encrypt-home"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/encrypt-home"),
            )


            def pick_files_result(e: FilePickerResultEvent):
                select_file_path.disabled = False
                select_file_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_file_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.bin'):
                    save_file_path.value += ".bin"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            def remove_last_component(path):
                # Get the directory portion of the path
                directory = os.path.dirname(path)
                
                return directory
            

            def two_factor(e):
                key_enc = encrypt(select_file_path.value,save_file_path.value)
                pic_path = remove_last_component(save_file_path.value)+"/key.png"
                check = encode('key.png',key_enc,pic_path)

                if check == False or key_enc == False:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                else:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True
                    page.update()

            page.overlay.extend([pick_files_dialog,save_file_dialog])

            page.views.append(
                ft.View(
                    '/two-factor-encrypt',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("2 FACTOR ENCRYPT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/encrypt-home'),
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select File To Encrypt",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=two_factor,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                    ]
                )
            )
        
        if page.route == '/two-factor-decrypt':

            extension = ft.Dropdown(
                options=[
                    ft.dropdown.Option('.jpg'),
                    ft.dropdown.Option('.txt'),
                ],
                label="Select Extension"
            )

            def close_dlg(e):
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/encrypt-home"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/encrypt-home"),
            )
            
            def pick_files_result(e: FilePickerResultEvent):
                select_file_path.disabled = False
                select_file_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_file_path.update()
                page.update()
            
            def key_files_result(e: FilePickerResultEvent):
                key_file_path.disabled = False
                key_file_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                key_file_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                save_file_path.value += extension.value
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            key_file_dialog = FilePicker(on_result=key_files_result)
            key_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog,key_file_dialog]) 

            def two_factor_decrypt(e):
                key = decode(key_file_path.value)
                check = decrypt(select_file_path.value,save_file_path.value,eval(key))

                if check == False:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                else:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True
                    page.update()

            
            page.views.append(
                ft.View(
                    'two-factor-decrypt',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("2 Factor Decrypt",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/encrypt-home'),
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Encrypted File",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Key Image",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:key_file_dialog.pick_files(allow_multiple=False),
                                ),
                                key_file_path,
                                extension,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=two_factor_decrypt,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                    ]
                )
            )
        
        if page.route == '/compress-img':

            def close_dlg(e): 
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/compress-home"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/compress-home"),
            )


            def pick_files_result(e: FilePickerResultEvent): 
                select_file_path.disabled = False
                select_file_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_file_path.update() 
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.jpg'):
                    save_file_path.value += ".jpg" 
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])

            quality = ft.Slider(min=0, max=100, divisions=10, label="{value}%")    
 
            def compress(e):
                check = compress_image(select_file_path.value,save_file_path.value,quality.value)
                if check == True:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True
                    quality.value = 20
                    page.update()
                else:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()


            page.views.append(
                ft.View(
                    '/compress-img',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("COMPRESS IMAGE",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/compress-home'), 
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select File To Compress",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path, 
                                quality,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=compress, 
                                ),
                            ],
                            alignment=ft.alignment.center,
                        ),
                        ft.Card(
                            content=(
                                ft.Container(
                                    content=ft.Text('"Lower slider value for LOWER QUALITY"',weight=ft.FontWeight.BOLD), 
                                    height=60, 
                                    width=414,
                                    alignment=ft.alignment.center
                                )
                            )
                        )
                    ]
                )
            )
        
        if page.route == '/compress-file':

            def close_dlg(e): 
                dlg_modal_work.open = False
                dlg_modal_error.open = False
                page.update()

            dlg_modal_work = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/compress-home"),
            )


            dlg_modal_error = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/compress-home"), 
            )


            def pick_files_result(e: FilePickerResultEvent):
                select_file_path.disabled = False
                select_file_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_file_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.gz'):
                    save_file_path.value += ".gz"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )


            def compressed_file(e):
                save = select_file_path.value + ".gz"
                key_value = compress_file(select_file_path.value,save)
                if key_value == False:
                    page.dialog = dlg_modal_error
                    dlg_modal_error.open = True
                    page.update()
                else:
                    page.dialog = dlg_modal_work
                    dlg_modal_work.open = True
                    page.update()
            
            page.overlay.extend([pick_files_dialog])


            page.views.append(
                ft.View(
                    '/compress-file',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("COMPRESS FILE",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/encrypt-home'),
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select File To Compress",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=compressed_file,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                    ]
                )
            )
        
        if page.route == "/convert-image":

            def close_dlg(e):
                dlg_modal_work_img.open = False
                dlg_modal_error_img.open = False
                page.update()

            dlg_modal_work_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/"),
            )


            dlg_modal_error_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/"),
            )

            
            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_image_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.pdf'):
                    save_file_path.value += ".pdf"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])
            
            def image2pdf(e):

                check = images_to_pdf(select_image_path.value,save_file_path.value)
                print(select_image_path.value)
                print(f'Error is : {check}')
                if check == True:
                    print('check work')
                    page.dialog = dlg_modal_work_img
                    dlg_modal_work_img.open = True 
                    page.update()
                else:
                    page.dialog = dlg_modal_error_img
                    dlg_modal_error_img.open = True
                    page.update()

            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("IMAGE TO PDF",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ],
                                center_title=True, 
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Image To Add",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=True),
                                ),
                                select_image_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=image2pdf,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )

        if page.route == '/more':
            page.views.append(
                ft.View(
                    '/more',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("MORE",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ]
                            ),
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        leading=ft.Icon(ft.icons.NO_ENCRYPTION),
                                                        title=ft.Text("Remove Background",weight=ft.FontWeight.W_900,size=20),
                                                        subtitle=ft.Text("Image Background Remove"), 
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.CupertinoButton("Remove Background Image",color=ft.colors.BLACK,on_click=lambda _:page.go('/bg-remove')),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.END,
                                                    )
                                                ]
                                            )
                                        ),
                                        color=secondary_color,
                                    ),
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('"use png or jpg formats"',weight=ft.FontWeight.BOLD),
                                                height=60, 
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    )
                                ]
                            )
                        )     
                    ]
                )
            )

        if page.route == "/bg-remove":

            def close_dlg(e):
                dlg_modal_work_img.open = False
                dlg_modal_error_img.open = False
                page.update()

            dlg_modal_work_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Successfull"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/more"),
            )

            dlg_modal_error_img = ft.AlertDialog(
                modal=True,
                title=ft.Text("Please Check Your Input Data"),
                # content=ft.Text("Do you really want to delete all those files?"),
                actions=[
                    ft.TextButton("Done", on_click=close_dlg),
                    # ft.TextButton("No", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: page.go("/more"),
            )

            def bg_remove(e):

                check = remove_background(select_image_path.value,save_file_path.value)
                print(f'Error is : {check}')
                if check == True:
                    print('check work')
                    page.dialog = dlg_modal_work_img
                    dlg_modal_work_img.open = True 
                    page.update()
                else:
                    page.dialog = dlg_modal_error_img
                    dlg_modal_error_img.open = True
                    page.update()

            def pick_files_result(e: FilePickerResultEvent):
                select_image_path.disabled = False
                select_image_path.value = (
                    ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
                )

                select_image_path.update()
                page.update()

            # CHOOSE OUTPUT FILE LOCATION

            def save_file_result(e: FilePickerResultEvent):
                save_file_path.disabled = False
                save_file_path.value = e.path if e.path else "Cancelled!"
                if not save_file_path.value.lower().endswith('.png'):
                    save_file_path.value += ".png"
                save_file_path.update()

            pick_files_dialog = FilePicker(on_result=pick_files_result)
            select_image_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True, 
                )
            
            save_file_dialog = FilePicker(on_result=save_file_result)
            save_file_path = ft.Text(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_500,
                disabled=True)
            
            page.overlay.extend([pick_files_dialog,save_file_dialog])
            

            page.views.append(
                ft.Column(
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("REMOVE BACKGROUND",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/more'), 
                                    )
                                ]
                            ),
                        ft.Column(
                            [
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Text("Select Image",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=False),
                                ),
                                select_image_path,
                                ft.CupertinoButton(
                                    content=ft.Row( 
                                        [
                                            ft.Text("Select Output Path",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=lambda _:save_file_dialog.save_file(),
                                ),
                                save_file_path,
                                ft.CupertinoButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.icons.SEND_SHARP),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=theme_color,
                                    alignment=ft.alignment.center,
                                    on_click=bg_remove,
                                ),
                            ],
                            alignment=ft.alignment.center,
                        )
                        
                    ]
                )
            )

        if page.route == '/about':
            page.views.append(
                ft.View(
                    '/about',
                    [
                        ft.AppBar(
                                leading=ft.Icon(ft.icons.HIDE_IMAGE_OUTLINED,color=ft.colors.WHITE,size=30),
                                bgcolor=theme_color,
                                title=ft.Text("ABOUT",color=ft.colors.WHITE,weight=ft.FontWeight.W_900),
                                actions=[
                                    ft.IconButton(
                                        ft.icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                        icon_color=ft.colors.WHITE,
                                        on_click=lambda _:page.go('/'),
                                    )
                                ]
                            ),
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('An ALL-IN-ONE Security App \nFor Your Personal And Professional Needs',weight=ft.FontWeight.BOLD,text_align="center"),
                                                height=120, 
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    ),
                                    ft.Card(
                                        content=(
                                            ft.Container(
                                                content=ft.Text('Version\n 0.0.1',weight=ft.FontWeight.BOLD,text_align="center"),
                                                height=60,
                                                width=414,
                                                alignment=ft.alignment.center
                                            )
                                        )
                                    ),
                                ]
                            )
                        )     
                    ]
                )
            )


        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    menu = ft.Column(
        width=414,
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        padding=30,
                        bgcolor=theme_color,
                        expand=True,
                        height=220,
                        margin=5,
                        border_radius=10,
                        content=ft.Column(
                            controls=[
                                ft.Image(src=f"images/hide.png",width=100,height=100,fit=ft.ImageFit.CONTAIN,color=ft.colors.WHITE), 
                                ft.Text("Hide Image",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20,text_align="center"),
                                ft.Text("Or Text",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20,text_align="center")
                            ],
                            alignment="center",
                        ),
                        alignment=ft.alignment.center,
                        on_click=lambda _:page.go('/stegno'),
                    ),
                    ft.Container(
                        padding=30,
                        bgcolor=theme_color,
                        expand=True,
                        height=220, 
                        margin=5,
                        border_radius=10,
                        content=ft.Column(
                            controls=[
                                ft.Image(src=f"/images/encryption.png",width=100,height=100,fit=ft.ImageFit.CONTAIN,color=ft.colors.WHITE),
                                ft.Text("Encrypt",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20,)
                            ],
                            alignment=ft.alignment.center,
                        ),
                        alignment=ft.alignment.center,
                        on_click=lambda _:page.go('/encrypt-home')
                    )
                ]
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        padding=30,
                        bgcolor=theme_color,
                        expand=True,
                        height=220,
                        margin=5,
                        border_radius=10,
                        content=ft.Column(
                            controls=[
                                ft.Image(src=f"images/compress.png",width=100,height=100,fit=ft.ImageFit.CONTAIN,color=ft.colors.WHITE), 
                                ft.Text("Compress File",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20)
                            ],
                            alignment="center",
                        ), 
                        alignment=ft.alignment.center,
                        on_click=lambda _:page.go('/compress-home')
                    ),
                    ft.Container(
                        padding=30,
                        bgcolor=theme_color,
                        expand=True,
                        height=220,
                        margin=5,
                        border_radius=10,
                        content=ft.Column(
                            controls=[
                                ft.Image(src=f"/images/convert.png",width=100,height=100,fit=ft.ImageFit.CONTAIN,color=ft.colors.WHITE),
                                ft.Text("Convert Files",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20)
                            ],
                            alignment="center",
                        ),
                        alignment=ft.alignment.center,
                        on_click=lambda _:page.go('/convert-image') 
                    )
                ]
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        padding=30,
                        bgcolor=theme_color,
                        expand=True,
                        height=220,
                        margin=5,
                        border_radius=10,
                        content=ft.Column(
                            controls=[
                                ft.Icon(ft.icons.MORE_ROUNDED,size=75,color=ft.colors.WHITE),
                                ft.Text("MORE FEATURES",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20)
                            ],
                            alignment="center",
                        ), 
                        alignment=ft.alignment.center,
                        on_click=lambda _:page.go('/more')
                    ),
                    ft.Container(
                        padding=30,
                        bgcolor=theme_color,
                        expand=True,
                        height=220,
                        margin=5,
                        border_radius=10,
                        content=ft.Column(
                            controls=[
                                ft.Icon(ft.icons.INFO_OUTLINE_ROUNDED,size=75,color=ft.colors.WHITE,),
                                ft.Text("About App",weight=ft.FontWeight.W_900,color=ft.colors.WHITE,size=20,text_align="center")
                            ],
                            alignment="center",
                        ),
                        alignment=ft.alignment.center,
                        on_click=lambda _:page.go('/about')
                    )
                ]
            ),
        ]
    )

    home = ft.SafeArea(
        expand=True,
        content=ft.Container(
            width=414,
            expand=True,
            bgcolor=bg_color,
            border_radius=10,
            content=menu
        )
    )

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


    page.update()

ft.app(main,assets_dir="assets")


