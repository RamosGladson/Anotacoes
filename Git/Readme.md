# Git
>É um versionador de arquivos.

Git é um versionador de arquivos que pode ser usado por uma pessoa ou um time de desenvolvimento. Foi criado com a finalidade de facilitar o desenvolvimento de softwares, mas pode ser usado com várias finalidades, de versionador de arquivos de imagens para designers até como um caderno de anotações, com acesso local ou global (através do github, desde que tenha acesso a internet). Segue site para auxílio no aprendizado:

>[Learn Git Branching][learn-gitbranching]


Alguns exempos de comandos no git:
```
git config --list    // mostra lista de configurações.
git config --global user.name "Gladson" // configura nome de usuário como Gladson.
git config --global alias.s status      // simplifica o comando status, podendo ser subistituido pela letra s (pode ser feito com qualquer comando).
git init             // inicializa o git na pasta local.
git status           // mostra o status do git.
git add file.txt     // adiciona o arquivo file.txt.
git add .            // adiciona todos os arquivos da pasta local.
git commit -m "texto referencia do commit"  // faz o commit para os arquivos que foram adicionados previamente e passa o texto entre aspas como referencia do commit.
git commit -am "texto"  // adiciona os arquivos untracked e faz o commit.
git show hash        // detalha o hash
git log              // mostra log.
git log --author="Gladson"  // mostra log do autor Gladson.
git shortlog         // mostra log resumido.
git log --graph      // log formato gráfico.
git show hash        // detalha o hash.
git diff             // diferença no arquivo modificado.
git diff --name-only //  mostra os nomes dos arquivos modificados
git checkout Readme.md   // retorna o arquivo para antes da modificação, antes de adicionar o arquivo para commit.
git reset head Readme.md // cancela o add.
git reset --soft hash    // retorna o arquivo ao ponto do commit e deleta as hashs anteriores, ficando o arquivo pronto para o commit.
git reset --mixed hash   // retorna o arquivo antes do add.
git reset --hard hash    // retorna o aquivo para a hash e apaga tudo o que foi feito depois.
git clean -df            // apaga os arquivos untracked
git checkout -- .        // retorna ao ponto do ultimo commit
git revert hash          // parece o reset, porém não apaga o commit com problema e cria um novo commit
git remote               // mostra dados do repo remoto(-v +detail)
git branch               // mostra branch
git branch -m <nomeBranch>      // renomeia a branch (-M = force)
git checkout <nomeBranch>     // navega entre branch (-b cria nova)
git branch -D <nomeBranch>  // deleta a branch local
git push --delete origin <nomeBranch>   // deleta a branch remoto
```


## Ciclo de vida dos arquivos

Os arquivos em um repositório git possuem cinco estágios:
* untracked
* staged
* commited
* modified
* deleted

Um arquivo recem criado nasce no estágio *untracked*, uma vez que esse arquivo é adicionado para o commit ele passa para o estágio de *staged* e apos o commit passa para o estágio de *commited* e caso seja modificado será classificado como *modified*


## Tags

Tags são etiquetas, esse procedimento cria versões do código
```
git tag                                    // mostra as tags
git tag -a v1.0.2.4 -m "Readme finalizado" // versiona tag
git show v1.0.2.4        // mostra as informações da tag
git push origin v1.0.2.4                   // sobe a tag v1.0.2.4
git push origin <nomeBranch> --tags        // sobe todas as tags
git tag -d v1.0.2.4      // deleta a tag v1.0.2.4 local
git push --delete origin v1.0.2.4  // deleta a tag v1.0.2.4 remoto
```


## Merge Rebase Stash

_Merge_ adiciona os commits de outra branch e finaliza com a criação de um nomo commit
```
git merge <nomeBranch>
```

_Rebase_ adiciona os commits de outra branch ao final
```
git rebase <nomeBranch>
```

_Stash_ pausa a altereção de um arquivo podendo iniciar um novo branch
```
git stash
git stash apply       // aplica as mudanças ao branch atual
git stash list        // lista as stashs
git stash clear       // limpa as stashs
```


## Github
>Github é um servidor git remoto

### Gerar/add chaves ssh

*Linux
Gerar as chaves
```
ssh-keygen -f ~/.ssh/arquivo-rsa -t rsa -b 4096  // gera um par de chaves que podem ter senha ou não
```
Add chave no github
```
cat ~/.ssh/arquivo_rsa.pub
```
Copiar e colar no github
// Configurações >> Settings >> SSH Key >> Add

* Windows
Gerar as chaves
```
ssh-keygen -f ~/.ssh/gladson-rsa
ou
ssh-keygen -t ed25519
ou
ssh-keygen -t rsa -b 4096
```
Iniciar agente ssh
```
eval $(ssh-agent)
ssh-add ~/.ssh/arquivo_rsa
```
Add chave no github
```
cat ~/.ssh/arquivo_rsa.pub
```
Copiar e colar no github
// Configurações >> Settings >> SSH Key >> Add

### Enviar arquivos

```
git remote add origin https://github.com/usuario/exemplo.git
git push origin master -u    // envia os arquivos, parametro -U marca origin como padrão
```
ou com troca de chaves
```
git remote add origin git@github.com/usuario/exemplo.git
git push origin master -u    // envia os aruivos, parametro -U marca origin como padrão
```

