<?php

namespace App\Http\Controllers;

use App\Http\Requests\BookRequest;
use App\Models\ModelBook;
use App\Models\User;

class BookController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $books=ModelBook::paginate(10); // busca 10 livros por página
        return view('index', compact('books')); //devolve index.blade.php passando a variável books
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        $users=ModelBook::all();
        return view('create', compact('users'));
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(BookRequest $request)
    {
        $cad=ModelBook::create([
            'title'=>$request->title,
            'pages'=>$request->pages,
            'price'=>$request->price,
            'id_user'=>$request->id_user
        ]);
        if($cad){
            return redirect('books');
        }
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $book=ModelBook::find($id);
        return view('show', compact('book'));
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        $book=ModelBook::find($id);
        $users=ModelBook::all();
        return view('create', compact('book', 'users'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(BookRequest $request, string $id)
    {
        ModelBook::where(['id' => $id])->update([
                'title'=>$request->title,
                'pages'=>$request->pages,
                'price'=>$request->price,
                'id_user'=>$request->id_user
        ]);
        return redirect('books');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        $del=ModelBook::destroy($id);
        return($del)?'sim':'nao';
    }
}
