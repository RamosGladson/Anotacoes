<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ModelBook extends Model
{
    //use HasFactory;
    protected $table='book'; //referencia a tabela book detro do banco relacionado em .env
    protected $fillable=['title', 'id_user', 'pages', 'price'];

    public function relUsers(){
        return $this->hasOne('App\Models\User', 'id', 'id_user');
    }
}