#### Clonar repositório
```
git clone https://github.com/usuario/exemplo.git
git pull origin master    // atualiza as modificações
```

### Ignorar arquivos no push

Criar arquivo .gitignore e inserir dentro dele as extensões que devem ser ignoradas.
```
echo ".env" >> .gitignore && echo "node_modules" >> .gitignore
```



# Como formatar o arquivo Readme.md
>fontes: 
>[Markdown guide][markdown-guide]
>[Medium @raullesteves][markdown-raul]
>[Dan Bader][bader-readme]
>[Billie Thompson][thompson-readme]
>[Andrés Villanueva][villanueva-readme]

Esse é um arquivo para anotar a formatação do arquivo Readme.md.
Podemos utilizar shields.
Esse arquivo utiliza sintaxe de markdown.


## Shields
>Fonte:
>[Professor José de Assis][assis-shields]

Shields são selos dinamicos de metadados que poderão ser gerados através do site [shields.io][shields-url]. O projeto pode ser consultado no [repositório][repo-shields]

### Exemplos

* Seguidores no github ![GitHub followers][git-followers]
* Seguidores no twitter ![Twitter Follow][twitter-follow]


## Markdown

Funciona de maneira parecida com o HTML.

### Header (h1, h2 e h3)
>usamos hashtags para títulos.

A quantidade de hashtags define a hierarquia do título
```
#
## 
###
```

### Ênfase (b, i e ~~riscado~~)

```
*itálico*
_itálico_ 

**negrito**
__negrito__

~~riscado~~

**_negrito e itálico_**
```

### Lista ordenada (ol)

```
1. Um ponto
2. Dois ponto
3. Três ponto
4. Quatro ponto
```

### Lista não ordenada (ul)

```
- Arroz
- Tomate
- Feijão
Da mesma meira
* Arroz
* Tomate
* Feijão
```

### Links (a href)

Podemos usar assim:
```
[Google] (https://google.com)
[Github] (https://github.com)
```
ou assim:
```
[Google][google-url]
[Github][github-url]

E definir google-url e github-url ao final do arquivo assim (também funciona para endereços de imagens):

<!-- Markdown links & definições de imagens -->
[google-url]: https://google.com
[github-url]: https://github.com
```

### Quotes (blockquote)
>Uma anotação assim.

```
### Quotes (equivalente ao <blockquote>)
>Uma anotação assim
```

### Lista de tarefas

Uma lista como essa:
[X] Exercícios físicos
[X] Buscar documento no cartório
[] Pegar as crianças na escola

É feita dessa maneira:

```
Uma lista como essa:
[X] Exercícios físicos
[X] Buscar documento no cartório
[] Pegar as crianças na escola

É feita dessa maneira:
```

### Um bloco de código

Para mostrar um bloco de código é necessário iniciar com três acentos crase e encerrar com três acentos crase.

```
"```" 
aqui vai o código
"```"
```

### Tabelas (table)

Em markdown temos que basicamente desenhar a tabela, porém existe uma ferramenta que pode facilitar e muito esse trabalho, [gerador][table-gerador].

Uma tabela assim:
|coluna 1 |coluna 2 |coluna 3 |
|---------|:-------:|--------:|
|         |         |         |
|         |         |         |

É feita assim:
```
|coluna 1 |coluna 2 |coluna 3 |
|---------|:-------:|--------:|
|         |         |         |
|         |         |         |
```

Essa linha define o alinhamento da coluna:
```
|---------|:-------:|--------:|
```
```
A esquerda:
|----------|

Centralizado:
|:--------:|

A direita:
|---------:|
```

### Imagens e gifs (img src="caminho")
>Podemos usar a tag html e definir atributos de altura e largura.

A inclusão de imagens funciona com ! como marcador, seguido de [] e (com o caminho)
```
![](/_imagens/barco.png)
```
ou assim:
```
![][barco]

<!-- links -->
[barco]: /_imagens/barco.png
```

### Utilidade do arquivo Readme.md

O arquivo readme orienta o usuário na utilização do repositório, em geral, inicia com o nome do projeto seguido pelos pré-requisitos, maneira de instalação, lista de autores, licença de uso, versões etc



<!-- Markdown Links -->
[learn-gitbranching]: https://learngitbranching.js.org
[markdown-guide]: https://www.markdownguide.org/
[shields-url]: https://shields.io/
[repo-shields]: https://github.com/badges/shields
[table-gerador]: https://www.tablesgenerator.com/markdown_tables
[git-followers]: https://img.shields.io/github/followers/ramosgladson?style=social
[twitter-follow]: https://img.shields.io/twitter/follow/gladsonramos?label=Follow&style=social
[markdown-raul]: https://medium.com/@raullesteves/github-como-fazer-um-readme-md-bonit%C3%A3o-c85c8f154f8
[bader-readme]: https://github.com/dbader/readme-template
[thompson-readme]: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
[villanueva-readme]: https://gist.github.com/Villanuevand/6386899f70346d4580c723232524d35a
[assis-shields]: https://www.youtube.com/watch?v=hQb0I3M2BuQ
