

import json

usuarios = {
    "1": {
        "nombre": "Daniel",
        "apellido": "Herrera",
        "contacto": {
            "correo": "garyford@gmail.com",
            "telefono": "001-512-801-0651x67779",
            "direccion": {
                "calle": "178 Walker Island Suite 840",
                "ciudad": "Gonzalezmouth",
                "estado": "Michigan",
                "codigo_postal": "92488",
                "pais": "Bermuda"
            }
        },
        "perfil": {
            "username": "bradley18",
            "fecha_nacimiento": "1987-07-15",
            "genero": "Masculino",
            "ocupacion": "Financial planner"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/mistytaylor",
            "linkedin": "https://linkedin.com/in/nancythomas",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": True,
            "temas_interes": ["arte", "moda", "tecnología"]
        }
    },
    "2": {
        "nombre": "Joseph",
        "apellido": "Sullivan",
        "contacto": {
            "correo": "grussell@hotmail.com",
            "telefono": "006-305-4158x3659",
            "direccion": {
                "calle": "9638 Hawkins Crossing Apt. 914",
                "ciudad": "Robertchester",
                "estado": "Illinois",
                "codigo_postal": "28682",
                "pais": "Ethiopia"
            }
        },
        "perfil": {
            "username": "kennethtaylor",
            "fecha_nacimiento": "1981-03-26",
            "genero": "Otro",
            "ocupacion": "Clinical psychologist"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/claire15",
            "linkedin": "",
            "instagram": "https://instagram.com/kellycooper"
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": False,
            "temas_interes": ["deportes", "arte", "viajes"]
        }
    },
    "3": {
        "nombre": "Kristina",
        "apellido": "Bradley",
        "contacto": {
            "correo": "mark58@hotmail.com",
            "telefono": "771-464-1767",
            "direccion": {
                "calle": "9396 Martin Bridge Apt. 544",
                "ciudad": "South Ryan",
                "estado": "Iowa",
                "codigo_postal": "41958",
                "pais": "Philippines"
            }
        },
        "perfil": {
            "username": "christine51",
            "fecha_nacimiento": "1966-09-21",
            "genero": "Femenino",
            "ocupacion": "Restaurant manager, fast food"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/dickersonjustin",
            "linkedin": "https://linkedin.com/in/michaela78",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["cocina", "tecnología", "viajes"]
        }
    },
    "4": {
        "nombre": "Monica",
        "apellido": "Molina",
        "contacto": {
            "correo": "daniel59@yahoo.com",
            "telefono": "(925)185-9544x03157",
            "direccion": {
                "calle": "53484 Garrett Wall",
                "ciudad": "East Sherri",
                "estado": "Washington",
                "codigo_postal": "81748",
                "pais": "Syrian Arab Republic"
            }
        },
        "perfil": {
            "username": "kayla97",
            "fecha_nacimiento": "1987-11-19",
            "genero": "Femenino",
            "ocupacion": "Company secretary"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/rgomez",
            "linkedin": "",
            "instagram": "https://instagram.com/sarah44"
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["viajes", "deportes", "tecnología"]
        }
    },
    "5": {
        "nombre": "Angela",
        "apellido": "House",
        "contacto": {
            "correo": "pwaters@dixon.biz",
            "telefono": "(616)639-1141",
            "direccion": {
                "calle": "8264 Morgan Lights",
                "ciudad": "Dianetown",
                "estado": "North Dakota",
                "codigo_postal": "64546",
                "pais": "Bolivia"
            }
        },
        "perfil": {
            "username": "randy13",
            "fecha_nacimiento": "2006-02-20",
            "genero": "Masculino",
            "ocupacion": "Airline pilot"
        },
        "redes_sociales": {
            "twitter": "",
            "linkedin": "https://linkedin.com/in/watkinsjessica",
            "instagram": "https://instagram.com/longlaura"
        },
        "preferencias": {
            "idioma": "Inglés",
            "newsletter": False,
            "temas_interes": ["moda", "arte", "cocina"]
        }
    }
}

def es_vacio(valor):
    return valor == ""

def formatear_campo(valor):
    if es_vacio(valor):
        return '<td class="vacio">[VACÍO]</td>'
    return f"<td>{valor}</td>"

def generar_tabla_usuario(uid, datos):
    nombre_completo = f"{datos['nombre']} {datos['apellido']}"
    html = [f'<h2>Usuario {uid} – {nombre_completo}</h2>']

    # Contacto
    contacto = datos["contacto"]
    direccion = contacto["direccion"]
    html.append('<table class="contacto"><tr><th colspan="2">Contacto</th></tr>')
    html.append(f"<tr><td>Correo</td>{formatear_campo(contacto['correo'])}</tr>")
    html.append(f"<tr><td>Teléfono</td>{formatear_campo(contacto['telefono'])}</tr>")
    for campo in ["calle", "ciudad", "estado", "codigo_postal", "pais"]:
        html.append(f"<tr><td>{campo.title()}</td>{formatear_campo(direccion[campo])}</tr>")
    html.append('</table>')

    # Perfil
    perfil = datos["perfil"]
    html.append('<table class="perfil"><tr><th colspan="2">Perfil</th></tr>')
    for campo in ["username", "fecha_nacimiento", "genero", "ocupacion"]:
        html.append(f"<tr><td>{campo.replace('_', ' ').title()}</td>{formatear_campo(perfil[campo])}</tr>")
    html.append('</table>')

    # Redes sociales
    redes = datos["redes_sociales"]
    html.append('<table class="redes"><tr><th colspan="2">Redes Sociales</th></tr>')
    for campo in ["twitter", "linkedin", "instagram"]:
        html.append(f"<tr><td>{campo.title()}</td>{formatear_campo(redes[campo])}</tr>")
    html.append('</table>')

    # Preferencias
    preferencias = datos["preferencias"]
    html.append('<table class="preferencias"><tr><th colspan="2">Preferencias</th></tr>')
    html.append(f"<tr><td>Idioma</td>{formatear_campo(preferencias['idioma'])}</tr>")
    html.append(f"<tr><td>Newsletter</td><td>{'✔️' if preferencias['newsletter'] else '❌'}</td></tr>")
    temas = ', '.join(preferencias['temas_interes'])
    html.append(f"<tr><td>Temas de Interés</td>{formatear_campo(temas)}</tr>")
    html.append('</table>')

    return "\n".join(html)

# Estilo CSS para el HTML
css = """
<style>
    table {
        width: 100%;
        margin: 20px 0;
        border-collapse: collapse;
    }
    th, td {
        padding: 8px 12px;
        border: 1px solid #ccc;
    }
    th {
        background-color: #333;
        color: white;
    }
    .contacto {
        background-color: #d9edf7;
    }
    .perfil {
        background-color: #dff0d8;
    }
    .redes {
        background-color: #fcf8e3;
    }
    .preferencias {
        background-color: #f2dede;
    }
    .vacio {
        background-color: #ffcccc;
        font-weight: bold;
    }
    h2 {
        margin-top: 40px;
        border-bottom: 2px solid #333;
    }
</style>
"""

# Generar el HTML completo
html = ['<html><head><meta charset="UTF-8"><title>Usuarios</title>', css, '</head><body>']
for uid, datos in usuarios.items():
    html.append(generar_tabla_usuario(uid, datos))
html.append('</body></html>')

# Guardar en archivo
with open("usuarios.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print("Archivo 'usuarios.html' generado correctamente.")
