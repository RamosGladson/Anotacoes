# Laravel
>[Documentação][laravel-doc]  |
>|  [Curso CRUD YT][crud-yt]


### MVC

**Model**

class ModelBook extends Model
{
    //use HasFactory;
    protected $table='book';                                        || referencia a tabela book detro do banco relacionado em .env
    protected $fillable=['title', 'id_user', 'pages', 'price'];

    public function relUsers(){
        return $this->hasOne('App\Models\User', 'id', 'id_user');
    }
}


**View**
>resources\view
Interface de interação com o usuário
** Padrão de nomenclatura:
nome.blade.php

_Template_
1. Criar pasta templates dentro de resources\view
2. Gerar um template dentro de body dar um nome a esse template:
```
[...]
<body>
    @yield('content')
[...]
```
3. Dentro da view a ser exibida:
```
@extends('templates.template')                  || Referencia ao arquivo template

@section('content')                             || Insere conteúdo da seção dentro do template para exibição

<h1>CRUD</h1>
<hr>

@endsection                                     || Finaliza a inserção do conteúdo

```
3.1 CSRF
>cross-site request forgery

```
<form method="POST" action="/profile">
    @csrf                                       || Previne CSRF

```

_foreach_

```
@foreach($books as $book)
    @php
        $user=$books->find($books->id)->relUsers;
    @endphp
    <tr>
        [...]
    </tr>
@endforeach


```

_required_
>obriga o usuário a preencher o campo

```
    <h1 class='text-center'>Cadastrar</h1>
    <hr>

    <div class='col-8 m-auto'>
        <form name='formCad' id='formCad' method='post' action='{{url("books")}}'>
            @csrf
            <input class='form-control' type='text' name='title'  id='title' placeholder='Título:' required></br>       || exemplo required
            <select class='form-control' name='id_user' id='id_user' required>
                <option value=''>Autor</option>
                @foreach($users as $user)
                <option value='{{$user->id}}'>{{$user->name}}</option>
                @endforeach

[...]

```


**Rotas**
>[Handler][handler]  |
>|  routes\web.php
```
Route::get('/books', function () {
    return view('index'); // aponta para resources\views\index.blade.php
});

ou

use App\Http\Controllers\BookController;
Route::resource('books', BookController::class);            || uri/books aponta para BookController

```

**Controller**
```
-----------------------------------------
class BookController extends Controller
{
    private $objUser;                                       || declara objeto para receber dados do banco
    private $objBook;

    public function __construct(){
        $this->objUser=new User();                          || conecta entidade com acesso ao banco
        $this->objBook=new ModelBook();
    }

        /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $books=$this->objBook->all();                       || busca todos os livros
        //$books=$this->objBook->all()->sortBy('title');    || busca todos os livros e ordena por titulo
        //$books=$this->objBook->all()->sortByDesc('title');|| busca todos os livros e inverte ordem por titulo
        return view('index', compact('books'));             || devolve index.blade.php passando a variável books
    }
[...]

    public function store(Request $request)
    {
        $cad=$this->objBook->create([
            'title'=>$request->title,
            'pages'=>$request->pages,
            'price'=>$request->price,
            'id_user'=>$request->id_user
        ]);
        if($cad){
            return redirect('books');                       || redireciona para /books em web.php
        }
    }
}
-----------------------------------------
```

** Metodos PUT, PATCH e DELETE com formulario
>[Form Method Spoofing][spoofing-method]  |
>|  Não há suporte para put, patch e delete em formularios html, a notação @method é necessária confomre exemplo abaixo:

```
<form action="/example" method="POST">
    @method('PUT')
    @csrf
</form>
```

_Metodo delete_
1. Criar pasta para java script dentro de public/assets/js

```
(function(win, doc){
    'use strict';

    function confirmDel(event){
        event.preventDefault();
        let token = doc.getElementsByName('_token')[0].value;
        if(confirm('Deseja excluir?')){
            let ajax = new XMLHttpRequest();
            ajax.open('DELETE',event.target.parentNode.href);
            ajax.setRequestHeader('X-CSRF-TOKEN', token)
            ajax.onreadystatechange=function(){
                console.log("deu certo")
                if(ajax.readyState === 4 && ajax.status === 200){
                    win.location.href='books';
                }
            }
            ajax.send();
        }else{
            return false;
        }
    }

    if(doc.querySelector('.js-del')){
        let btn=doc.querySelectorAll('.js-del');
        for(let i=0; i<btn.length; i++){
            btn[i].addEventListener('click',confirmDel,false);
        }
    }


})(window, document)
```
2. Em index.blade.pjp, acima da tabela adicionar @csrf

3. Adicionar url ao botão
```
<a href='{{url("books/$book->id")}}'>
<button class="btn btn-danger">Deletar</button>
</a>
```
4. BookController
```
public function destroy(string $id)
{
    $del=$this->objBook->destroy($id);
    return($del)?'sim':'nao';
}
```



**Request**
>É possível criar regras de requisições

```
php artisan make:request BookRequest                        || cria arquivo de validação de requisições


class BookRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'title'=>'required',
            'pages'=>'required|numeric'
        ];
    }
}


```
_Validação_
>[Regras de validação][validation-rules]

