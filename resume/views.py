# views.py
from django.shortcuts import render


def homepage(request):
    context = {
        "name": "Fabricio Alves",
        "linkedin": "https://linkedin.com/in/fabricioalves1",
        "github": "https://github.com/fbc165",
        "email": "fabricio.alves2698@gmail.com",
        "title": "👷‍♂️💻 Engenheiro de Software",
        "about": "Engenheiro de software backend especializado em Python, com experiência em criar sistemas eficientes e escaláveis. \
            Valorizo código limpo, boas práticas e soluções simples para problemas complexos.\
            Busco sempre realizar entregas de valor que contribuam da melhor maneira pro négocio priorizando sempre a experiência do usuário final.",
        "experience": [
            {
                "position": "Engenheiro de Software",
                "company": "Telavita",
                "duration": "Nov 2024 - Presente",
                "description": "Desenvolvo novas features no sistema, realizo a manutenção e faço correção de bugs no backend da aplicação.\
                    Além disso, crio automações usando n8n e javascript para as diversas equipes da empresa.",
            },
            {
                "position": "Estagiário em Engenharia de Software",
                "company": "STMicroelectronics",
                "duration": "Jan 2024 - Agosto 2024",
                "description": "Desenvolvi uma aplicação web que tornou acessível um modelo próprio da empresa de I.A para predição \
                    de parâmetros de um circuito eletrônico. Esse projeto reduziu o custo com licenças de software de simulação \
                    em aproximadamente €10.000 mensais e aumentou a produtividade de várias equipes devido a redução em 99% do tempo de espera dos resultados.",
            },
            {
                "position": "Estagiário em Engenharia de Sistemas",
                "company": "AUTOMA",
                "duration": "Mai 2022 - Dez 2022",
                "description": "Implementei scripts em python para automação de processos industriais, otimizando fluxos de dados.\
                    Esse projeto permitiu aumentar a produtividade da minha equipe devido a eliminação de tarefas repetitivas e demoradas.",
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
            {"name": "Python", "level": 90},
            {"name": "Django", "level": 90},
            {"name": "FastAPI", "level": 75},
            {"name": "PostgreSQL", "level": 85},
            {"name": "JavaScript", "level": 80},
            {"name": "n8n", "level": 90},
            {"name": "Node.JS", "level": 80},
            {"name": "Express.JS", "level": 80},
            {"name": "Docker", "level": 70},
            {"name": "HTMX", "level": 50},
            {"name": "CI/CD", "level": 80},
            {"name": "Jenkins", "level": 65},
        ],
        "languages": ["Português (nativo)", "Inglês (avançado)", "Francês (fluente)"],
        "projects": [
            {
                'name': 'Sistema Web para Subestações',
                'description': 'Aplicação distribuída com mensageria para controle central de dados.',
                'link': 'https://github.com/seu-usuario/seu-projeto'
            },
        ],
    }
    return render(request, "homepage.html", context)
