# Docker
>Comandos docker
```
docker exec -it [nome_container] [comando]

docker run [options] image:tag [command] [args]     // modo attach por default


[options]
--network minha_rede                      // utiliza a rede minha_rede
-p 8080:80                                // mapeia porta 8080 do host apontando para porta exposta 80 do container
--expose 80                               // apena expoe a porta 80 do container
-d                                        // roda container em modo detach, não bloqueia o terminal
-i                                        // modo interativo
-it                                       // abre um terminal
-v /app/resources                         // volume anonimo
-v nome:/app/temp                         // named volume
-v pasta/host:/container                  // bind volume, mapeia pasta do host ao container para persistencia de dados
-v pasta/host:/container:ro               // bind volume, mapeia pasta do host ao container para persistencia de dados [read only]
-v "%cd%":/app                            // monta pasta atual do hosto na pasta /app do container
--env VAR1=value1 --env VAR2=value2       // informa as variaveis de ambiente
--dns 8.8.8.8 --dns 8.8.4.4               // fornece um servidor dns ao container                       

docker attach [nome container]            // estabelece modo attach ao container
docker logs -f [nome container]           // ecoa como attach, porem não mata o container ao sair

docker start [nome container]             // modo detach por default
docker start -a [nome container]          // inicia com modo attach


docker cp [origem] [destino]

eg.
docker cp pasta/. container_name:/pasta   // copia do host para container
docker cp container_name:/pasta/. pasta/  // copia do container para host

```

## Docker Build
>Customiza uma imagem a partir de outra.
[comandos][comandos-url]
```
Comandos:                                 // 
docker images                             // mostra as imagens
docker rmi                                // remove imagem
docker image prune                        // remove imagens nao utilizadas
docker image pull                         // puxa uma imagen do repositorio
docker image push                         // envia uma imagem para o repositorio
docker image rm [id]                      // remove imagens pelo id
docker tab [nome_imagem_origem:tag] [nome_imagem_destino:tag]   // clona imagem

docker push [repositorio/nome:tag]        // envia imagem para docker hub

docker login                              // loga no docker hub

docker build [options]

[options]
--file, -f                                // especifica a diretorio e arquivo Dockerfile
--label                                   // meta data para imagem, utilizado para filtrar a imagem
--tag, -t                                 // coloca um nome para imagem ou nome:tag  nginx:meusite

```

## Docker network
>
```
host.docker.internal                      // aponta para o host do container

docker network create nome_rede           // cria uma rede para comunicação entre os containers
docker network create --driver overlay nome_rede  // rede do tipo overlay
docker network create -d overlay nome_rede        // outra maneira de declarar a linha acima

*tipos de driver para rede

bridge                                    // cria uma rede nat
host                                      // cria uma rede bridge
overlay                                   // rede entre hosts, funciona com Swarm
macvlan                                   // permite customizar MAC address em um container
none                                      // desabilita as redes
Third-party plugins                       // 
```

## Arquivo Dockerfile:                         [dockerfile][dockerfile-url]
>Arquivo para construcao de imagem docker
```
# comentario
# minha imagem docker

FROM ubuntu:18.04                          // tudo começa com um FROM, nesse caso baixa a imagem do ubuntu 18 LTS

WORKDIR /var/www/html                      // diretorio de entrada para os comando RUN CMD ENTRYPOIND COPY ADD

RUN [comandos]                             // pode ser executada ou nao, uma ou mais vezes

eg.
RUN apt-get update -y && apt-get upgrade -y
RUN echo "minhamaquina" > /etc/hostname
RUN echo "192.168.0.3  meuad.local" >> /etc/hosts

CMD                                         // faz praticamente a mesma coisa que RUN, mas apenas o ultimo é executado (na criação do container), caso outro comando seja passado na criação do container, esse comando não é executado

ENTRYPOINT                                  // faz praticamente a mesma coisa que CMD, porem execulta todos, nao apenas o ultimo

ADD arquivo-host arquivo-host-no-container  // transfere um arquivo do host para o container
* A instrução ADD também tem alguns efeitos interessantes, como: caso o arquivo que esteja sendo passado seja um arquivo de extensão tar, ele fará a descompressão automaticamente, além do fato já mencionado de poder fazer download de arquivos por URLS. *

COPY arquivo-host arquivo-host-no-container // transfere um arquivo do host para o container
* A instrução COPY, permite apenas a passagem de arquivos ou diretórios, diferente do ADD, que permite downloads *


ARG QUAL_QUER_COISA                         // funciona como uma env  "--build-arg QUAL_QUER_COISA=minhamaquina"

RUN echo $QUAL_QUER_COISA > /etc/hostname   // insere conteudo de QUAL_QUER_COISA ao arquivo /etc/hotname


ENV POSTGRES_PASSWORD=mysecretpassword      // passagem de variaveis env

                                            // somente volumes anonimos podem ser criados com Dockerfile
VOLUME /myvol                               // mapeia volume anonimo
VOLUME [ "/app/node_module" ]               // volume anonimo

```
### Arquivo .dockerignore
>Informa quais arquivos não deveriam ser copiados para a imagem docker

