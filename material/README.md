
![Logo](https://github.com/reprograma/on35-python-s05-projeto-guiado-I/blob/main/assets/reprograma-fundos-claros.png?raw=true)


# Print Reprograma

Essa é um componente de print com esteroides para deixar nosso terminal mais bunitinho


## cor(`<cor>`)

Essa função tem como objetivo mudar a cor do texto, abaixo está as correr que ele aceita

| Nome da cor | abreviado | negrito        | abreviado em negrito |
|-------------|-----------|----------------|----------------------|
| branco      | w         | branco negrito | wb                   |
| vermelho    | r         | vermelho       | rb                   |
| verde       | g         | verde          | gb                   |
| amarelo     | y         | amarelo        | yb                   |
| azul        | b         | azul           | bb                   |
| magenta     | m         | magenta        | mb                   |
| ciano       | c         | ciano          | cb                   |
| cinza       | gr        | cinza          | grb                  |

Tirando as cores tambem é possivel deixar o texto em negrito passando a cor como:

`negrito`

## pular_linha()

Essa função pula uma linha

---

### quantidade
valor padrão = 1
muda o numero de linhas que são puladas

    pular_linha(quantidade = 4)

## limpar()

Limpa a tela
## limpar_formatacao()

Remove todas as formatações feitas e volta ao padrão do terminal
## separador(`<tamanho>`)

Imprime um separador na tela do tamanho informado 

---

### caracter
valor padrão = '═'
muda o caracter usado para fazer a separação

    separador(caracter = '-')
### cor_texto
valor padrão = ''
muda a cor do separador

    separador(cor_texto = 'amarelo')
## imprimir(`<textos>`)

Imprime os textos passados, ele aceita vários textos separados por virgula

    imprimir('Olá mundo')
    imprimir('Olá','mundo') 

---

### sep
valor padrão = ' '
muda o caracter usado para fazer a separação dos textos

    imprimir(texto1,texto2,texto3,';')
### end
valor padrão = '\n'
muda o último caracter que será colocado no texto

    imprimir('manter esse texto na linha',end='')
### tamanho	
valor padrão = 0
define o tamanho do texto a ser exibido

    imprimir('manter esse texto na linha',tamanho=100)
### caracter	
valor padrão = ' '
caracter que será usado para completar a linha caso o texto seja menor que o tamanho

    imprimir('manter esse texto na linha',caracter='.',tamanho=100)
### alinhar
valor padrão = ' comeco'
define como o texto será alinhado no tamanho que passado como manutenção

	imprimir('manter esse texto na linha',alinhar='fim',tamanho=100)

 - **comeco** - Alinha no começo
 - **centro** - Alinha ao centro
 - **fim** - Alinha no final

### cor_texto
valor padrão = ''
muda a cor do texto passado

    imprimir('manter esse texto na linha', cor_texto = 'amarelo')
## retangulo(`<texto>`)

Imprime o texto com um retângulo em volta

---

### sv
valor padrão = 0
Separador vertical, define o valor de linhas que será pulado em cima e em baixo do texto

    retangulo('Olá mundo', sv=1)
### sh
valor padrão = 0
Separador horizontal, define o valor de caracteres que será pulados antes e depois do texto

    retangulo('Olá mundo', sh=10)
### tamanho
valor padrão = 0
Tamanho do retângulo que será exibido

    retangulo('Olá mundo', tamanho=100)
### cor_barra
valor padrão = ''
muda a cor da barra do retângulo

    retangulo('Olá mundo', cor_barra = 'amarelo')
### cor_texto
valor padrão = ''
muda a cor do texto dentro do retângulo

    retangulo('Olá mundo', cor_texto = 'amarelo')
### margem
valor padrão = 0
Tamanho de caracteres que seram pulados antes do retângulo

    retangulo('Olá mundo', margem=10)