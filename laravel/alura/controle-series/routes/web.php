<?php

use App\Http\Controllers\SeriesController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});


Route::get('/ola', function(){
    echo 'olá mundo';
});


Route::resource('/series', SeriesController::class);
