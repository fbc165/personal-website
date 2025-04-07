# views.py
from django.shortcuts import render


def homepage(request):
    context = {
        "name": "Fabricio Alves",
        "title": "Engenheiro de Software",
        "about": "Sou engenheiro com experiência em desenvolvimento web, Python, automação industrial e sistemas distribuídos.",
        "experience": [
            {
                "position": "Estagiário em Desenvolvimento Web",
                "company": "STMicroelectronics",
                "duration": "Jan 2023 - Jun 2023",
                "description": "Desenvolvimento de aplicação web e backend de IA com Django, FastAPI, PostgreSQL.",
            },
            {
                "position": "Estágio em Automação",
                "company": "AUTOMA",
                "duration": "Mai 2022 - Dez 2022",
                "description": "Programação em Python para sistemas SCADA e automação de subestações.",
            },
        ],
        "education": [
            {
                "degree": "Engenharia de Controle e Automação",
                "institution": "UNIFEI",
                "duration": "2018 - 2025",
            },
            {
                "degree": "Engenharia da Computação (duplo diploma)",
                "institution": "ENIB - França",
                "duration": "2022 - 2024",
            },
        ],
        "skills": [
            "Python",
            "Django",
            "FastAPI",
            "PostgreSQL",
            "JavaScript",
            "HTMX",
            "Node-RED",
            "AWS",
        ],
        "languages": ["Português (nativo)", "Inglês (avançado)", "Francês (fluente)"],
    }
    return render(request, "homepage.html", context)
