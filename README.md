# 🗂️ Sistema Task Manager – AT 9 (Testes de Software)

Um sistema simples de **gerenciamento de tarefas** desenvolvido em **Python**, aplicando conceitos de **arquitetura em camadas**, **separação de responsabilidades** e **testes automatizados com pytest**.

---

## ⚙️ Como Usar o Projeto

Siga as instruções abaixo para configurar e executar o projeto no seu ambiente local.

### 🧩 Pré-requisitos

- **Python 3.8+** instalado  
- **pip** (gerenciador de pacotes do Python)

---

### 🚀 Passos para Execução

#### 1️⃣ Clone o repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>
```

### 2️⃣ (Opcional, mas recomendado) Crie e ative um ambiente virtual

Isso isola as dependências do projeto:

### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Linux  
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências

O projeto utiliza as bibliotecas listadas no arquivo requirements.txt.
Execute:
```bash
pip install -r requirements.txt  
```

### 4️⃣ Execute os testes

Para verificar se a implementação está correta, rode a suíte de testes:

```bash
pytest -v
```

Todos os testes devem passar com sucesso ✅  
<img width="923" height="232" alt="image" src="https://github.com/user-attachments/assets/c3544e1b-f176-442a-a2d8-c417882a456b" />  

### 5️⃣ Execute o exemplo de uso

Para ver uma demonstração simples do sistema em ação:

```bash
python app.py
```

### 🧱 Estrutura do Projeto

A organização das pastas separa claramente a lógica da aplicação dos testes automatizados.  

```bash
.
├── task_manager/
│   ├── __init__.py
│   ├── task.py
│   ├── storage.py
│   └── repository.py
├── tests/
│   ├── conftest.py
│   ├── test_task.py
│   └── test_repository.py
├── app.py
├── requirements.txt
└── README.md
```

### 👥 Grupo

Aléxia Santa Rosa Suares – 22.224.016-0    

Gabrielle Mitie Suzuke Tenguan – 22.124.097-1  

Larissa Gonçalves da Silva – 22.224.022-8  
