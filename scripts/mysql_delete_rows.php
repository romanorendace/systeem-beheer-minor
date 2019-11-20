<?php
$servername = "localhost";
$username = "check";
$password = "rDEetGxq82DCE";
$dbname = "check";

try {
    # open connection
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    # delete row to keep row count 80-10
    $del = "DELETE FROM check.log WHERE id > 90";
    $conn->query($del);
    
    # close connection
    $conn = null;
    }

catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }


?> 
