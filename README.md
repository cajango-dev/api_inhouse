# InHouse API

API para gerenciamento de partidas in-house de League of Legends.  
Desenvolvida em Django, com arquitetura modular por app e painel de administração personalizado com Jazzmin.

## 🚀 Funcionalidades

- Gestão de jogadores, temporadas, partidas e estatísticas.
- Painel de administração customizado (modo escuro, ícone e nome personalizados).
- Autenticação com JWT via DRF.
- Estrutura organizada por "feature folders" (apps independentes).
- Ícones e nomes personalizados para facilitar a navegação no admin.

## 📁 Estrutura de Apps

Cada entidade principal está separada em sua própria pasta com:
- `models.py`
- `views.py`
- `serializers.py`
- `urls.py`
- `apps.py`

Apps incluídos:

- `players` → Jogadores  
- `matches` → Partidas  
- `seasons` → Temporadas  
- `season_players` → Jogadores da Temporada  
- `player_matches` → Partidas de Jogador  
- `season_player_lanes` → Estatísticas por Rota  
- `champions` → Campeões  
- `champion_tier_list` → Tier List de Campeões  
- `staff` → Equipe  
- `authentication` → Autenticação personalizada  
- `inqueue` → Fila de partidas  

## 🛠️ Requisitos

- Python 3.11+
- Django 4.x
- Django REST Framework
- Django Simple JWT
- Jazzmin

## ⚙️ Setup do Projeto

```bash
# Crie e ative seu ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Faça as migrações
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Rode o servidor com abertura automática do admin
python runserver_open.py


📜 Licença
LeagueOfHu3BR © 2025
