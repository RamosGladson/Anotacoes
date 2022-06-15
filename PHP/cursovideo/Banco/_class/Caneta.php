<?php


class Caneta{
    private $modelo;
    private $cor;
    private $ponta;
    private $carga;
    private $tampada;
    
    function __construct($modelo, $cor, $ponta, $carga) {    
        $this->modelo = $modelo;
        $this->cor = $cor;
        $this->ponta = $ponta;
        $this->carga = $carga;
        $this->tampada = true;
    }


    function setModelo($modelo){
        $this->modelo = $modelo;
    }
    function setCor($cor){
        $this->cor = $cor;        
    }
    function setPonta($ponta){
        $this->ponta = $ponta;        
    }
    function setCarga(){
        return $this->carga;
    }
    function getModelo(){
        return $this->modelo;
    }
    function gettCor(){
        return $this->cor;        
    }
    function getPonta(){
        return $this->ponta;        
    }
    function getCarga(){
        return $this->carga;
    }
    function tampar(){
        $this->tampada = true;
    }
    function destampar(){
        $this->tampada = false;
    }

    function rabiscar(){
        if ($this->tampada == false){
            echo "Rabiscar";
        } else {
            echo "caneta está tampada, não pode rabiscar";
        }    
    }
    

}