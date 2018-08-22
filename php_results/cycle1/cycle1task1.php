<?php

for ($i=1; $i < strlen($input); $i++) {
	if ($input[$i] == $input[0]) {
		$input[$i] = '*';
	}
}

echo $input;
