<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
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
