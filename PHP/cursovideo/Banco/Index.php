<!DOCTYPE html5>
<html>

<body>
<?php

require "_class/Caneta.php";

$bic = new Caneta("bic", "azul", "0.5", 80);
$bic->destampar();
$bic->rabiscar();
$bic->tampar();
$bic->rabiscar();

?>

</body>
</html>