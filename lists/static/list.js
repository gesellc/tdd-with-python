window.Superlists = {};
window.Superlists.initialize = function () {
    $('input').on('keypress', function () {
        $('.has-error').hide();
    });
};
