<?php



class Programador extends Pessoa{
    protected $linguagem;
    

    public function __construct($tmpNome, $tmpSite, $tmpLinguagem)
    {
        $this->setNome($tmpNome);
        $this->setSite($tmpSite);
        $this->setLinguagem($tmpLinguagem);

        echo "<br>Objeto ".__CLASS__." foi instanciado<br>";
    }

    public function setLinguagem($nLinguagem){
        $this->linguagem=$nLinguagem;
    }
    public function getLinguagem(){
        return $this->linguagem;
    }

}

?>