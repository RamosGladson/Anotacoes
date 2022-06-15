<?php

require "Pessoa.php";
require "Programador.php";
include "DisplayA.php";
include "DisplayB.php";

$programador = new Programador("Diego", "diego.com.br", "c#");
//$uma_pessoa->setNome("Diego");
//$uma_pessoa->setSite("diego.com.br");

//echo $uma_pessoa->nome;
DisplayA\menu("A");

echo $programador->getNome();
echo ' ';
echo $programador->getSite();
echo ' ';
echo $programador->getLinguagem();
echo ' ';
echo $programador::ESPECIE;
