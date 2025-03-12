# Sistema Bancário em Python

Este é um projeto simples, para o desafio DIO, de um sistema bancário desenvolvido em Python. Ele permite criar contas, realizar depósitos, saques, ver extratos e listar todas as contas cadastradas.

---

## **Funcionalidades**

1. **Criar Conta**:
   - Crie uma nova conta bancária com um número e um titular.

2. **Depositar**:
   - Realize depósitos em uma conta existente.

3. **Sacar**:
   - Realize saques de uma conta existente (desde que haja saldo suficiente).

4. **Ver Extrato**:
   - Visualize o extrato de uma conta, com todas as transações e o saldo atual.

5. **Listar Contas**:
   - Veja uma lista de todas as contas cadastradas no banco.

6. **Sair**:
   - Encerre o programa.

---

## **Estrutura do Projeto**

O projeto é composto pelos seguintes arquivos:

- **`conta.py`**: Contém a classe `Conta`, que representa uma conta bancária.
- **`banco.py`**: Contém a classe `Banco`, que gerencia múltiplas contas.
- **`main.py`**: O ponto de entrada do programa, onde o sistema bancário é executado.
- **`README.md`**: Este arquivo, que documenta o projeto.

---

## **Como Executar o Projeto**

### **Pré-requisitos**

- Python 3.x instalado.
- Nenhuma dependência externa é necessária.

### **Passos para Executar**

1. Clone o repositório ou baixe os arquivos do projeto.

2. Navegue até a pasta do projeto:

   ```bash
   cd sistema_bancario
   ```

3. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

4. Siga as instruções no menu interativo para usar o sistema bancário.

---

## **Exemplo de Uso**

Aqui está um exemplo de como usar o sistema:

1. **Criar uma conta**:
   ```
   Escolha uma opção: 1
   Número da conta: 123
   Nome do titular: João Silva
   Conta 123 criada para João Silva.
   ```

2. **Depositar dinheiro**:
   ```
   Escolha uma opção: 2
   Número da conta: 123
   Valor do depósito: 1000
   Depósito de R$1000.0 realizado com sucesso.
   ```

3. **Ver extrato**:
   ```
   Escolha uma opção: 4
   Número da conta: 123

   --- Extrato da Conta 123 ---
   Titular: João Silva
   Transações:
   Depósito: +1000.0
   Saldo atual: R$1000.0
   ```

4. **Listar contas**:
   ```
   Escolha uma opção: 5

   --- Contas no Banco Banco DIO ---
   Conta 123 - Titular: João Silva - Saldo: R$1000.0
   ```

5. **Sair**:
   ```
   Escolha uma opção: 6
   Saindo...
   ```

---

## **Melhorias Futuras**

Este projeto pode ser expandido com as seguintes funcionalidades:

1. **Validação de Dados**:
   - Verificar se o número da conta é único.
   - Validar o nome do titular (evitar números ou caracteres especiais).

2. **Transferências entre Contas**:
   - Permitir transferências de dinheiro entre contas.

3. **Persistência de Dados**:
   - Salvar os dados das contas em um arquivo (`.txt` ou `.json`) para persistência.

4. **Interface Gráfica**:
   - Criar uma interface gráfica usando `tkinter` ou outra biblioteca.

5. **Segurança**:
   - Adicionar autenticação com senha para acessar as contas.

---

## **Contribuição**

Se você quiser contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## **Contato**

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- **GitHub**: [EdBispoDev](https://github.com/EdbispoDev)