BookController
``` 
use App\Http\Requests\BookRequest;                            || adicionar BookRequest

    public function store(BookRequest $request)
    {
        $cad=$this->objBook->create([
            'title'=>$request->title,
            'pages'=>$request->pages,
            'price'=>$request->price,
            'id_user'=>$request->id_user
        ]);
        if($cad){
            return redirect('books');
        }
    }
```

_Linguagem_
>[Laravel language][laravel-language]  |
>|  [Laravel pt-BR][laravel-pt-br]  |
>|  [Laravel demais locais][laravel-demais]

```
php artisan lang:publish
composer require lucascudo/laravel-pt-br-localization --dev
php artisan vendor:publish --tag=laravel-pt-br-localization

// Altere Linha (aproximadamente) 85 do arquivo config/app.php para:
'locale' => 'pt_BR'
ou
    'locale' => env('APP_LOCALE', 'en'),        || nesse caso, vai utilizar o inglês caso não esteja especificado no arquivo .env
e alterar APP_LOCALE no arquivo .env

```
ou
```
php artisan lang:publish
fazer o download
copiar a pasta da linguagem em lang
// Altere Linha (aproximadamente) 85 do arquivo config/app.php para:
'locale' => 'nomeDaPasta'
ou
    'locale' => env('APP_LOCALE', 'en'),        || nesse caso, vai utilizar o inglês caso não esteja especificado no arquivo .env
e alterar APP_LOCALE com o nome da pasta no arquivo .env
```

_Mensagens personalizadas_
[Doc]:[mensagens-persolnalizada]

BookRequest
```
    public function messages(): array
    {
        return [
            'title.required' => 'Coloque o título',
            'pages.numeric' => 'Coloque quantidade de páginas em números',
        ];
    }
```

### Config Banco de Dados

.env
```
DB_CONNECTION=mariadb
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=123456
```

config\database.php
```
    'default' => env('DB_CONNECTION', 'mariadb'),

[...]
'engine' => 'InnoDB',
[...]
```

app\Providers\AppServiceProvider
```
use Illuminate\Support\Facades\Schema;

[...]

    public function boot(): void
    {
        Schema::defaultStringLength(191);
    }
```


```
*** mariadb
show variables like "character_set_database";
show variables like "collation_database";
alter database curso collate = 'utf8mb4_unicode_ci';
```

### Comandos

```
composer create-project --prefer-dist laravel/laravel projeto           || cria um projeto
php artisan serve                                                       || inicia um servidor local na porta 8000
php artisan make:controller BookController --resource                   || cria BookController
php artisan make:model ModelBook -m                                     || cria model book e a migration
php artisan migrate                                                     || roda os scripts de banco
php artisan make:request BookRequest                                    || cria arquivo de validação de requisições
php artisan make:seeder BookSeeder                                      || cria o alimentador de banco para testes
php artisan db:seed                                                     || execulta o seed
```


### Requisitos
> Primeiro instalar php e fazer o apontamento da versão instalada na instalação do composer  |
>|  [PHP][php]  |
>|  [COMPOSER][composer]

### Seeder
>Alimenta banco com informações para testes

database/BookSeeder.php
```
use App\Models\ModelBook;

class BookSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(ModelBook $book): void
    {
        $book->create([
            'title'=>'livro um',
            'pages'=>200,
            'price'=>10.59,
            'id_user'=>1
        ]);
        $book->create([
            'title'=>'livro dois',
            'pages'=>300,
            'price'=>30.59,
            'id_user'=>1
        ]);
        $book->create([
            'title'=>'livro três',
            'pages'=>250,
            'price'=>18.59,
            'id_user'=>1
        ]);
    }
}
```
database\DatabaseSeeder
```
class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        $this->call(BookSeeder::class);
    }
}

```

### Paginação
>BookController.php
```
     */
    public function index()
    {
        $books=$this->objBook->paginate(10); // busca 10 livros por página
        return view('index', compact('books')); //devolve index.blade.php passando a variável books
    }

```
index.blade.php
```
[...]
  </tbody>
</table>

{{$books->links()}}                 | cria rodapé com paginação
</div>

@endsection
```


<!-- Markdown Links -->
[laravel-doc]: https://laravel.com/docs/11.x
[crud-yt]: https://www.youtube.com/watch?v=c4v1D2bYD5U&list=PLbnAsJ6zlidsbjXqTWQhbnKibzl69LQar
[handler]: https://laravel.com/docs/11.x/controllers#actions-handled-by-resource-controllers
[php]: https://www.php.net/downloads.php
[composer]: https://getcomposer.org/download/
[validation-rules]: https://laravel.com/docs/11.x/validation#available-validation-rules
[laravel-language]: https://laravel.com/docs/11.x/localization#publishing-the-language-files
[laravel-pt-br]: https://github.com/lucascudo/laravel-pt-BR-localization
[laravel-demais]: https://github.com/Laravel-Lang/lang
[mensagens-persolnalizada]: https://laravel.com/docs/11.x/validation#customizing-the-error-messages
[spoofing-method]: https://laravel.com/docs/11.x/routing#form-method-spoofing