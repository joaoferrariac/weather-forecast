# Aplicativo de Previsão do Tempo

![Captura de Tela do Aplicativo](adicionar-imagem-aqui)

## 📌 Visão Geral
Aplicativo de previsão do tempo desenvolvido em Python utilizando a API do OpenWeatherMap. Exibe condições climáticas atuais e previsão para os próximos 4 dias, com opção de trocar a cidade.

## ✨ Funcionalidades
- 🌦️ Exibição do clima atual (temperatura, sensação térmica, umidade, vento)
- 📅 Previsão para os próximos 4 dias
- 🏙️ Troca de cidade pesquisada
- 🌍 Suporte a múltiplas localidades
- 🖼️ Ícones ilustrativos das condições climáticas

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- Tkinter (interface gráfica)
- API OpenWeatherMap
- Biblioteca Requests (chamadas HTTP)
- PIL/Pillow (manipulação de imagens)

## ⚙️ Instalação
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/weather-app.git
cd weather-app
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Obtenha uma chave de API gratuita no OpenWeatherMap

Crie um arquivo `settings.py` em `models/` com:

```python
class Settings:
    API_KEY = "sua_chave_aqui"
    BASE_URL = "http://api.openweathermap.org/data/2.5/"
    UNITS = "metric"
    LANG = "pt_br"
    DEFAULT_CITY = "São Paulo"
```

## 🚀 Como Executar

```bash
python app.py
```

## 🗂️ Estrutura do Projeto

```
weather-app/
├── assets/               # Arquivos estáticos
├── controllers/          # Lógica de controle
├── models/               # Modelos e acesso a dados
├── views/                # Componentes de interface
│   ├── components/       # Componentes reutilizáveis
├── app.py                # Ponto de entrada
└── README.md
```

## 📝 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 🤝 Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📧 Contato
**João Ferrari** - [joaoferraridev@gmail.com](mailto:joaoferraridev@gmail.com)

🔗 **Link do Projeto:** [https://github.com/joaoferrariac/weather-forecast](https://github.com/joaoferrariac/weather-forecast)
