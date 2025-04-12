# views.py
from django.shortcuts import render


def homepage(request):
    context = {
        "name": "Fabricio Alves",
        "title": "Engenheiro de Software",
        "about": "Engenheiro de controle e automação com experiência em desenvolvimento web backend, python e sistemas distribuídos.  Busco sempre realizar entregas de valor que contribuam para melhora da aplicação e experiência do usuário",
        "experience": [
            {
                "position": "Engenheiro de Software",
                "company": "Telavita",
                "duration": "Nov 2024 - Presente",
                "description": "Nesta healthtech, desenvolvo e dou manutenção no backend nos microsserviços em python da aplicação. Crio automações usando n8n e javascript.",
            },
            {
                "position": "Estagiário em Engenharia de Software",
                "company": "STMicroelectronics",
                "duration": "Jan 2024 - Agosto 2024",
                "description": "Desenvolvi uma aplicação web que possibilitou a acessibilidade de um modelo de IA interno para predição de valores de um circuito eletrônico",
            },
            {
                "position": "Estagiário em engenharia de sistemas",
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
            "Flask",
            "PostgreSQL",
            "JavaScript",
            "n8n",
            "Node.JS",
            "Express.JS",
            "Javascript",
            "Docker",
            "HTMX",
            "CI/CD",
            "AWS",
            "C",
            "POO",
            "Jenkins",
        ],
        "languages": ["Português (nativo)", "Inglês (avançado)", "Francês (fluente)"],
    }
    return render(request, "homepage.html", context)
