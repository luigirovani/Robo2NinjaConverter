import pandas as pd
from tkinter import filedialog
from tkinter import Tk


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

            # Remover duplicatas
            df_sujo_clean.drop_duplicates(subset=['ID'], inplace=True)

            # Concatenar no consolidado
            consolidado = pd.concat([consolidado, df_sujo_clean])

        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {e}")

    # Remover duplicatas no consolidado final
    consolidado.drop_duplicates(subset=['ID'], inplace=True)

    return consolidado


def salvar_arquivo(consolidado):
    """Função para salvar o arquivo consolidado em formato CSV."""
    if not consolidado.empty:
        output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
                                                   title="Salvar arquivo")
        if output_path:
            # Salvar o arquivo CSV sem o campo Phone
            consolidado.to_csv(output_path, index=False)
            print(f"Arquivo salvo em {output_path}")
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
