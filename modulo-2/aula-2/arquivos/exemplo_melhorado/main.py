# 🚀 Main - Teste do Sistema de Aprovação
# Arquivo principal que importa dados do data lake e testa as funções de ML

from dados_alunos import carregar_dados, obter_features_target
from modelo_aprovacao import ModeloAprovacao, criar_modelo_treinado

def main():
    """Função principal que testa todo o sistema"""
    
    print("🎓 Sistema de Previsão de Aprovação")
    print("=" * 50)
    
    # 1. Carregar dados do data lake
    print("\n📊 1. Carregando dados do data lake...")
    df = carregar_dados()
    print(f"   - Dataset carregado com {len(df)} alunos")
    print(f"   - Colunas: {list(df.columns)}")
    
    # 2. Separar features e target
    print("\n🔧 2. Preparando dados para ML...")
    X, y = obter_features_target()
    print(f"   - Features: {list(X.columns)}")
    print(f"   - Target: aprovado")
    
    # 3. Criar e treinar modelo
    print("\n🧠 3. Treinando modelo de ML...")
    modelo = criar_modelo_treinado()
    modelo.mostrar_info_modelo()
    
    # 4. Testar previsões individuais
    print("\n🎯 4. Testando previsões individuais...")
    testes = [
        (4, 2, "Aluno com 4h estudo, 2 faltas"),
        (1, 8, "Aluno com 1h estudo, 8 faltas"),
        (7, 0, "Aluno com 7h estudo, 0 faltas"),
        (3, 5, "Aluno com 3h estudo, 5 faltas")
    ]
    
    for horas, faltas, descricao in testes:
        resultado = modelo.prever_aprovacao(horas, faltas)
        print(f"   - {descricao}: {resultado}")
    
    # 5. Testar previsões múltiplas
    print("\n👥 5. Testando previsões múltiplas...")
    horas_list = [2, 6, 8, 1, 5]
    faltas_list = [3, 1, 0, 7, 2]
    
    resultados = modelo.prever_multiplos_alunos(horas_list, faltas_list)
    for resultado in resultados:
        print(f"   - {resultado}")
    
    print("\n✅ Testes concluídos com sucesso!")

if __name__ == "__main__":
    main()
