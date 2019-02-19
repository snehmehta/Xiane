function submit_message(message) {

    $.post( "/send_message", {
        message: message,
    }, handle_response);
    
    function handle_response(data) {
      // append the bot repsonse to the div
        if(data.display == 'card'){
          $('.chat-container').append(`
            <div class="card chat-message bot-message" style="width: 18rem;">
            <img class="card-img-top" width="200px" height="200px" src="${data.assets}" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">Details</h5>
                <p class="card-text">${data.message}</p>
            </div>
            </div> 
          `)
      }
      else if(data.display == 'text'){
        $('.chat-container').append(`
              <div class="chat-message bot-message">
                  ${data.message}
              </div>
          `)
          // remove the loading indicator
          $( "#loading" ).remove();
       }
       else if(data.display == 'iframe'){
        $('.chat-container').append(`
            <div class="chat-message bot-message">
<<<<<<< HEAD
              <iframe scrolling="no" src="${data.message}" frameborder="0" style="width: 400px; height: 333px;"></iframe>
=======
              <iframe scrolling="no" src="${data.message}" frameborder="0" style="width: 350px; height: 333px; z-index : 2;"></iframe>
>>>>>>> b008c446193d65749ce075bacb44e361359da5b6
            </div>
      `)
      $( "#loading" ).remove();
    }
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