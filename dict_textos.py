"""rponce66-web"""

textos = {
    'es': {
        'language': 'Idioma',
        'menu': {
            'home': 'Inicio',
            'about': 'Quiénes Somos',
            'services': 'Servicios',
            'blog': 'Blog',
            'contact': 'Contacto'
        },
        'pages': {
            'home': {
                'title': 'Bienvenidos',
                'subtitle': 'Soluciones innovadoras para su empresa'
            },
            'about': {
                'title': 'Quiénes Somos',
                'content': """
                Somos un grupo especializado en consultoría contable, financiera y de auditoría, liderada por Richard Ponce, Economista y Especialista en Finanzas con más de 30 años de experiencia. Nuestro enfoque combina excelencia técnica, cumplimiento normativo y soluciones innovadoras adaptadas a las necesidades de cada cliente.
                Nuestro equipo de profesionales asociados posee una sólida trayectoria en contabilidad, auditoría y finanzas corporativas, lo que nos permite ofrecer un servicio integral, confiable y de alta calidad.
                Desarrollamos herramientas automatizadas en Excel (VBA) y software especializado en Python. También integramos análisis de datos con Power BI y Looker Studio para fortalecer la toma de decisiones.
                Nuestro compromiso es brindar soluciones efectivas, escalables y alineadas con los estándares internacionales, contribuyendo al crecimiento sostenible de su organización.
                """  # pylint: disable=line-too-long
            },
            'services': {
                'title': 'Nuestros Servicios',
                'items': [
                    {
                        'name': 'Asesoría Contable',
                        'description': '''Orientación permanente en lo referente al registro de las transacciones de su empresa.''',  # pylint: disable=line-too-long
                        'detail': '''Orientación permanente en lo referente al registro de las transacciones de su empresa. En tal sentido, el servicio de asesoría contable asegura el correcto registro y actualización en la contabilidad, mediante el examen de cuentas específicas, y el análisis y control de cuentas con riesgo considerable.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principales:',
                        'features': [
                            'Examen de cuentas específicas.',
                            'Análisis y control de cuentas con riesgo considerable.',
                            'Preparación y revisión limitada de Estados Financieros.',
                            'Elaboración de Estados Financieros Ajustados por Inflación ambos bajo Normas Internacionales de Información Financiera (NIIF).',  # pylint: disable=line-too-long
                            'Planificación y tomas de inventarios físicos, Otros.',
                            'Aplicación de las Normas Internacionales de Información Financiera y las Normas Internacionales de Información Financiera para pequeñas y medianas entidades, tanto en su adopción como en normas específicas.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar Servicio"
                    },
                    {
                        'name': 'Gestión Financiera',
                        'description': '''Servicio de tercerización en la ejecución de distintas tareas de las áreas de administración, contabilidad y finanzas.''',  # pylint: disable=line-too-long
                        'detail': '''Subcontratación de determinadas funciones, tareas o procesos de su empresa con el objetivo de permitir que se enfoque en su actividad principal, que puede resultar en una reducción de costos, mejora de la calidad, acceso a experiencia y agilidad.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principales:',
                        'features': [
                            'Contable: subcontratación de la gestión del sistema contable, el cual está conformado por los métodos y registros establecidos para identificar, reunir, analizar, clasificar, registrar y producir información cuantitativa de las operaciones que realiza su empresa.',  # pylint: disable=line-too-long
                            'Fiscal: subcontratación de Sistema de Control Fiscal, conformado por el registro, control, emisión de reportes de todas las obligaciones fiscales de su empresa, tanto nacionales como municipales. Con apego estricto al marco legal vigente en materia fiscal, ofrecemos orientación con el objeto de traducir en acciones prácticas las normas vigentes, con miras a cubrir la empresa de riesgos y demás contingencias fiscales.',  # pylint: disable=line-too-long
                            'Auditoría Interna: subcontratación de aquellas actividades de evaluación independiente establecidas dentro de una empresa para examinar y evaluar sus actividades. Su objetivo es ayudar a los miembros de una organización en el cumplimiento efectivo de sus responsabilidades al proporcionar análisis, evaluaciones, recomendaciones y asesoría.',  # pylint: disable=line-too-long
                            'Planificación Financiera: subcontratación de Sistema de Planificación Financiera, conformado por el plan de acción dirigido a cumplir una meta prevista, expresada en valores y términos financieros que, debe cumplirse en determinado tiempo y bajo ciertas condiciones previstas, este concepto se aplica a cada centro de responsabilidad de la organización.',  # pylint: disable=line-too-long
                            'Crédito: subcontratación que tiene como objetivo primordial, evaluar la situación financiera de los clientes de su empresa en un momento determinado, de acuerdo con la interpretación de sus estados financieros y con la elaboración y comparación de unos índices financieros, que permitan informar sobre su rentabilidad, liquidez y solvencia financiera, determinando así, si son susceptibles de otorgarles el crédito comercial y/o establecer el límite de este; minimizando con ello el riesgo de morosidad en la cartera de cuentas por cobrar.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar Servicio"
                    },
                    {
                        'name': 'Auditoría Externa',
                        'description': '''Servicio que verifica el cumplimiento y la precisión de los estados financieros.''',  # pylint: disable=line-too-long
                        'detail': '''Proceso de evaluación independiente, para verificar la exactitud y cumplimiento de los estados financieros y otros procesos normativos. Su objetivo principal es dar credibilidad y transparencia a la empresa, proporcionando una opinión experta sobre su situación financiera, la cual es utilizada por inversionistas, clientes y otras partes interesadas.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principales:',
                        'features': [
                            'Auditoría Financiera: planeación, ejecución y control de una serie de actividades que conducen a la expresión de muestra opinión acerca de la veracidad de los estados financieros, si están formulados de acuerdo con principios de contabilidad generalmente aceptados y de consistencia en la aplicación de dichos principios en períodos sucesivos. Para ello contamos con los mejores profesionales formados en grandes firmas transnacionales.',  # pylint: disable=line-too-long
                            'Auditoría Fiscal: evaluación y análisis de obligaciones fiscales, a las cuales está sometida la empresa, con el objeto de determinar si la misma se encuentra bajo los parámetros establecidos en las leyes y reglamentos inherentes.',  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar Servicio"
                    },
                    {
                        'name': 'Análisis de Datos',
                        'description': '''Servicio de conversión de datos sin procesar en valor de negocio.''',  # pylint: disable=line-too-long
                        'detail': '''Proceso de examinar conjuntos de datos complejos para descubrir patrones, interpretar información y tomar decisiones estratégicas. Utiliza una variedad de técnicas, incluyendo estadísticas y aprendizaje automático, para convertir datos brutos en conocimientos prácticos que pueden mejorar la toma de decisiones, optimizar operaciones y predecir tendencias futuras.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principales:',
                        'features': [
                            'Proceso de análisis: implica definir objetivos, recopilar, limpiar, analizar e interpretar datos para finalmente visualizar y comunicar los hallazgos. ',  # pylint: disable=line-too-long
                            'Uso de técnicas: emplea métodos como la estadística, el aprendizaje automático (machine learning) y el procesamiento de lenguaje natural (PNL) para extraer patrones y realizar predicciones.',  # pylint: disable=line-too-long
                            'Objetivo final: busca obtener información significativa que permita a las organizaciones tomar decisiones informadas en lugar de basarse en suposiciones, optimizando así sus procesos y mejorando los resultados.',  # pylint: disable=line-too-long
                            'Aplicaciones: se aplica en diversas áreas para entender el comportamiento del cliente, predecir fallos técnicos, optimizar la logística y mejorar la experiencia del usuario.',  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar Servicio"
                    },
                    {
                        'name': 'Desarrollo de Software',
                        'description': '''Creación, diseño, implementación y soporte de software.''',  # pylint: disable=line-too-long
                        'detail': '''Subcontratación de determinadas funciones, tareas o procesos de su empresa con el objetivo de permitir que se enfoque en su actividad principal, que puede resultar en una reducción de costos, mejora de la calidad, acceso a experiencia y agilidad.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principales:',
                        'features': [
                            'Proceso cíclico y sistemático: El desarrollo de software sigue un ciclo de vida (SDLC, por sus siglas en inglés) que va desde la concepción hasta el mantenimiento, pasando por la planificación, análisis de requisitos, diseño, desarrollo, pruebas, implementación y mantenimiento.',  # pylint: disable=line-too-long
                            'Diseño y planificación: Incluye la definición de la arquitectura, la experiencia del usuario (UX) y la planificación de la producción para cumplir con objetivos específicos.',  # pylint: disable=line-too-long
                            'Programación (Codificación): Es la fase donde se escribe el código fuente en un lenguaje de programación para crear las instrucciones que la computadora debe seguir.',  # pylint: disable=line-too-long
                            'Pruebas (Testing): Consiste en verificar que el software funciona correctamente, está libre de errores (bugs) y cumple con los requisitos especificados antes de su lanzamiento.',  # pylint: disable=line-too-long
                            'Mantenimiento y actualizaciones: Una vez lanzado, el software requiere actualizaciones, correcciones de errores y mejoras continuas para seguir siendo relevante y seguro.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar Servicio"
                    },
                    {
                        'name': 'Desarrollo Web',
                        'description': '''Creación de sitios web modernos, responsivos y optimizados para todos los dispositivos.''',  # pylint: disable=line-too-long
                        'detail': '''En el entorno digital actual, tu sitio web es la primera impresión que los clientes tienen de tu negocio. Ofrecemos un servicio integral de desarrollo de sitios web que garantiza una experiencia de usuario excepcional, diseño responsive y rendimiento optimizado. Nuestro equipo se especializa en crear soluciones a medida, adaptadas a las necesidades específicas de tu empresa, ya sea una página web corporativa, una tienda en línea o un portal interactivo. Nos aseguramos de que tu sitio web no solo sea visualmente atractivo, sino también funcional y fácil de navegar, con tiempos de carga rápidos y una estructura SEO-friendly que favorezca tu posicionamiento en buscadores.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principales:',
                        'features': [
                            'Frontend: desarrollo de la interfaz de usuario, la parte visual e interactiva que el usuario ve en el navegador. Se utiliza para dar estilo y crear interactividad.',  # pylint: disable=line-too-long
                            'Backend: desarrollo de la lógica del servidor, las bases de datos y la comunicación entre el servidor y el frontend.',  # pylint: disable=line-too-long
                            'Creación y mantenimiento: el desarrollo web no solo implica la creación inicial de un sitio, sino también su mantenimiento continuo, como la actualización de contenido, la corrección de errores y la mejora del rendimiento y la seguridad.',  # pylint: disable=line-too-long
                            'Enfoque en la experiencia del usuario: un buen desarrollo web prioriza la creación de experiencias de usuario agradables, intuitivas y eficientes, asegurando que el sitio sea accesible, cómodo y funcional.',  # pylint: disable=line-too-long
                            'Adaptabilidad y constante evolución: es un campo que evoluciona rápidamente, por lo que los desarrolladores deben estar en constante aprendizaje de nuevas tecnologías, herramientas y tendencias para adaptarse y crear soluciones efectivas.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar Servicio"
                    }
                ]
            },
            'blog': {
                'title': 'Nuestro Blog',
                'description': '''Mantente al día con las últimas tendencias tecnológicas, consejos
                y novedades de nuestra industria. Nuestro blog está lleno de contenido valioso para
                ayudarte a tomar las mejores decisiones para tu negocio.''',
                'link_text': 'Visitar Blog'
            },
            'contact': {
                'title': 'Solicitud de Servicios',
                'form': {
                    'name': 'Nombre completo',
                    'email': 'Correo electrónico',
                    'company': 'Nombre de la empresa',
                    'country': 'País',
                    'service': 'Servicio de interés',
                    'message': 'Mensaje detallado',
                    'submit': 'Enviar Solicitud',
                    'success': 'Solicitud enviada exitosamente. Te contactaremos pronto.',
                    'error': 'Por favor, completa todos los campos obligatorios.'
                }
            },
            'countries': [
                'Albania',
                'Alemania',
                'Arabia Saudita',
                'Argentina',
                'Australia',
                'Austria',
                'Bangladesh',
                'Barbados',
                'Bélgica',
                'Belice',
                'Bolivia',
                'Brasil',
                'Bulgaria',
                'Camboya',
                'Canadá',
                'Chile',
                'China',
                'Chipre',
                'Colombia',
                'Corea del Sur',
                'Costa Rica',
                'Croacia',
                'Cuba',
                'Dinamarca',
                'Ecuador',
                'Egipto',
                'El Salvador',
                'Emiratos Árabes Unidos',
                'Eslovaquia',
                'Eslovenia',
                'España',
                'Estados Unidos de América',
                'Estonia',
                'Filipinas',
                'Finlandia',
                'Francia',
                'Grecia',
                'Guatemala',
                'Guyana',
                'Haití',
                'Honduras',
                'Hong Kong',
                'Hungría',
                'India',
                'Indonesia',
                'Irlanda',
                'Islandia',
                'Israel',
                'Italia',
                'Jamaica',
                'Japón',
                'Letonia',
                'Líbano',
                'Lituania',
                'Luxemburgo',
                'Madagascar',
                'Malasia',
                'Malta',
                'Marruecos',
                'México',
                'Moldavia',
                'Myanmar',
                'Nicaragua',
                'Noruega',
                'Nueva Zelanda',
                'Países Bajos',
                'Pakistán',
                'Paraguay',
                'Perú',
                'Polonia',
                'Portugal',
                'Puerto Rico',
                'Qatar',
                'Reino Unido',
                'República Checa',
                'República de Belarús',
                'República Dominicana',
                'Rumania',
                'Rusia',
                'Senegal',
                'Serbia',
                'Singapur',
                'Sri Lanka',
                'Sudáfrica, República de',
                'Suecia',
                'Suiza',
                'Suriname',
                'Tailandia',
                'Taiwán',
                'Trinidad y Tobago',
                'Túnez',
                'Turquía',
                'Ucrania',
                'Uruguay',
                'Venezuela',
                'Vietnam'
            ]
        },
        'page_tittle': {
            'home': 'rponce66 - Soft & Finances',
            'about': 'Quiénes Somos - rponce66',
            'services': 'Servicios - rponce66',
            'blog': 'Blog - rponce66',
            'contact': 'Contacto - rponce66',
            'service_0': 'Asesoría Contable - rponce66',
            'service_1': 'Gestión Financiera - rponce66',
            'service_2': 'Auditoría Externa - rponce66',
            'service_3': 'Análisis de Datos - rponce66',
            'service_4': 'Desarrollo de Software - rponce66',
            'service_5': 'Desarrollo Web - rponce66'
        },
        'footer': {
            'copyright': '© 2025 rponce66. Todos los derechos reservados.'
        }
    },
    'en': {
        'language': 'Language',
        'menu': {
            'home': 'Home',
            'about': 'About Us',
            'services': 'Services',
            'blog': 'Blog',
            'contact': 'Contact'
        },
        'pages': {
            'home': {
                'title': 'Welcome',
                'subtitle': 'Innovative solutions for your business'
            },
            'about': {
                'title': 'About Us',
                'content': """
                    We are a group specializing in accounting, financial, and audit consulting, led by Richard Ponce, an economist and finance specialist with over 30 years of experience. Our approach combines technical excellence, regulatory compliance, and innovative solutions tailored to each client's needs.
                    Our team of professional associates has a solid track record in accounting, auditing, and corporate finance, enabling us to offer comprehensive, reliable, and high-quality service.
                    We develop automated tools in Excel (VBA) and specialized software in Python. We also integrate data analysis with Power BI and Looker Studio to strengthen decision-making.
                    Our commitment is to provide effective, scalable solutions aligned with international standards, contributing to the sustainable growth of your organization.

                    """  # pylint: disable=line-too-long
            },
            'services': {
                'title': 'Our Services',
                'items': [
                    {
                        'name': 'Accounting Consulting',
                        'description': '''Ongoing guidance regarding the recording of your company's transactions.''',  # pylint: disable=line-too-long
                        'detail': '''Ongoing guidance regarding the recording of your company's transactions. In this regard, our accounting advisory service ensures accurate and up-to-date accounting records.''',  # pylint: disable=line-too-long
                        'features_title': 'Key features:',
                        'features': [
                            'Examination of specific accounts.',
                            'Analysis and control of accounts with significant risk.',
                            'Preparation and limited review of Financial Statements.',
                            'Preparation of Inflation-Adjusted Financial Statements, both under International Financial Reporting Standards (IFRS).',  # pylint: disable=line-too-long
                            'Planning and conducting physical inventories, among other services.',
                            'Application of International Financial Reporting Standards and International Financial Reporting Standards for Small and Medium-sized Entities, both in terms of adoption and specific standards.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': 'Request Service'
                    },
                    {
                        'name': 'Financial Management',
                        'description': '''Outsourcing service for the execution of various tasks in the areas of administration, accounting and finance.''',  # pylint: disable=line-too-long
                        'detail': '''Outsourcing certain functions, tasks, or processes of your company with the aim of allowing you to focus on your core business, which can result in cost reduction, improved quality, access to expertise, and agility.''',  # pylint: disable=line-too-long
                        'features_title': 'Key features:',
                        'features': [
                            "Accounting: outsourcing the management of the accounting system, which consists of the methods and records established to identify, gather, analyze, classify, record, and produce quantitative information on your company's operations.",  # pylint: disable=line-too-long
                            "Tax: outsourcing the Tax Control System, which includes the registration, control, and issuance of reports for all your company's tax obligations, both national and municipal. In strict adherence to the current legal framework on tax matters, we offer guidance to translate current regulations into practical actions, aiming to protect the company from risks and other tax contingencies.",  # pylint: disable=line-too-long
                            "Internal Audit: outsourcing those independent evaluation activities established within a company to examine and evaluate its operations. Its objective is to assist members of an organization in the effective fulfillment of their responsibilities by providing analysis, evaluations, recommendations, and advice.",  # pylint: disable=line-too-long
                            "Financial Planning: Outsourcing of the Financial Planning System, consisting of the action plan aimed at fulfilling a planned goal, expressed in financial values and terms, which must be fulfilled within a certain time and under certain planned conditions; this concept applies to each responsibility center of the organization.",  # pylint: disable=line-too-long
                            "Credit: Its primary objective is to evaluate the financial situation of your company's clients at a given time, based on the interpretation of their financial statements and the development and comparison of financial ratios. These ratios provide information on their profitability, liquidity, and financial solvency, thus determining whether they are eligible for commercial credit and/or establishing its limit; thereby minimizing the risk of delinquency in the accounts receivable portfolio."  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Request Service"
                    },
                    {
                        'name': 'External Audit',
                        'description': '''Service that verifies the compliance and accuracy of financial statements.''',  # pylint: disable=line-too-long
                        'detail': '''An independent evaluation process to verify the accuracy and compliance of financial statements and other regulatory processes. Its main objective is to lend credibility and transparency to the company by providing an expert opinion on its financial situation, which is used by investors, clients, and other stakeholders.''',  # pylint: disable=line-too-long
                        'features_title': 'Key features:',
                        'features': [
                            'Financial Audit: planning, execution, and control of a series of activities that lead to the expression of our opinion regarding the accuracy of the financial statements, whether they are prepared in accordance with generally accepted accounting principles, and the consistency in the application of these principles in successive periods. For this, we have the best professionals trained at leading multinational firms.',  # pylint: disable=line-too-long
                            "Tax Audit: evaluation and analysis of the company's tax obligations to determine whether it complies with the parameters established in the relevant laws and regulations.",  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Request Service"
                    },
                    {
                        'name': 'Data Analysis',
                        'description': '''Service for converting raw data into business value.''',  # pylint: disable=line-too-long
                        'detail': '''The process of examining complex datasets to discover patterns, interpret information, and make strategic decisions. It uses a variety of techniques, including statistics and machine learning, to transform raw data into actionable insights that can improve decision-making, optimize operations, and predict future trends.''',  # pylint: disable=line-too-long
                        'features_title': 'Key features:',
                        'features': [
                            'Analysis process: This involves defining objectives, collecting, cleaning, analyzing, and interpreting data to ultimately visualize and communicate the findings.',  # pylint: disable=line-too-long
                            'Use of techniques: It employs methods such as statistics, machine learning, and natural language processing (NLP) to extract patterns and make predictions.',  # pylint: disable=line-too-long
                            'Ultimate goal: It seeks to obtain meaningful information that allows organizations to make informed decisions instead of relying on assumptions, thereby optimizing their processes and improving results.',  # pylint: disable=line-too-long
                            'Applications: It is applied in diverse areas to understand customer behavior, predict technical failures, optimize logistics, and improve user experience.',  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Request Service"
                    },
                    {
                        'name': 'Software Development',
                        'description': '''Software creation, design, implementation and support.''',  # pylint: disable=line-too-long
                        'detail': '''We offer comprehensive online and desktop software development solutions designed to meet the specific needs of your business. Our team of expert developers works with cutting-edge technologies to create custom applications that streamline your processes and improve operational efficiency.''',  # pylint: disable=line-too-long
                        'features_title': 'Key features:',
                        'features': [
                            'Cyclical and systematic process: Software development follows a software development life cycle (SDLC) that extends from conception to maintenance, encompassing planning, requirements analysis, design, development, testing, implementation, and maintenance.',  # pylint: disable=line-too-long
                            'Design and planning: This includes defining the architecture, user experience (UX), and production planning to meet specific objectives.',  # pylint: disable=line-too-long
                            'Programming (Coding): This is the phase where source code is written in a programming language to create the instructions the computer must follow.',  # pylint: disable=line-too-long
                            'Testing: This involves verifying that the software functions correctly, is free of bugs, and meets the specified requirements before release.',  # pylint: disable=line-too-long
                            'Maintenance and updates: Once released, the software requires updates, bug fixes, and continuous improvements to remain relevant and secure.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Request Service"
                    },
                    {
                        'name': 'Web Development',
                        'description': '''Creation of modern, responsive websites optimized for all devices.''',  # pylint: disable=line-too-long
                        'detail': '''In today's digital environment, your website is the first impression customers have of your business. We offer a comprehensive website development service that guarantees an exceptional user experience, responsive design, and optimized performance. Our team specializes in creating custom solutions tailored to your company's specific needs, whether it's a corporate website, an online store, or an interactive portal. We ensure your website is not only visually appealing but also functional and easy to navigate, with fast loading times and an SEO-friendly structure that improves your search engine ranking.''',  # pylint: disable=line-too-long
                        'features_title': 'Key features:',
                        'features': [
                            'Frontend: Development of the user interface, the visual and interactive part that the user sees in the browser. It is used to add style and create interactivity.',  # pylint: disable=line-too-long
                            'Backend: Development of the server logic, databases, and communication between the server and the frontend.',  # pylint: disable=line-too-long
                            'Creation and maintenance: Web development involves not only the initial creation of a site but also its ongoing maintenance, such as updating content, fixing bugs, and improving performance and security.',  # pylint: disable=line-too-long
                            'Focus on user experience: Good web development prioritizes creating enjoyable, intuitive, and efficient user experiences, ensuring that the site is accessible, user-friendly, and functional.',  # pylint: disable=line-too-long
                            'Adaptability and constant evolution: This is a rapidly evolving field, so developers must constantly learn about new technologies, tools, and trends to adapt and create effective solutions.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Request Service"
                    }
                ]
            },

            'blog': {
                'title': 'Our Blog',
                'description': '''Stay up to date with the latest technology trends,
                tips and news from our industry. Our blog is full of valuable content to
                help you make the best decisions for your business.''',
                'link_text': 'Visit Blog'
            },
            'contact': {
                'title': 'Service Request',
                'form': {
                    'name': 'Full name',
                    'email': 'Email address',
                    'company': 'Company name',
                    'country': 'Country',
                    'service': 'Service of interest',
                    'message': 'Detailed message',
                    'submit': 'Send Request',
                    'success': 'Request sent successfully. We will contact you soon.',
                    'error': 'Please fill in all required fields.'
                }
            },
            'countries': [
                'Albania',
                'Germany',
                'Saudi Arabia',
                'Argentina',
                'Australia',
                'Austria',
                'Bangladesh',
                'Barbados',
                'Belgium',
                'Belize',
                'Bolivia',
                'Brazil',
                'Bulgaria',
                'Cambodia',
                'Canada',
                'Chile',
                'China',
                'Cyprus',
                'Colombia',
                'South Korea',
                'Costa Rica',
                'Croatia',
                'Cuba',
                'Denmark',
                'Ecuador',
                'Egypt',
                'El Salvador',
                'United Arab Emirates',
                'Slovakia',
                'Slovenia',
                'Spain',
                'United States of America',
                'Estonia',
                'Philippines',
                'Finland',
                'France',
                'Greece',
                'Guatemala',
                'Guyana',
                'Haiti',
                'Honduras',
                'Hong Kong Kong',
                'Hungary',
                'India',
                'Indonesia',
                'Ireland',
                'Iceland',
                'Israel',
                'Italy',
                'Jamaica',
                'Japan',
                'Latvia',
                'Lebanon',
                'Lithuania',
                'Luxembourg',
                'Madagascar',
                'Malaysia',
                'Malta',
                'Morocco',
                'Mexico',
                'Moldova',
                'Myanmar',
                'Nicaragua',
                'Norway',
                'New Zealand',
                'Netherlands',
                'Pakistan',
                'Paraguay',
                'Peru',
                'Poland',
                'Portugal',
                'Puerto Rico',
                'Qatar',
                'United Kingdom',
                'Czech Republic',
                'Belarus',
                'Dominican Republic',
                'Romania',
                'Russia',
                'Senegal',
                'Serbia',
                'Singapore',
                'Sri Lanka',
                'South Africa',
                'Sweden',
                'Switzerland',
                'Suriname',
                'Thailand',
                'Taiwan',
                'Trinidad and Tobago',
                'Tunisia',
                'Turkey',
                'Ukraine',
                'Uruguay',
                'Venezuela',
                'Vietnam',
            ]
        },
        'page_tittle': {
            'home': 'rponce66 - Soft & Finances',
            'about': 'About Us - rponce66',
            'services': 'Services - rponce66',
            'blog': 'Blog - rponce66',
            'contact': 'Contact - rponce66',
            'service_0': 'Accounting Consulting - rponce66',
            'service_1': 'Financial Management - rponce66',
            'service_2': 'External Audit - rponce66',
            'service_3': 'Data Analysis - rponce66',
            'service_4': 'Software Development - rponce66',
            'service_5': 'Web Development - rponce66'
        },
        'footer': {
            'copyright': '© 2025 rponce66. All rights reserved.'
        }
    },
    'pt': {
        'language': 'Idioma',
        'menu': {
            'home': 'Inicio',
            'about': 'Quem Somos',
            'services': 'Serviços',
            'blog': 'Blog',
            'contact': 'Contato'
        },
        'pages': {
            'home': {
                'title': 'Bem-vindos',
                'subtitle': 'SSoluções inovadoras para o seu negócio'
            },
            'about': {
                'title': 'Quem Somos',
                'content': """
                Somos um grupo especializado em consultoria contábil, financeira e de auditoria, liderado por Richard Ponce, economista e especialista em finanças com mais de 30 anos de experiência. Nossa abordagem combina excelência técnica, conformidade regulatória e soluções inovadoras, personalizadas para as necessidades de cada cliente.
                Nossa equipe de profissionais associados possui sólida experiência em contabilidade, auditoria e finanças corporativas, o que nos permite oferecer um serviço completo, confiável e de alta qualidade.
                Desenvolvemos ferramentas automatizadas em Excel (VBA) e softwares especializados em Python. Também integramos a análise de dados com Power BI e Looker Studio para fortalecer a tomada de decisões.
                Nosso compromisso é fornecer soluções eficazes e escaláveis, alinhadas aos padrões internacionais, contribuindo para o crescimento sustentável da sua organização.
                """  # pylint: disable=line-too-long
            },
            'services': {
                'title': 'Nossos Serviços',
                'items': [
                    {
                        'name': 'Consultoria Contábil',
                        'description': '''Orientação contínua sobre o registro das transações da sua empresa.''',  # pylint: disable=line-too-long
                        'detail': '''Assessoria contínua no registro das transações da sua empresa. Nesse sentido, nosso serviço de consultoria contábil garante registros contábeis precisos e atualizados.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principais:',
                        'features': [
                            'Exame de contas específicas.'
                            'Análise e controle de contas com risco significativo.',
                            'Elaboração e revisão limitada das Demonstrações Financeiras.',
                            'Elaboração de Demonstrações Financeiras Ajustadas pela Inflação, de acordo com as Normas Internacionais de Relato Financeiro (IFRS).',  # pylint: disable=line-too-long
                            'Planejamento e realização de inventários físicos, entre outros serviços.',  # pylint: disable=line-too-long
                            'Aplicação das Normas Internacionais de Relato Financeiro e das Normas Internacionais de Relato Financeiro para Pequenas e Médias Empresas, tanto em termos de adoção quanto de normas específicas.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar serviço"
                    },
                    {
                        'name': 'Gestão Financeira',
                        'description': '''Serviço de terceirização para a execução de diversas tarefas nas áreas de administração, contabilidade e finanças.''',  # pylint: disable=line-too-long
                        'detail': '''A terceirização de determinadas funções, tarefas ou processos da sua empresa tem como objetivo permitir que você se concentre no seu negócio principal, o que pode resultar em redução de custos, melhoria da qualidade, acesso a conhecimento especializado e agilidade.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principais:',
                        'features': [
                            'Contable: Contabilidade: a terceirização da gestão do sistema contábil, que consiste nos métodos e registros estabelecidos para identificar, coletar, analisar, classificar, registrar e produzir informações quantitativas sobre as operações da sua empresa.',  # pylint: disable=line-too-long
                            'Impostos: a terceirização do Sistema de Controle Tributário, que inclui o registro, controle e emissão de relatórios para todas as obrigações tributárias da sua empresa, tanto nacionais quanto municipais. Em estrita conformidade com o atual marco legal em matéria tributária, oferecemos orientação para traduzir as regulamentações vigentes em ações práticas, visando proteger a empresa de riscos e outras contingências tributárias.',  # pylint: disable=line-too-long
                            'Auditoria Interna: a terceirização das atividades de avaliação independente realizadas dentro de uma empresa para examinar e avaliar suas operações. Seu objetivo é auxiliar os membros de uma organização no cumprimento eficaz de suas responsabilidades, fornecendo análises, avaliações, recomendações e consultoria.',  # pylint: disable=line-too-long
                            'Planejamento Financeiro: a terceirização do Sistema de Planejamento Financeiro consiste no plano de ação destinado a atingir uma meta planejada, expressa em valores e termos financeiros, que deve ser cumprida dentro de um determinado prazo e sob certas condições planejadas; esse conceito se aplica a cada centro de responsabilidade da organização.',  # pylint: disable=line-too-long
                            'Crédito: a terceirização tem como objetivo principal avaliar a situação financeira dos clientes da sua empresa em um determinado momento, por meio da interpretação de suas demonstrações financeiras e da elaboração e comparação de índices financeiros, que permitem avaliar sua rentabilidade, liquidez e solvência financeira, determinando se eles são elegíveis para crédito comercial e/ou estabelecendo o limite deste; minimizando, assim, o risco de inadimplência na carteira de contas a receber.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar serviço"
                    },
                    {
                        'name': 'Auditoria Externa',
                        'description': '''Serviço que verifica a conformidade e a exatidão das demonstrações financeiras.''',  # pylint: disable=line-too-long
                        'detail': '''Um processo de avaliação independente para verificar a exatidão e a conformidade das demonstrações financeiras e outros processos regulatórios. Seu principal objetivo é conferir credibilidade e transparência à empresa, fornecendo uma opinião especializada sobre sua situação financeira, utilizada por investidores, clientes e demais partes interessadas.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principais:',
                        'features': [
                            'Auditoria Financeira: planejamento, execução e controle de uma série de atividades que levam à emissão de nossa opinião sobre a exatidão das demonstrações financeiras, se elas foram elaboradas de acordo com os princípios contábeis geralmente aceitos e a consistência na aplicação desses princípios em períodos sucessivos. Para isso, contamos com os melhores profissionais, treinados em importantes empresas multinacionais.',  # pylint: disable=line-too-long
                            'Auditoria Fiscal: avaliação e análise das obrigações fiscais da empresa para determinar se ela está em conformidade com os parâmetros estabelecidos nas leis e regulamentos pertinentes.',  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar serviço"
                    },
                    {
                        'name': 'Análise de Dados',
                        'description': '''Serviço para converter dados brutos em valor comercial.''',  # pylint: disable=line-too-long
                        'detail': '''O processo de examinar conjuntos de dados complexos para descobrir padrões, interpretar informações e tomar decisões estratégicas. Utiliza uma variedade de técnicas, incluindo estatística e aprendizado de máquina, para transformar dados brutos em insights acionáveis que podem aprimorar a tomada de decisões, otimizar operações e prever tendências futuras.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principais:',
                        'features': [
                            'Processo de análise: Envolve a definição de objetivos, coleta, limpeza, análise e interpretação de dados para, por fim, visualizar e comunicar as descobertas.',  # pylint: disable=line-too-long
                            'Utilização de técnicas: Emprega métodos como estatística, aprendizado de máquina (machine learning) e processamento de linguagem natural (PLN) para extrair padrões e fazer previsões.',  # pylint: disable=line-too-long
                            'Objetivo final: Busca obter informações relevantes que permitam às organizações tomar decisões embasadas em vez de se basearem em suposições, otimizando assim seus processos e melhorando os resultados.',  # pylint: disable=line-too-long
                            'Aplicações: É aplicado em diversas áreas para compreender o comportamento do cliente, prever falhas técnicas, otimizar a logística e aprimorar a experiência do usuário.',  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar serviço"
                    },
                    {
                        'name': 'Desenvolvimento de Software',
                        'description': '''Criação, design, implementação e suporte de software.''',  # pylint: disable=line-too-long
                        'detail': '''Oferecemos soluções completas de desenvolvimento de software online e para desktop, projetadas para atender às necessidades específicas do seu negócio. Nossa equipe de desenvolvedores especializados trabalha com tecnologias de ponta para criar aplicativos personalizados que otimizam seus processos e melhoram a eficiência operacional.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principais:',
                        'features': [
                            'Processo cíclico e sistemático: O desenvolvimento de software segue um ciclo de vida de desenvolvimento de software (SDLC) que se estende da concepção à manutenção, abrangendo planejamento, análise de requisitos, projeto, desenvolvimento, testes, implementação e manutenção.',  # pylint: disable=line-too-long
                            'Projeto e planejamento: Isso inclui a definição da arquitetura, da experiência do usuário (UX) e do planejamento de produção para atender a objetivos específicos.',  # pylint: disable=line-too-long
                            'Programação (codificação): Esta é a fase em que o código-fonte é escrito em uma linguagem de programação para criar as instruções que o computador deve seguir.',  # pylint: disable=line-too-long
                            'Testes (Testing): Isso envolve verificar se o software funciona corretamente, está livre de erros e atende aos requisitos especificados antes do lançamento.',  # pylint: disable=line-too-long
                            'Manutenção e atualizações: Após o lançamento, o software requer atualizações, correções de erros e melhorias contínuas para permanecer relevante e seguro.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar serviço"
                    },
                    {
                        'name': 'Desenvolvimento Web',
                        'description': '''Criação de sites modernos e responsivos, otimizados para todos os dispositivos.''',  # pylint: disable=line-too-long
                        'detail': '''No ambiente digital atual, seu website é a primeira impressão que os clientes têm da sua empresa. Oferecemos um serviço completo de desenvolvimento web que garante uma experiência de usuário excepcional, design responsivo e desempenho otimizado. Nossa equipe é especializada na criação de soluções personalizadas, sob medida para as necessidades específicas da sua empresa, seja um website corporativo, uma loja virtual ou um portal interativo. Garantimos que seu website seja não apenas visualmente atraente, mas também funcional e fácil de navegar, com tempos de carregamento rápidos e uma estrutura otimizada para SEO, que melhora seu posicionamento nos mecanismos de busca.''',  # pylint: disable=line-too-long
                        'features_title': 'Características principais:',
                        'features': [
                            'Frontend: Desenvolvimento da interface do usuário, a parte visual e interativa que o usuário vê no navegador. É usado para adicionar estilo e criar interatividade.',  # pylint: disable=line-too-long
                            'Backend: Desenvolvimento da lógica do servidor, bancos de dados e comunicação entre o servidor e o frontend.',  # pylint: disable=line-too-long
                            'Criação e manutenção: O desenvolvimento web envolve não apenas a criação inicial de um site, mas também sua manutenção contínua, como atualização de conteúdo, correção de bugs e melhoria de desempenho e segurança.',  # pylint: disable=line-too-long
                            'Foco na experiência do usuário: Um bom desenvolvimento web prioriza a criação de experiências de usuário agradáveis, intuitivas e eficientes, garantindo que o site seja acessível, fácil de usar e funcional.',  # pylint: disable=line-too-long
                            'Adaptabilidade e evolução constante: Este é um campo em rápida evolução, portanto, os desenvolvedores devem aprender constantemente sobre novas tecnologias, ferramentas e tendências para se adaptar e criar soluções eficazes.'  # pylint: disable=line-too-long
                        ],
                        'cta_button': "Solicitar serviço"
                    }
                ]
            },
            'blog': {
                'title': 'Nosso Blog',
                'description': '''Mantenha-se atualizado com as últimas tendências tecnológicas,
                dicas e novidades da nossa indústria. Nosso blog está cheio de conteúdo valioso
                para ajudá-lo a tomar as melhores decisões para o seu negócio.''',
                'link_text': 'Visite o blog'
            },
            'contact': {
                'title': 'Solicitação de Serviços',
                'form': {
                    'name': 'Nome completo',
                    'email': 'Endereço de email',
                    'country': 'País',
                    'service': 'Serviço de interesse',
                    'company': 'Nome da empresa',
                    'message': 'Mensagem detalhada',
                    'submit': 'Enviar Solicitação',
                    'success': 'Solicitação enviada com sucesso. Entraremos em contato em breve.',
                    'error': 'Por favor, preencha todos os campos obrigatórios.'
                }
            },
            'countries': [
                'Albânia',
                'Alemanha',
                'Arábia Saudita',
                'Argentina',
                'Austrália',
                'Áustria',
                'Bangladesh',
                'Barbados',
                'Bélgica',
                'Belize',
                'Bolívia',
                'Brasil',
                'Bulgária',
                'Camboja',
                'Canadá',
                'Chile',
                'China',
                'Chipre',
                'Colômbia',
                'Coreia do Sul',
                'Costa Rica',
                'Croácia',
                'Cuba',
                'Dinamarca',
                'Equador',
                'Egito',
                'El Salvador',
                'Emirados Árabes Unidos',
                'Eslováquia',
                'Eslovênia',
                'Espanha',
                'Estados Unidos da América',
                'Estônia',
                'Filipinas',
                'Finlândia',
                'França',
                'Grécia',
                'Guatemala',
                'Guiana',
                'Haiti',
                'Honduras',
                'Hong Kong Hong Kong',
                'Hungria',
                'Índia',
                'Indonésia',
                'Irlanda',
                'Islândia',
                'Israel',
                'Itália',
                'Jamaica',
                'Japão',
                'Letônia',
                'Líbano',
                'Lituânia',
                'Luxemburgo',
                'Madagascar',
                'Malásia',
                'Malta',
                'Marrocos',
                'México',
                'Moldávia',
                'Mianmar',
                'Nicarágua',
                'Noruega',
                'Nova Zelândia',
                'Países Baixos',
                'Paquistão',
                'Paraguai',
                'Peru',
                'Polônia',
                'Portugal',
                'Porto Rico',
                'Catar',
                'Reino Unido',
                'República Tcheca',
                'Bielorrússia',
                'República Dominicana',
                'Romênia',
                'Rússia',
                'Senegal',
                'Sérvia',
                'Singapura',
                'Sri Lanka',
                'África do Sul',
                'Suécia',
                'Suíça',
                'Suriname',
                'Tailândia',
                'Taiwan',
                'Trinidad e Tobago',
                'Tunísia',
                'Turquia',
                'Ucrânia',
                'Uruguai',
                'Venezuela',
                'Vietnã',
            ]
        },
        'page_tittle': {
            'home': 'rponce66 - Soft & Finances',
            'about': 'Quem Somos - rponce66',
            'services': 'Serviços - rponce66',
            'blog': 'Blog - rponce66',
            'contact': 'Contato - rponce66',
            'service_0': 'Consultoria Contábil - rponce66',
            'service_1': 'Gestão Financeira - rponce66',
            'service_2': 'Auditoria Externa - rponce66',
            'service_3': 'Análise de Dados - rponce66',
            'service_4': 'Desenvolvimento de Software - rponce66',
            'service_5': 'Desenvolvimento Web - rponce66'
        },
        'footer': {
            'copyright': '© 2025 rponce66. Todos os direitos reservados.'
        }
    }
}
