import conexao
cursor = conexao.conexao.cursor()

def cadastrar_produto():
    nome=input('Nome: ')
    try:
        preco=float(input('Preço: '))
        estoque=int(input('Estoque: '))
    except ValueError:
        print('Valor de preço ou estoque inválidos.')
        return
    categoria=input('Categoria: ')
    try:
        sql_select='''SELECT nome FROM produtos
        WHERE nome = %s'''
        cursor.execute(sql_select, (nome,))
        resultado=cursor.fetchone()
    except Exception as erro:
        print(f'Erro do banco: {erro}')
        return
    if resultado:
        print('Produto já cadastrado!')
    else:
        try:
            sql='''INSERT INTO produtos (nome, preco, estoque, categoria)
            VALUES (%s,%s,%s,%s)'''
            valores=(nome, preco, estoque, categoria)
            cursor.execute(sql, valores)
            conexao.conexao.commit()
            print('Produto cadastrado!')
        except Exception as erro:
            print(f'Erro do banco: {erro}')
            return
def listar_produto():
    nome=input('Digite o nome do produto: ')
    try:
        sql_select='''SELECT * FROM produtos
        WHERE nome = %s'''
        cursor.execute(sql_select,(nome,))
        resultado=cursor.fetchone()
    except Exception as erro:
        print(f'Erro do banco: {erro}')
        return
    if resultado:
        print(23*'=')
        print('Produto encontrado!')
        print(f'ID: {resultado[0]}')
        print(f'Nome: {resultado[1]}')
        print(f'Preço: {resultado[2]}')
        print(f'Estoque: {resultado[3]}')
        print(f'Categoria: {resultado[4]}')
        print(23*'=')
    else:
        print('Produto não encontrado!')

def deletar_produto():
    nome=input('Digite o nome do produto para deletar: ')
    try:
        sql_select='''SELECT nome FROM produtos
        WHERE nome = %s'''
        cursor.execute(sql_select, (nome,))
        resultado=cursor.fetchone()
    except Exception as erro:
        print(f'Erro do banco: {erro}')
        return
    if resultado:
        try:
            sql_delete='''DELETE FROM produtos
            WHERE nome = %s'''
            cursor.execute(sql_delete,(nome,))
            conexao.conexao.commit()
            print(f'Produto {nome} deletado!')
        except Exception as erro:
            print(f'Erro do banco: {erro}')
            return
    else:
        print('Produto não econtrado')

def atualizar_nome():
        id=pedir_id()
        if id is None:
            return
        nome=input('Nome: ')
        try:
            update='''UPDATE produtos
            SET nome = %s
            WHERE id = %s'''
            cursor.execute(update,(nome, id,))
            if cursor.rowcount > 0:
                conexao.conexao.commit()
                mostrar_produto(id)
            else:
                print('Produto não encontrado!')
        except Exception as erro:
            print(f'Erro do banco: {erro}')
            return

def atualizar_preco():
    id=pedir_id()
    if id is None:
        return
    try:    
        preco=float(input('Preço: '))
    except ValueError: 
        print('Digite um número válido')
        return
    try:
        update='''UPDATE produtos
        SET preco = %s
        WHERE id = %s'''
        cursor.execute(update,(preco,id))
        if cursor.rowcount>0:
            conexao.conexao.commit()
            mostrar_produto(id)
        else:
            print('Produto não encontrado!')
    except Exception as erro:
        print(f'Erro do banco: {erro}') 
        return
    
def atualizar_estoque():
        id=pedir_id()
        if id is None:
            return
        try:
            estoque=int(input('Estoque: '))
        except ValueError :
            print('Digite um número válido')
            return
        try:
            update='''UPDATE produtos
            SET estoque = %s
            WHERE id = %s'''
            cursor.execute(update,(estoque,id))
            if cursor.rowcount>0:
                conexao.conexao.commit()
                mostrar_produto(id)
            else:
                print('Produto não encontrado!')
        except Exception as erro:
            print(f'Erro do banco: {erro}')
            return

def atualizar_categoria():
        id=pedir_id()
        if id is None:
            return
        categoria=input('Categoria: ')
        try:
            update='''UPDATE produtos
            SET categoria = %s
            WHERE id = %s'''
            cursor.execute(update,(categoria,id))
            if cursor.rowcount>0:
                conexao.conexao.commit()
                mostrar_produto(id)
            else:
                print('Produto não encontrado!')
        except Exception as erro:
            print(f'Erro do banco: {erro}')
            return
def update_cadastro():
    try:
        resposta=int(input('Deseja alterar o nome(1), preço(2), estoque(3) ou categoria(4)? '))
    except ValueError:
        print('Digite um número interio válido!')
        return
    if resposta==1:
        atualizar_nome()
    elif resposta==2:
        atualizar_preco()
    elif resposta==3:
        atualizar_estoque()
    elif resposta==4:
        atualizar_categoria()
    else:
        print('Ação inválida')

def pedir_id():
    try:
        id=int(input('ID: '))
        return id
    except ValueError:
        print('Digite um número inteiro válido')
        return

def mostrar_produto(id):
    sql = '''
    SELECT * FROM produtos
    WHERE id = %s
    '''
    cursor.execute(sql, (id,))
    resultado = cursor.fetchone()

    if resultado:
        print(23*'=')
        print(f'ID: {resultado[0]}')
        print(f'Nome: {resultado[1]}')
        print(f'Preço: {resultado[2]}')
        print(f'Estoque: {resultado[3]}')
        print(f'Categoria: {resultado[4]}')
        print(23*'=')

while True:
    print(23*'=')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Deletar produto')
    print('4 - Atualizar produto')
    print('5 - Sair')
    print(23*'=')

    try:
        r=int(input('> '))
    except ValueError:
        print('Digite um número inteiro válido!')
        continue
    if r==1:
        cadastrar_produto()
    elif r==2:
        listar_produto()
    elif r==3:
        deletar_produto()
    elif r==4:
        update_cadastro()
    elif r==5:
        print('Saindo...')
        break
    else:
        print('Ação inválida!')