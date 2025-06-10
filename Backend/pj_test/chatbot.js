$(document).ready(function () {
    $("#send-btn").click(function () {
        var userMessage = $("#user-input").val();

        $.ajax({
            url: "chatbot.php",
            type: "POST",
            data: { message: userMessage },
            success: function (response) {
                $("#chat-output").append("<p><strong>You:</strong> " + userMessage + "</p>");
                $("#chat-output").append("<p><strong>Bot:</strong> " + response + "</p>");
                $("#user-input").val("");
            }
        });
    });
});
