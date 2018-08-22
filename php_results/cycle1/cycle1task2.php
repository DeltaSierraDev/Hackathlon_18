<?php
$input = 'Hello world!';
$input = strtolower(preg_replace('/[^a-z]+/i', '', $input));
$array = str_split($input);
$countArray = array_count_values($array);
ksort($countArray);
foreach ($countArray as $key => $value) {
	echo $key.':'.$value.'<br>';
}
