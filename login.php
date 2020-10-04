<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dabella1";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn -> connect_error) {
    die("Connection failed: " . $conn -> connect_error);
}

$sql = "SELECT * FROM accounts WHERE u_name='$_POST[username]' AND p_word='$_POST[password]'";
if($result = mysqli_query($conn, $sql)){
    if(mysqli_num_rows($result) > 0){
        echo "Logged in Sucessfully";
        echo "<br/>";
        echo "<a href='index.html'>Go Back to Log in screen</a>";
        mysqli_free_result($result);
    } else {
        echo "Error: Unsuccessful Login";
        echo "<br/>";
        echo "<a href='login.html'>Go Back to Home Screen</a>";
    }
}