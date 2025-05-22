import flet as ft


#Funcion principal
def main(page: ft.Page): 

    page.title="Mi página"
    page.theme_mode = ft.ThemeMode.DARK
    page.appbar=ft.CupertinoAppBar(
        middle=ft.Text("Florencia Leytón Tamayo", size=30,color=ft.Colors.LIGHT_BLUE_400)
    )

    page.theme=ft.Theme(
        color_scheme=ft.ColorScheme(
        primary=ft.Colors.LIGHT_BLUE_300,
        primary_container=ft.Colors.DEEP_ORANGE_200,
        on_primary=ft.Colors.WHITE,
        secondary=ft.Colors.LIGHT_BLUE_300,
        secondary_container=ft.Colors.DEEP_ORANGE_200,
        on_secondary=ft.Colors.WHITE,
        ),
    )

    #img=ft.Image(
        #src=f"https://pythonlife.in/images/pythonlogo.png", 
       # width=150, 
       # height=150
   # )

    #Componentes separados
    menu=ft.Tabs(
        tabs=[
            ft.Tab(
                icon=ft.Icons.DOOR_FRONT_DOOR, 
                text="Inicio",
                content=
                    ft.Text(
                        "This is Tab 1", 
                        color=ft.Colors.LIGHT_BLUE_400),
                        container=ft.Container(
                            ft.ElevatedButton(
                                "Tercero B", 
                                icon=ft.Icons.STAR_ROUNDED, 
                                icon_color=ft.Colors.GREEN_ACCENT_400) 

                        )
                    
                ),
            ft.Tab(text="Dashboard",icon=ft.Icons.SMART_TOY),
            ft.Tab(text="Acerca de",icon=ft.Icons.MEMORY),
            ft.Tab(text="Configuración",icon=ft.Icons.SETTINGS_ETHERNET)
        ],
        tab_alignment=ft.TabAlignment.CENTER
        
    )

  


    page.add(  #Metodo add nos permite agregar componentes a la interfaz
      #Componentes basicos
      menu,

    )


ft.app(main) 

                #content=
                  # ft.ElevatedButton(
                    #            text="Tercero B",
                     #           on_click=lambda e:page.open_url("https://www.google.com"),
                     #           icon=ft.Icons.STAR_ROUNDED, 
                      #          icon_color=ft.Colors.GREEN_ACCENT_400
                    #),