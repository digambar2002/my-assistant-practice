$(document).ready(function () {


    // Animating Text    
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",

        },

        out: {
            effect: "bounceOut",
        }
    });

    // Siri wave configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        speed: "0.30",
        amplitude: "1",
        autostart: true,

    });

    // Fade up Siri text animation
    $(".siri-message").textillate({
        selector: '.s-message',
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },

        out: {
            effect: "fadeOutUp",
            sync: true,
        }
    });


    // ---------------------------------------------------------- Day 4 --------------------------------------------------

    // When Click on BOB, it hide and display spectrum
    $("#MicBtn").click(function () {

        eel.playAssisatntSound()
        $("#Oval").attr("hidden", true);
        $("#Siriwave").attr("hidden", false);

    });





});