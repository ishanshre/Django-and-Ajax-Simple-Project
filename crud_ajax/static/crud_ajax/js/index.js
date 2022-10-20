const postsBox = document.getElementById('posts-box')//get the postbox element using id
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBtn = document.getElementById('end-box')
const postForm = document.getElementById('post-form')
const postTitle = document.getElementById('id_title')
const postBody = document.getElementById('id_body')
const postCsrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(postCsrf, postCsrf[0].value)
const url = window.location.href
// a function for getting csrf token. From docs
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');
// end of csrf token

// function for like and unlike
const likeUnlikePosts = () => {
  const likeUnlikeForms = [...document.getElementsByClassName('like-unlike-forms')]//append like unlike form in list using spread 
  console.log(likeUnlikeForms)
  // add a event listerner on like - unlike button submit
  likeUnlikeForms.forEach(form=> form.addEventListener('submit', e=>{
    e.preventDefault()// prevents from reloading the page
    const clickedId= e.target.getAttribute('data-form-id')//get the custom html attribute
    const clickedBtn = document.getElementById(`like-unlike-${clickedId}`)//get like-unlike button with uniquer post id
    $.ajax({
      type:'POST',
      url:"/like-unlike/",
      data: {
        'csrfmiddlewaretoken':csrftoken,
        'pk':clickedId,

      },
      success: function(response){
        console.log(response)
        //logic for displaying like and unlike button when clicked without reloading the page
        clickedBtn.textContent = response.liked ? `Unlike (${response.like_count})` :`Like(${response.like_count})`
      },
      error: function(error){
        console.log(error)
      }
    })
  }))
}
let visible = 3 // visible number of post to the user
const getData = () => {
  $.ajax({
    type:'GET',
    url: `/posts-data/${visible}`,
    success: function(response){
      console.log(response)
      const data = response.data;
      setTimeout(() => {
        spinnerBox.classList.add('not-visible');
        console.log(data);
        data.forEach(el => {
            postsBox.innerHTML += `
            <div class="card mt-3">
            <div class="card-header">
              ${el.title}
            </div>
            <div class="card-body">
              <p class="card-text">${el.body}</p>
              <a href="${url}post/${el.slug}" class="btn btn-outline-secondary">Detail</a>
              <form class='like-unlike-forms' data-form-id=${el.id}>

              <button class="btn btn-outline-primary" id="like-unlike-${el.id}">${el.liked ? `Unlike (${el.like_count})` :`Like(${el.like_count})`}</button>
              </form>
            </div>
            <div class="card-footer text-muted">
              ${el.created}
            </div>
          </div>
            `
        });
        likeUnlikePosts()// calling likeunline function
      }, 100)
      console.log(response.size)
      if (response.size === 0){
        endBtn.textContent = 'No post have been added yet...'
      }
      else if (response.size <= visible){
        loadBtn.classList.add('not-visible')
        endBtn.textContent = 'No post to display'
      }
    },
    error: function(error) {
        console.log('error',error)
    }
  });
}
// load more logic

loadBtn.addEventListener('click', ()=>{
  spinnerBox.classList.remove('not-visible')
  visible += 3
  getData()
})

postForm.addEventListener('submit', e=>{
  e.preventDefault()
  $.ajax({
    type:'POST',
    url:'',
    data: {
      'csrfmiddlewaretoken':postCsrf[0].value,
      'title':postTitle.value,
      'body':postBody.value,
    },
    success: function(response){
      postsBox.insertAdjacentHTML('afterbegin', `
      <div class="card mt-3">
      <div class="card-header">
        ${response.title}
      </div>
      <div class="card-body">
        <p class="card-text">${response.body}</p>
        <a href="#" class="btn btn-outline-secondary">Detail</a>
        <form class='like-unlike-forms' data-form-id=${response.id}>

        <button class="btn btn-outline-primary" id="like-unlike-${response.id}">Like</button>
        </form>
      </div>
      <div class="card-footer text-muted">
        ${response.created}
      </div>
    </div>
      `)
      
      likeUnlikePosts()
      postForm.reset()
      $('#addPostModal').modal('hide');
      handleAlerts('success','New Post Added')
     
      
    },
    error: function(error){
      console.log(error);
      handleAlerts('danger', 'No Post added')
    }
  });
});

getData()

