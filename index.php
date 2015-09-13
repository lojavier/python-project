<!DOCTYPE html>
<html>
<head>
	<title>SW FARE REDUCER</title>
	<meta charset="utf-8">
	<link href="css/style.css" rel='stylesheet' type='text/css' />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>

	<script type="text/javascript">
		function newFlight()
		{
			document.swform.action = "newflight.php";
			document.getElementById('swform').submit();
		}
		function updatePrice()
		{
			document.swform.action = "updateprice.php";
			document.getElementById('swform').submit();
		}
		function removeFlight()
		{
			document.swform.action = "removeflight.php";
			document.getElementById('swform').submit();
		}
	</script>

	<!--webfonts-->
	<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700,800' rel='stylesheet' type='text.css'/>
	<!--//webfonts-->
</head>
 
<body>
	<div class="main">
		<form method="POST" name="swform">
    		<h1><span>SW</span> <lable> FARE REDUCER </lable> </h1>
  			<div class="inset">
	  			<p>
   	 				<input name="CONFIRMATION_NUM" style="text-transform:uppercase" type="text" placeholder="CONFIRMATION #" maxlength="6" required/>
				</p>
  				<p>
				    <input name="FIRST_NAME" style="text-transform:uppercase" type="text" placeholder="FIRST NAME" required/>
  				</p>
  				<p>
				    <input name="LAST_NAME" style="text-transform:uppercase" type="text" placeholder="LAST NAME" required/>
  				</p>
				  <!-- <p>
				    <input type="checkbox" name="remember" id="remember">
				    <label for="remember">Remember me for 14 days</label>
				  </p> -->
 			</div>
 	 
			<p class="p-container">
				<input type="submit" value="NEW FLIGHT" onclick="newFlight();">
			</p>
			<p class="p-container">
				<input type="submit" value="UPDATE PRICE" onclick="updatePrice();">
			</p>
			<p class="p-container">
				<input type="submit" value="REMOVE FLIGHT" onclick="removeFlight();">
			</p>
		</form>
	</div>

	<?php
	// http://stackoverflow.com/questions/14047979/executing-python-script-in-php-and-exchanging-data-between-the-two
	// $command = "/usr/bin/python sw_flight_validator.py 8ABYGC Lorenzo Javier text 9252007284 11 POINTS 2989";
	$command = escapeshellcmd('/usr/bin/python sw_flight_validator.py 8ABYGC Lorenzo Javier text 9252007284 11 POINTS 2989 2>&1');
	$output = shell_exec($command);
	echo $output;

	// ob_start();
	// passthru('/usr/bin/python sw_flight_validator.py 8ABYGC Lorenzo Javier text 9252007284 11 POINTS 2989 2>&1');
	// $output = ob_get_clean(); 
	// echo $output;

	// echo exec($command);
	// echo $output;

	// $file = popen($command,"r");
	// // //some code to be executed

	// while( !feof( $file ) )
	// {
	// 	echo fread($file, 99999);
	// 	flush();
	// 	ob_flush();
	// }
	// pclose($file);

	?>
</body>
</html>