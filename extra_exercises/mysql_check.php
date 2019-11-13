<?php
$servername = "localhost";
$username = "check";
$password = "rDEetGxq82DCE";
$dbname = "check";

try {
    # open connection
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    # get last row
    $sql = "SELECT * FROM check.log ORDER BY id DESC LIMIT 1";
    $result = $conn->query($sql);
   
    if($row = $result->fetch()) {
        echo '<p>';
        echo $row["text"];
        echo '</p>';
    }

    # delete row to keep row count 80-10
    $del = "DELETE FROM check.log WHERE id > 90";
    $conn->query($sql);
    
    # close connection
    $conn = null;
    }

catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }


?> 