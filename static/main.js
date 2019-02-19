function submit_message(message) {

    $.post( "/send_message", {
        message: message,
    }, handle_response);
    
    function handle_response(data) {
      // append the bot repsonse to the div
      $('.chat-container').append(`
            <div class="chat-message bot-message">
                ${data.message}
            </div>
      `)
      /*
      $('.chatbot-img').append(`
            <div  class="bot-img">
                <img src="static/img/bot.gif" /> 
            </div>
      `)*/
      //$('<img class="bot-img" src="static/img/bot.gif" />').prependTo('.bot-message');
      // remove the loading indicator
      $( "#loading" ).remove();
    }
}


$('#target').on('submit', function(e){
    e.preventDefault();
    const input_message = $('#input_message').val()
    // return if the user does not enter any text
    if (!input_message) {
      return
    }
    
    $('.chat-container').append(`
        <div class="chat-message human-message">
            ${input_message}
        </div>
    `)
    
    // loading 
    $('.chat-container').append(`
        <div class="chat-message text-center bot-message" id="loading">
            <b>...</b>
        </div>
    `)
    
    // clear the text input 
    $('#input_message').val('')
    
    // send the message
    submit_message(input_message)
});

// Get a reference to the div you want to auto-scroll.
var someElement = document.querySelector('.chat-container');
// Create an observer and pass it a callback.
var observer = new MutationObserver(scrollToBottom);
// Tell it to look for new children that will change the height.
var config = {childList: true};
observer.observe(someElement, config);
function scrollToBottom() {
    someElement.scrollTop = someElement.scrollHeight;
  }