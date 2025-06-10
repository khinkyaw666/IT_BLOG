<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $message = strtolower($_POST["message"]);
    
    // Call Python AI chatbot API
    $python_api_url = "http://127.0.0.1:5000/chat";
    $response = file_get_contents($python_api_url . "?message=" . urlencode($message));
    
    echo json_decode($response)->response;
}
?>
