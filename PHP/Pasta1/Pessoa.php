<?php

use LDAP\Result;

    class Pessoa{
        protected $nome;
        protected $site;
        const ESPECIE = "Humana";


        public function __construct($name, $portal)        
        {
                $this->setNome($name);
                $this->setSite($portal);

        }

        public function getNome(){
            return $this->nome;
        }

        public function getSite(){
            return $this->site;
        }

        public function setNome($novoNome){
            $this->nome=$novoNome;
        }
        
        public function setSite($novoSite){
            $this->site=$novoSite;
        }

        
        
    }

