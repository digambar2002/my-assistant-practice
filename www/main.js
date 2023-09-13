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
});