"""rponce 66 web"""

import os
import flet as ft
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from dict_textos import textos

# Cargar variables de entorno
load_dotenv()


class WebApp:
    """Clase representado a la WebApp"""

    def __init__(self, page: ft.Page):
        self.page = page
        self.current_language = 'es'
        self.current_page = 'home'

        # Configurar la página
        self.page.title = 'rponce66 - Soft & Finances'
        self.page.padding = 0
        self.page.spacing = 0

        # Variables para responsive
        self.is_mobile = False

        # Controles principales
        self.header_container = None
        self.body_container = None
        self.footer_container = None
        self.mobile_drawer = None

        # Configurar responsive
        self.page.on_resize = self.on_page_resize

        self.setup_page()

    def on_page_resize(self, e):  # pylint: disable=unused-argument
        """Manejar cambios de tamaño de pantalla"""
        self.is_mobile = self.page.width < 768
        self.update_layout()

    def update_layout(self):
        """Actualizar layout según el tamaño de la pantalla"""
        self.page.controls.clear()
        self.setup_page()
        self.page.update()

    def change_language(self, lang):
        """Cambiar idioma de la aplicación"""
        self.current_language = lang
        self.update_layout()

    def navigate_to(self, page_name):
        """Navegar a una página específica"""
        self.current_page = page_name
        t = textos[self.current_language]

        if self.mobile_drawer:
            self.mobile_drawer.open = False

        # Actualizar el título de la página según la navegación
        page_titles = {
            'home': 'rponce66 - Soft & Finances',
            'about': t['page_tittle']['about'],
            'services': t['page_tittle']['services'],
            'blog': t['page_tittle']['blog'],
            'contact': t['page_tittle']['contact'],
            'service_0': t['page_tittle']['service_0'],
            'service_1': t['page_tittle']['service_1'],
            'service_2': t['page_tittle']['service_2'],
            'service_3': t['page_tittle']['service_3'],
            'service_4': t['page_tittle']['service_4'],
            'service_5': t['page_tittle']['service_5']
        }

        if page_name in page_titles:
            self.page.title = page_titles[page_name]

        self.update_layout()

    def create_logo(self, size=80):
        """Crear logo clickleable"""
        return ft.Container(
            content=ft.Image(
                src="rponce66_01sf.png",
                width=size * 2.5,
                height=size,
                fit=ft.ImageFit.CONTAIN
            ),
            padding=ft.padding.all(7),
            border_radius=8,
            on_click=lambda _: self.navigate_to('home')
        )

    def create_flag_button(self, lang, flag):  # pylint: disable=unused-argument
        """Crear botón de bandera para cambiar de idioma"""
        flags = {
            'es': '114.png',
            'en': '320.png',
            'pt': '310.png'
        }

        tooltips = {
            'es': 'Español',
            'en': 'English',
            'pt': 'Português'
        }

        return ft.Container(
            content=ft.Image(
                src=flags[flag],
                fit=ft.ImageFit.COVER
            ),
            padding=ft.padding.all(5),
            on_click=lambda _: self.change_language(flag),
            border_radius=4,
            tooltip=tooltips[flag]
        )

    def create_menu_item(self, text, page_name):
        """Crear item de menú"""
        return ft.TextButton(
            text=text,
            on_click=lambda _: self.navigate_to(page_name),
            style=ft.ButtonStyle(
                color='#191970' if self.current_page != page_name else ft.Colors.GREEN_600,
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD if self.current_page == page_name
                    else ft.FontWeight.NORMAL)
            )
        )

    def create_header(self):
        """Crear header responsive"""
        t = textos[self.current_language]

        if self.is_mobile:
            # Header móvil con menú hamburguesa
            self.mobile_drawer = ft.NavigationDrawer(
                controls=[
                    ft.Container(height=12),
                    ft.NavigationDrawerDestination(
                        label=t['menu']['home'],
                        icon=ft.Icons.HOME,
                        selected_icon=ft.Icons.HOME_FILLED,
                    ),
                    ft.NavigationDrawerDestination(
                        label=t['menu']['about'],
                        icon=ft.Icons.INFO,
                        selected_icon=ft.Icons.INFO_OUTLINED,
                    ),
                    ft.NavigationDrawerDestination(
                        label=t['menu']['services'],
                        icon=ft.Icons.WORK,
                        selected_icon=ft.Icons.WORK_OUTLINE,
                    ),
                    ft.NavigationDrawerDestination(
                        label=t['menu']['blog'],
                        icon=ft.Icons.ARTICLE,
                        selected_icon=ft.Icons.ARTICLE_OUTLINED,
                    ),
                    ft.NavigationDrawerDestination(
                        label=t['menu']['contact'],
                        icon=ft.Icons.ARTICLE,
                        selected_icon=ft.Icons.CONTACT_MAIL_OUTLINED,
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=ft.Row([
                            ft.Text(t['language'], size=14,
                                    weight=ft.FontWeight.BOLD),
                            self.create_flag_button('Español', 'es'),
                            self.create_flag_button('English', 'en'),
                            self.create_flag_button('Português', 'pt'),
                        ]),
                        padding=ft.padding.all(16)
                    )
                ],
                on_change=self.handle_drawer_change
            )

            self.page.drawer = self.mobile_drawer

            return ft.Container(
                content=ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.MENU,
                        on_click=lambda _: setattr(
                            self.page.drawer, 'open', True) or self.page.update()
                    ),
                    self.create_logo(30)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                bgcolor=ft.Colors.WHITE,
                padding=ft.padding.symmetric(horizontal=16, vertical=8),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=5,
                    color=ft.Colors.BLACK12
                )
            )
        else:
            # Header desktop
            return ft.Container(
                content=ft.Row([
                    # Logo
                    self.create_logo(),

                    # Menú Central
                    ft.Row([
                        self.create_menu_item(t['menu']['home'], 'home'),
                        self.create_menu_item(t['menu']['about'], 'about'),
                        self.create_menu_item(
                            t['menu']['services'], 'services'),
                        self.create_menu_item(t['menu']['blog'], 'blog'),
                        self.create_menu_item(t['menu']['contact'], 'contact'),
                    ], spacing=20),

                    # Banderas
                    ft.Row([
                        self.create_flag_button('Español', 'es'),
                        self.create_flag_button('English', 'en'),
                        self.create_flag_button('Português', 'pt'),
                    ], spacing=5)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                bgcolor=ft.Colors.WHITE,
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=5,
                    color=ft.Colors.BLACK12
                )
            )

    def handle_drawer_change(self, e):
        """Manejar cambios en el drawer de navegación"""
        page_map = {0: 'home', 1: 'about',
                    2: 'services', 3: 'blog', 4: 'contact'}
        if e.control.selected_index is not None:
            self.navigate_to(page_map[e.control.selected_index])

    def create_home_page(self):
        """Crear página de inicio"""
        t = textos[self.current_language]['pages']['home']
        image_h = ft.Image(
            src="portada_h.png",
            width=self.page.width,
            height=800,
            fit=ft.ImageFit.COVER
        )
        image_v = ft.Image(
            src="portada_v.png",
            width=self.page.width,
            fit=ft.ImageFit.COVER
        )

        return ft.Container(
            content=ft.Column([
                # Imagen principal con texto superpuesto
                ft.Container(
                    content=ft.Stack([
                        # Imagen de fondo
                        image_h if not self.is_mobile else image_v,
                        # Texto superpuesto
                        ft.Container(
                            content=ft.Column([
                                ft.Text(
                                    t['title'],
                                    size=32 if not self.is_mobile else 24,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                    color='#90EE90'
                                ),
                                ft.Text(
                                    t['subtitle'],
                                    size=18 if not self.is_mobile else 16,
                                    text_align=ft.TextAlign.CENTER,
                                    color=ft.Colors.WHITE,
                                )
                            ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10),
                            padding=ft.padding.all(
                                40) if not self.is_mobile else ft.padding.only(left=20, top=130, right=20),  # pylint: disable=line-too-long
                            alignment=ft.alignment.center if not self.is_mobile else ft.alignment.top_left,  # pylint: disable=line-too-long
                            expand=True
                        )
                    ]),
                    height=800 if not self.is_mobile else '100%',
                    border_radius=10,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    margin=ft.margin.all(10)
                )
            ]),
            padding=ft.padding.all(10)
        )

    def create_about_page(self):
        """Crear página Quiénes Somos"""
        t = textos[self.current_language]['pages']['about']

        return ft.Container(
            content=ft.Column([
                ft.Text(
                    t['title'],
                    size=28 if not self.is_mobile else 18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color='#90EE90'
                ),
                ft.Row([
                    # Imagen
                    ft.Container(
                        content=ft.Image(
                            src="Quienes-Somos.jpg",
                            border_radius=10
                        ),
                        border_radius=10,
                        padding=ft.padding.all(20),
                        expand=1 if not self.is_mobile else None,
                        width=100 if not self.is_mobile else '100%',
                    ),

                    # Texto
                    ft.Container(
                        content=ft.Text(
                            t['content'],
                            size=16 if not self.is_mobile else 12,
                            text_align=ft.TextAlign.JUSTIFY,
                            color=ft.Colors.WHITE
                        ),
                        padding=ft.padding.all(20),
                        expand=2 if not self.is_mobile else None
                    )
                ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=20,
                    wrap=self.is_mobile
                )
            ], spacing=30 if not self.is_mobile else 10),
            padding=ft.padding.all(20)
        )

    def create_services_page(self):
        """Crear página de servicios"""
        t = textos[self.current_language]['pages']['services']

        services_grid = []
        icons = [ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, ft.Icons.TRANSFER_WITHIN_A_STATION,
                 ft.Icons.CONTENT_PASTE_SEARCH, ft.Icons.ANALYTICS,
                 ft.Icons.SETTINGS_APPLICATIONS, ft.Icons.WEB]

        for i, service in enumerate(t['items']):
            service_card = ft.Container(
                content=ft.Column([
                    ft.Icon(
                        icons[i] if i < len(icons) else ft.Icons.STAR,
                        size=60,
                        color='#191970'
                    ),
                    ft.Text(
                        service['name'],
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color='#191970'
                    ),
                    ft.Text(
                        service['description'],
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.GREY_700
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                bgcolor=ft.Colors.WHITE,
                padding=ft.padding.all(20),
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=5,
                    color=ft.Colors.BLACK12
                ),
                expand=1,
                on_click=lambda e, idx=i: self.navigate_to(f'service_{idx}'),
                ink=True
            )
            services_grid.append(service_card)

        # Organizar servicios en filas
        if self.is_mobile:
            services_layout = ft.Column([
                ft.Column(services_grid, spacing=20)
            ])
        else:
            services_layout = ft.Column([
                ft.Row(services_grid[:2], spacing=20),
                ft.Row(services_grid[2:], spacing=20)
            ], spacing=20)

        return ft.Container(
            content=ft.Column([
                ft.Text(
                    t['title'],
                    size=28 if not self.is_mobile else 24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color='#90EE90'
                ),
                services_layout
            ], spacing=30),
            padding=ft.padding.all(20)
        )

    def create_blog_page(self):
        """Crear página del blog"""
        t = textos[self.current_language]['pages']['blog']

        return ft.Container(
            content=ft.Column([
                ft.Text(
                    t['title'],
                    size=28 if not self.is_mobile else 24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color='#90EE90'
                ),

                ft.Container(
                    content=ft.Column([
                        # Imagen del blog
                        ft.Container(
                            content=ft.Icon(
                                ft.Icons.ARTICLE,
                                size=100,
                                color='#191970'
                            ),
                            bgcolor=ft.Colors.GREY_100,
                            border_radius=10,
                            padding=ft.padding.all(20),
                            alignment=ft.alignment.center
                        ),

                        ft.Text(
                            t['description'],
                            size=16,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.BLACK87
                        ),

                        ft.ElevatedButton(
                            text=t['link_text'],
                            on_click=lambda _: self.page.launch_url(
                                'https://rponce66.blogspot.com/'),
                            style=ft.ButtonStyle(
                                bgcolor='#191970',
                                color=ft.Colors.WHITE
                            )
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(30),
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=5,
                        color=ft.Colors.BLACK12
                    )
                )
            ], spacing=30),
            padding=ft.padding.all(20)
        )

    def send_email(self, name, email, company, country, service, message):
        """Enviar email de contacto con SendGrid"""
        try:
            sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
            content = f"""
            Nueva solicitud de servicio recibida:

            Nombre: {name}
            Email: {email}
            Empresa: {company}
            País: {country}
            Servicio solicitado: {service}

            Mensaje:
            {message}

            ---
            Este correo fue enviado desde el formulario de contacto de rponce66 - Soft & Finances
            """

            mail = Mail(
                from_email=os.environ["EMAIL_SENDER"],
                to_emails=os.environ["EMAIL_RECEIVER"],
                subject=f"Solicitud de Servicio: {service}",
                plain_text_content=content
            )
            sg.send(mail)
            return True
        except (KeyError, OSError) as e:
            print(f"Error al enviar email: {e}")
            return False

    def create_contact_page(self):
        """Crear página de contacto"""
        t = textos[self.current_language]['pages']['contact']

        # Campos del formulario
        name_field = ft.TextField(
            label=t['form']['name'],
            border_radius=8,
            filled=True
        )

        email_field = ft.TextField(
            label=t['form']['email'],
            border_radius=8,
            filled=True
        )

        company_field = ft.TextField(
            label=t['form']['company'],
            border_radius=8,
            filled=True
        )
        country_field = ft.Dropdown(
            label=t['form']['country'],
            options=[
                ft.dropdown.Option(country)
                for country in textos[self.current_language]['pages']['countries']
            ],
            border_radius=8,
            filled=True
        )

        service_field = ft.Dropdown(
            label=t['form']['service'],
            options=[
                ft.dropdown.Option(service['name'])
                for service in textos[self.current_language]['pages']['services']['items']
            ],
            border_radius=8,
            filled=True
        )

        message_field = ft.TextField(
            label=t['form']['message'],
            multiline=True,
            min_lines=4,
            max_lines=6,
            border_radius=8,
            filled=True
        )

        def handle_submit(e):  # pylint: disable=unused-argument
            if name_field.value and email_field.value and company_field.value and country_field.value and message_field.value:  # pylint: disable=line-too-long
                success = self.send_email(
                    name_field.value, email_field.value, company_field.value, country_field.value, service_field.value, message_field.value)  # pylint: disable=line-too-long
                if success:
                    # Limpiar formulario
                    name_field.value = ""
                    email_field.value = ""
                    company_field.value = ""
                    country_field.value = None
                    service_field.value = None
                    message_field.value = ""

                    # Mostrar mensaje de éxito
                    self.page.open(ft.SnackBar(ft.Text(t['form']['success']),
                                               bgcolor=ft.Colors.GREEN_500))
                    self.page.update()
            else:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Text(t['form']['error']),
                    bgcolor=ft.Colors.RED_500
                )

        return ft.Container(
            content=ft.Column([
                ft.Text(
                    t['title'],
                    size=28 if not self.is_mobile else 24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color='#90EE90'
                ),

                ft.Container(
                    content=ft.Column([
                        name_field,
                        email_field,
                        company_field,
                        country_field,
                        service_field,
                        message_field,
                        ft.ElevatedButton(
                            text=t['form']['submit'],
                            on_click=handle_submit,
                            style=ft.ButtonStyle(
                                bgcolor='#191970',
                                color=ft.Colors.WHITE
                            )
                        )
                    ], spacing=20),
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(30),
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=5,
                        color=ft.Colors.BLACK12
                    ),
                    width=600 if not self.is_mobile else None
                )
            ], spacing=30, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.padding.all(20),
            alignment=ft.alignment.center
        )

    def create_service_detail_page(self, lang, service_index):
        """Crear página de detalle de servicio individual"""
        t = textos[self.current_language]['pages']['services']
        service = t['items'][service_index]
        icons = [ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, ft.Icons.TRANSFER_WITHIN_A_STATION,
                 ft.Icons.CONTENT_PASTE_SEARCH, ft.Icons.ANALYTICS,
                 ft.Icons.SETTINGS_APPLICATIONS, ft.Icons.WEB]

        service_images = ['servicio_0.jpg', 'servicio_1.jpg', 'servicio_2.jpg',
                          'servicio_3.jpg', 'servicio_4.jpg', 'servicio_5.jpg']

        back_services = {
            'es': 'Volver a Servicios',
            'en': 'Back to Services',
            'pt': 'Voltar aos Serviços'
        }
        # Contenido de texto del lado derecho
        text_content = ft.Column([
            # Icono del servicio
            ft.Icon(
                icons[service_index],
                size=60,
                color='#191970'
            ),

            # Descripción corta
            ft.Text(
                service['description'],
                size=16,
                text_align=ft.TextAlign.JUSTIFY if not self.is_mobile else ft.TextAlign.CENTER,
                color='#191970',
                weight=ft.FontWeight.W_500
            ),

            ft.Divider(height=20),

            # Descripción detallada
            ft.Text(
                service['detail'],
                size=15,
                text_align=ft.TextAlign.JUSTIFY,
                color=ft.Colors.BLACK87
            ),

            # Características
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        service['features_title'],
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color='#191970'
                    ),
                    *[
                        ft.Row([
                            ft.Icon(ft.Icons.CHECK_CIRCLE,
                                    color=ft.Colors.GREEN_500, size=20),
                            ft.Text(feature, size=14, expand=True,
                                    color=ft.Colors.BLACK87)
                        ], spacing=10)
                        for feature in service['features']
                    ]
                ], spacing=10),
                margin=ft.margin.only(top=20)
            ),

            # Botón de contacto
            ft.Container(
                content=ft.ElevatedButton(
                    text=service['cta_button'],
                    on_click=lambda _: self.navigate_to('contact'),
                    style=ft.ButtonStyle(
                        bgcolor='#191970',
                        color=ft.Colors.WHITE,
                        padding=ft.padding.symmetric(
                            horizontal=40, vertical=15)
                    ),
                    icon=ft.Icons.CONTACT_MAIL
                ),
                alignment=ft.alignment.center_left if not self.is_mobile else ft.alignment.center,
                margin=ft.margin.only(top=20)
            )
        ], spacing=15, expand=True)

        # Layout responsive
        if self.is_mobile:
            # En móvil: imagen arriba, texto abajo
            main_content = ft.Column([
                ft.Container(
                    content=ft.Image(
                        src=service_images[service_index],
                        height=400,
                        fit=ft.ImageFit.COVER,
                        border_radius=10
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20)
                ),
                text_content
            ], spacing=20)
        else:
            # En desktop: imagen izquierda, texto derecha
            main_content = ft.Row([
                # Imagen a la izquierda
                ft.Container(
                    content=ft.Image(
                        src=service_images[service_index],
                        width=350,
                        height=600,
                        fit=ft.ImageFit.COVER,
                        border_radius=10
                    ),
                    alignment=ft.alignment.top_left
                ),
                # Texto a la derecha
                text_content
            ], spacing=30, vertical_alignment=ft.CrossAxisAlignment.START)

        return ft.Container(
            content=ft.Column([
                # Botón de regreso
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color='#90EE90',
                            on_click=lambda _: self.navigate_to('services'),
                            tooltip=back_services[lang]
                        ),
                        ft.Text(
                            back_services[lang],
                            size=14,
                            color=ft.Colors.WHITE
                        )
                    ], spacing=5),
                    margin=ft.margin.only(bottom=20)
                ),

                # Título del servicio
                ft.Text(
                    service['name'],
                    size=32 if not self.is_mobile else 24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.LEFT if not self.is_mobile else ft.TextAlign.CENTER,
                    color='#90EE90'
                ),

                # Contenido principal
                ft.Container(
                    content=main_content,
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(30 if not self.is_mobile else 20),
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=5,
                        color=ft.Colors.BLACK12
                    )
                )
            ], spacing=20),
            padding=ft.padding.all(20)
        )

    def create_body(self):
        """Crear contenido del body según la página actual"""
        pages = {
            'home': self.create_home_page,
            'about': self.create_about_page,
            'services': self.create_services_page,
            'blog': self.create_blog_page,
            'contact': self.create_contact_page,
            'service_0': lambda: self.create_service_detail_page(lang=self.current_language, service_index=0),  # pylint: disable=line-too-long
            'service_1': lambda: self.create_service_detail_page(lang=self.current_language, service_index=1),  # pylint: disable=line-too-long
            'service_2': lambda: self.create_service_detail_page(lang=self.current_language, service_index=2),  # pylint: disable=line-too-long
            'service_3': lambda: self.create_service_detail_page(lang=self.current_language, service_index=3),  # pylint: disable=line-too-long
            'service_4': lambda: self.create_service_detail_page(lang=self.current_language, service_index=4),  # pylint: disable=line-too-long
            'service_5': lambda: self.create_service_detail_page(lang=self.current_language, service_index=5)  # pylint: disable=line-too-long
        }

        return ft.Container(
            content=ft.Column(
                [pages[self.current_page]()],
                scroll=ft.ScrollMode.AUTO
            ),
            expand=True,
            bgcolor=ft.Colors.BLUE_GREY_900
        )

    def create_social_button(self, platform, url, image):
        """Crear botón de red social"""
        return ft.Container(
            content=ft.Image(
                src=image,
                width=25,
                height=25,
                fit=ft.ImageFit.CONTAIN
            ),
            on_click=lambda _: self.page.launch_url(url),
            tooltip=platform,
            padding=ft.padding.all(5)
        )

    def create_footer(self):
        """Crear footer"""
        t = textos[self.current_language]['footer']

        social_buttons = ft.Row([
            self.create_social_button(
                "YouTube", "https://www.youtube.com/@SIFexsoft", "youtube.svg"),
            self.create_social_button(
                "Facebook", "https://www.facebook.com/sifex.soft", "facebook.svg"),
            self.create_social_button(
                "Instagram", "https://www.instagram.com/rponce66/?hl=es", "instagram.svg"),
            self.create_social_button(
                "LinkedIn", "https://www.linkedin.com/in/econ-richard-ponce/", "linkedin.svg"),
            self.create_social_button("X", "https://x.com/rponce66", "x.svg"),
        ], spacing=5)

        if self.is_mobile:
            return ft.Container(
                content=ft.Column([
                    ft.Row([
                        self.create_logo(40)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        social_buttons
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.Text(t['copyright'], size=12, color=ft.Colors.GREY_700,
                                text_align=ft.TextAlign.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
                bgcolor=ft.Colors.GREY_900,
                padding=ft.padding.all(20)
            )
        else:
            return ft.Container(
                content=ft.Row([
                    self.create_logo(50),
                    ft.Text(t['copyright'], size=12, color=ft.Colors.GREY_700),
                    social_buttons
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                bgcolor=ft.Colors.GREY_900,
                padding=ft.padding.symmetric(horizontal=20, vertical=15)
            )

    def setup_page(self):
        """Configurar la página completa"""
        self.is_mobile = self.page.width < 768

        # Crear componentes
        header = self.create_header()
        body = self.create_body()
        footer = self.create_footer()

        # Agregar a la página
        self.page.controls = [
            ft.Column([
                header,
                body,
                footer
            ], spacing=0, expand=True)
        ]

        self.page.update()


def main(page: ft.Page):
    """Función main"""
    WebApp(page)


if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets', view=ft.WEB_BROWSER)
