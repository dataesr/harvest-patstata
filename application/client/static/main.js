$('#all').on('click', function() {
    $.ajax({
        url: '/inpi',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        method: 'GET'
    })
    .done(res => {
        $('#res_inpi').html(res.data);
    })
    .fail(err => {
        console.log(err)
    });
});