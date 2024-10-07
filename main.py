import os
import pandas as pd
from tkinter import filedialog
from tkinter import Tk

PATTERN_NINJA_CSV = os.path.join(os.getenv('LOCALAPPDATA'), 'programs', 'Ninja Add', 'Listas', 'usuarios_backup.csv')

def selecionar_arquivos():
    """Função para selecionar múltiplos arquivos via janela gráfica."""
    root = Tk()
    root.withdraw()  # Esconder a janela principal
    file_paths = filedialog.askopenfilenames(title="Selecione os arquivos CSV sujos",
                                             filetypes=[("CSV files", "*.csv")])
    return file_paths


def processar_csv(file_paths):
    """Função para processar e converter arquivos CSV para o formato correto."""
    consolidado = pd.DataFrame()

    for file in file_paths:
        try:
            # Carregar o arquivo sujo
            df_sujo = pd.read_csv(file, sep=None, engine='python')  # Detectar automaticamente o delimitador

            # Extrair e renomear as colunas importantes, ignorando a coluna 'telefone'
            df_sujo_clean = df_sujo[['user_id', 'nome', 'username']].copy()
            df_sujo_clean.columns = ['ID', 'Name', 'Username']

            # O Ninja só poderá encontrar usuários que tiverem username
            df_sujo_clean.dropna(subset=['Username'], inplace=True)

            # Remover duplicatas
            df_sujo_clean.drop_duplicates(subset=['ID'], inplace=True)

            # Concatenar no consolidado
            consolidado = pd.concat([consolidado, df_sujo_clean])

        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {e}")

    # Remover duplicatas no consolidado final
    consolidado.drop_duplicates(subset=['ID'], inplace=True)

    return consolidado


def salvar_arquivo(consolidado, output_path=PATTERN_NINJA_CSV):
    """Função para salvar o arquivo consolidado em formato CSV."""
    if not consolidado.empty:
        if output_path:
            consolidado.to_csv(output_path, index=False)
            print(f"Arquivo salvo em {output_path}")
            print('Ative a opção "backup" antes de adicionar para o Ninja Add trabalhar com ela')
        else:
            print("Nenhum local de salvamento foi selecionado.")
    else:
        print("O DataFrame consolidado está vazio. Nenhum arquivo foi salvo.")


# Fluxo principal
if __name__ == "__main__":
    # Selecionar arquivos CSV
    arquivos_selecionados = selecionar_arquivos()

    if arquivos_selecionados:
        # Processar arquivos
        consolidado = processar_csv(arquivos_selecionados)

        # Verificar se há dados para salvar
        if not consolidado.empty:
            # Salvar o arquivo final
            salvar_arquivo(consolidado)
        else:
            print("Nenhum dado foi consolidado, nada será salvo.")
    else:
        print("Nenhum arquivo selecionado.")
