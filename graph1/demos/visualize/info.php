<!DOCTYPE html>
<html>
<body>
<?php
echo $_GET['name'];
$filename = $_GET['name'];
$myfile = fopen("./data/".$filename, "r");
while(!feof($myfile)) {
  echo fgets($myfile) . "<br>";
}
fclose($myfile);
?>
</body>
</html>