```
Dockerfile                                  //não copia o arquivo Dockerfile
.git

```


## Docker Compose
>Seta um ambiente para trabalhar com mais de um container

### Arquivo docker-compose.yml para wordpress  
>[compatibilidade][compatibilidade-url]

```
version: '3.8'                              // matriz de compatibilidade

services:
  db:                                       // nomeia o serviço
    image: mariadb                          // seleciona uma imagem, caso não tenha uma imagem local, baixa do docker hub
    volumes:                                // utilizacao de volumes eh opcional, serve para persistencia de dados
      - /c/tmp/banco:/var/lib/mysql         // cria um volume no host e aponta para pasta /var/lib/mysql do container
      - ./app:/var/www/html                 // usa caminho relativo
    restart: always                         // reinicia o container sempre que travar
    environment:
      MYSQL_ROOT_PASSWORD: p@ssw0rd         // seta variavel env
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    
  wordpress:
    depends_on:                             // só inicia após container db estar ok
      - db
    image: wordpress
    container_name: mongodb                 // nomeia container
    volumes:
      - /c/tmp/wordpress:/var/www/html
      - volume1:/app                        // volume tipo named
    ports:
      - "8080:80"                           // mapeia a porta 8080 do host apontando para porta 80 do container
    restart: always
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

  frontend
    build: ./frontend                      // especifica caminho Dockerfile para construção de imagem docker

volumes:                                   // cria volumes
  data:
  logs:
  backend:

networks:                                  // cria redes | desnecessário
  mvc:
```

### Arquivo docker-compose.yml para wordpress com .env
[compatibilidade][compatibilidade-url]

```
version: '3.8'                              // matriz de compatibilidade

services:
  db:                                       // nomeia o serviço
    image: mariadb                          // seleciona uma imagem, caso não tenha uma imagem local, baixa do docker hub
    volumes:
      - /c/tmp/banco:/var/lib/mysql         // cria um volume no host e aponta para pasta /var/lib/mysql do container
    restart: always                         // reinicia o container sempre que travar
    environment:
      MYSQL_ROOT_PASSWORD: ${SQL_PASSWD}    // seta variavel env
      MYSQL_DATABASE: ${SQL_DATABASE}
      MYSQL_USER: ${SQL_USER}
      MYSQL_PASSWORD: ${SQL_PASSWORD}
    
  wordpress:
    depends_on:                             // só inicia após container db estar ok
      - db
    image: wordpress
    volumes:
      - /c/tmp/wp:/var/www/html
    ports:
      - "8080:80"                           // mapeia a porta 8080 do host apontando para porta 80 do container
    restart: always
    environment:
      WORDPRESS_DB_HOST: ${DB_HOST}
      WORDPRESS_DB_USER: ${DB_USER}
      WORDPRESS_DB_PASSWORD: ${DB_PASSWORD}
      WORDPRESS_DB_NAME: ${DB_NAME}

```

### Arquivo .env
```
SQL_PASSWD=p@ssw0rd
SQL_DATABASE=wordpress
SQL_USER=wordpress
SQL_PASSWORD=wordpress

DB_HOST=db
DB_USER=wordpress
DB_PASSWORD=wordpress
DB_NAME=wordpress
```
>docker compose up -d


<!-- links -->
[dockerfile-url]: https://www.alura.com.br/artigos/desvendando-o-dockerfile?gclid=Cj0KCQjwwJuVBhCAARIsAOPwGATIUMSQUUMZtDNGMWCFJ6BCSXp_RFKGScAsoE9jYlQgPEsHd_PMLi4aAiWoEALw_wcB
[comandos-url]: https://docs.docker.com/engine/reference/commandline/docker/
[compatibilidade-url]: https://docs.docker.com/compose/compose-file/compose-versioning/