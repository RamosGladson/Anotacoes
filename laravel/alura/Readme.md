# Laravel na Alura


# Controller  

É possível gerar um controler com o comando  
>php artisan make:controller NomeDoController --resource 


O parametro Request captura a requisição  
```
$request->get('id') captura a requisição id passada na uri, ex:  
```

http://localhost:8000/series?id=1
```
public function index(Request $request){
    $id = $request->get('id');
    [...]
}

return response($string, 200, []);                                      | [] cabecalho
return response($lista);                                                | retorna um json com a lista
return response('', 302, ['location' => 'https://google.com']);         | resposta de redirecionamento
return redirect('https://google.com')                                   | resposta de redirecionamento
$request->url()                                                         | captura a url
$request->method()                                                      | captura o método
$request->input()                                                       | input de um formulário



public function index(Request $request)
{

    $id = $request->get('id');
    $series = [
        'Punisher',
        'Lost',
        'Grey\'s Anatomy'
    ];

    return view('listar-series', compact('series'));
    ou
    return view ('listar-series')->with('series', $series);
}
```

# View

_Template_
1. Dentro da pasta views, criar pasta templates  
2. criar arquivo template.blade.php
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    @yield('content')
</body>
</html>
```
3. Criar pasta para componente, por exemplo views/series
4. Criar arquivo index.blade.php
```
@extends('templates.template')

@section('content')

<h1 class='text-center'>Séries</h1>

<ul>
    @foreach($series as $serie)
        <li>{{$serie}}</li>
    @endforeach
</ul>

@endsection
```


_Componentes_
1. Dentro da pasta views, criar pasta components
2. Criar arquivo layout.blade.php
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ $title }}</title>
</head>
<body>
<h1>{{ $title }}</h1>

{{ $slot }}

</body>
</html>
```
3. Utilização do componente em outro arquivo
```
<x-layout title='Séries'>
    <ul>
        @foreach ($series as $serie)
        <li> {{ $serie }} </li>
        @endforeach
    </ul>


</x-layout>
```
4. Criação de componente pelo php artisan
```
php artisan make:component Layout
```
Isso cria uma classe dentro de app\View\Componets e um componente dentro de resources\views\components, 
perimitindo assim a manipulação e validação de parametros.



Controller:
```
    public function index(Request $request)
    {

        $id = $request->get('id');
        $series = [
            'Punisher',
            'Lost',
            'Grey\'s Anatomy'
        ];

        return view("series.index", compact('series'));
    }
```

## Webpack
>Manipula arquivos de front-end

_Laravel Mix_
>Define os passos de consttrução do webpack

* Instalação:
1. 
```
npm install laravel-mix --save-dev
```
2. Crie um arquivo na raiz do projeto  
webpack.mix.cjs
```
const mix = require('laravel-mix');
```

_Bootstrap_
1. Instalar bootstrap
npm install bootstrap

2. Renomear resources\css\app.css para app.scss

3. Importar o bootstrap
@import "~bootstrap/scss/bootstrap";

4. Editar webpack.mix.cjs
```
const mix = require('laravel-mix');

mix
.sass('resources/css/app.scss', 'public/css')
```

5. Editar resources/js/app.js
```
import './bootstrap.js';
```

6. Adicionar mix em package.json
```
{
    "private": true,
    "scripts": {
        "dev": "vite",
        "build": "vite build",
        "mix": "mix"
    },
    "devDependencies": {
        // Dependências aqui
    }
}
```

7. Rodar mix 2X
```
npm run mix
```

8. Add ao head
```
    <link rel="stylesheet" href="{{ asset('css/app.css')}}">
```

9. Remover de resources/js arquivos app.js e bootstrap.js

### Notações

```
@foreach ($series as $serie)
<li> {{ $serie }} </li>
@endforeach

igual a:
<?php foreach ($series as $serie); ?>
<li><?= $serie; ?></li>
<?php endforeach; ?>


@unless (Auth::check())                     | mesmo que if com negação
    <p>Não está logado</p>
@endunless

@isset($varialve)                           | not null
@empty($variavel)                           | verifica se está vazia

@{{ $nome }}                                | ignora os caracteres especiais e exibe {{ $nome }} na tela

```



# Estrutura de pastas
vendor                              | pacotes instalados
storage                             | pasta de armazenamento de imagens OU aploads
routes                              | rotas
resources                           | recursos relacionados ao front-end
public                              | acessível pelo servidor web
lang                                | tradução
database                            | config do banco de dados
config                              | configurações
bootstrap                           | bootstrap de inicio
app                                 | nosso código

# Database

## Migrations
> Versionador de banco de dados

```
php artisan make:migration          | Cria uma migração já com a criação da tabela series
```

## ORM

```
php artisan make:model Serie        | Cria um ORM para tabela series

Arquivo adicionado em app/Models/Serie.php

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Serie extends Model
{
    use HasFactory;

    protected $table = 'seriado';   | Não obrigatório, por padrão seria mapeado a tabela series
    
    public $timestamps = false;     | Caso não queira guardar timestamps
}
```

### Query Scopes

```
public function index(Request $request)
    {        
        $series = Serie::query()->orderBy('nome')->get();   | Ordena por ordem alfabetica
        $series = Serie::all();                             | Retorna colection com todos

        return view("series.index", compact('series'));
    }

public function store(Request $request)
    {

        $serie = new Serie();
        $serie->nome = $request->input('nome');
        $serie->save(); 

        return redirect('/series');


    }
```

# Comandos
```
composer create-project laravel/laravel controle-series
php artisan lang:publish    
php artisan serve --host=127.0.0.1 --port=12000       
php artisan make:controller SeriesController --resource             | cria controller já com crud   
php artisan make:component Layout 
php artisan make:model Serie                                        | cria um orm para tabela series                     
```

> Ao baixar projeto um projeto laravel

```
composer install                | Instalará todas as dependências listadas no arquivo composer.json.
cp .env.example .env            
php artisan key:generate        | Isso irá atualizar o arquivo .env com uma chave de aplicativo aleatória.
php artisan migrate             | Isso criará as tabelas definidas pelas migrações no banco de dados.
php artisan serve               | Isso iniciará um servidor de desenvolvimento local na porta padrão 8000.
```