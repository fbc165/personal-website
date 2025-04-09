# views.py
from django.shortcuts import render


def homepage(request):
    context = {
        "name": "Fabricio Alves",
        "title": "Engenheiro de Software",
        "about": "Engenheiro de formação com experiência em desenvolvimento web backend, python e sistemas distribuídos.",
        "experience": [
            {
                "position": "Engenheiro de Software",
                "company": "Telavita",
                "duration": "Nov 2024 - Presente",
                "description": "Desenvolvo e dou manutenção no backend nos microsserviços da aplicação. Crio automações usando python, n8n e javascript.",
            },
            {
                "position": "Estagiário em Desenvolvimento Web",
                "company": "STMicroelectronics",
                "duration": "Jan 2023 - Jun 2023",
                "description": "Desenvolvi uma aplicação web que possibilitou a acessibilidade de um modelo de IA interno",
            },
            {
                "position": "Desenvolvedor Python",
                "company": "AUTOMA",
                "duration": "Mai 2022 - Dez 2022",
                "description": "Implementei scripts em Python para automação de processos industriais, otimizando fluxos de dados e reduzindo o tempo de processamento em 40%..",
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
            "Node.JS",
            "HTMX",
            "AWS",
        ],
        "languages": ["Português (nativo)", "Inglês (avançado)", "Francês (fluente)"],
    }
    return render(request, "homepage.html", context)
