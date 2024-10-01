Funcionalidades:
- Converte arquivos CSV do formato 'Robo de Leads' para o formato 'Ninja Add'.
- Suporta conversão em lote de múltiplos arquivos de uma vez.
- Remove entradas duplicadas com base no ID do usuário.
- Gera uma saída limpa com apenas as colunas necessárias.

Requisitos:
- Python 3.10 ou superior
- Biblioteca pandas

Instalação:
1. Clone o repositório:
   git clone https://github.com/nicollasm/Robo2NinjaConverter.git

2. Navegue até o diretório do projeto:
   cd Robo2NinjaConverter

3. Crie um ambiente virtual e ative-o:
   python -m venv .venv
   
   .venv\\Scripts\\activate  # No Windows
   
   source .venv/bin/activate  # No macOS/Linux

5. Instale as dependências necessárias:
   pip install -r requirements.txt

Uso:
1. Execute a aplicação Python para converter seus arquivos CSV:
   python main.py

2. Siga as instruções para selecionar seus arquivos de entrada e gerar o arquivo de saída.

Licença:
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
