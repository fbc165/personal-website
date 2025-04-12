# views.py
from django.shortcuts import render


def homepage(request):
    context = {
        "name": "Fabricio Alves",
        "title": "👷‍♂️💻 Engenheiro de Software",
        "about": "Engenheiro com experiência em desenvolvimento web backend, python e sistemas distribuídos.  Busco sempre realizar entregas de valor que contribuam da melhor maneira pro négocio priorizando sempre a experiência do usuário final",
        "experience": [
            {
                "position": "Engenheiro de Software",
                "company": "Telavita",
                "duration": "Nov 2024 - Presente",
                "description": "Desenvolvo e dou manutenção no backend nos microsserviços da aplicação. Crio automações usando n8n e javascript.",
            },
            {
                "position": "Estagiário em Engenharia de Software",
                "company": "STMicroelectronics",
                "duration": "Jan 2024 - Agosto 2024",
                "description": "Desenvolvi uma aplicação web que tornou acessível um modelo de IA interno para predição \
                    de parâmetros de um circuito eletrônico. Esse projeto reduziu o custo com software proprietários de simulação \
                    em até 45% e aumentou a produtividade das equipes devido a redução de tempo de espera dos resultados em 99%",
            },
            {
                "position": "Estagiário em Engenharia de Sistemas",
                "company": "AUTOMA",
                "duration": "Mai 2022 - Dez 2022",
                "description": "Implementei scripts em python para automação de processos industriais, otimizando fluxos de dados.",
            },
        ],
        "education": [
            {
                "degree": "Engenharia de Controle e Automação",
                "institution": "Universidade Federal de Itajubá",
                "duration": "2018 - 2025",
            },
            {
                "degree": "Engenharia da Computação (duplo diploma)",
                "institution": "École Nationale d'Ingénieurs de Brest",
                "duration": "2022 - 2024",
            },
        ],
        "skills": [
            "Python",
            "Django",
            "FastAPI",
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
            "Jenkins",
        ],
        "languages": ["Português (nativo)", "Inglês (avançado)", "Francês (fluente)"],
    }
    return render(request, "homepage.html", context)
