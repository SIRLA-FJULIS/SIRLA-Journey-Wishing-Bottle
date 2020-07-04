$(document).ready(function(){
$('.like-form').submit(function(event){
    event.preventDefault()
    const post_id = $(this).attr('id')
    const likeText = $(`.like-btn${post_id}`).text()
    const trim = $.trim(likeText)
    const url = $('.like-form').attr('action')
    const likeTotalText = $(`.likes-total${post_id}`).text()
    var trimTotal = parseInt(likeTotalText)

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'post_pk': post_id
        },

        success: function() {
            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8000/serialized/',
                success: function(response){
                    $.each(response, function(index, element){
                        if (post_id == element.id){
                            if  (trim == 'Like'){
                                $(`.like-btn${post_id}`).html('Unlike')
                                trimTotal += 1
                                $(`.likes-total${post_id}`).html(trimTotal+' likes')
                            } else if (trim == 'Unlike'){
                                $(`.like-btn${post_id}`).html('Like')
                                trimTotal -= 1
                                $(`.likes-total${post_id}`).html(trimTotal+' likes')
                            } else {
                                console.log('ups')
                        }
                        }
                    })
                },
                error: function(response){
                    console.log('error')
                }
            })
        },

        error: function(error){
            console.log('error', error)
        }
    })
})}
)