const btnBack = document.getElementById('btn-back')
const btnDelete = document.getElementById('btn-delete')
const btnUpdate = document.getElementById('btn-update')
const btnAuth = document.getElementById('btn-auth')
const postBox = document.getElementById('post-box')
const postTitle = document.getElementById('id_title')
const postBody = document.getElementById('id_body')
const url = window.location.href + 'data/'
const urlUpdate = window.location.href + 'update/'
const urlDelete = window.location.href + 'delete/'

const formUpdate = document.getElementById('update-form')
const formDelete = document.getElementById('delete-form')
const postUpdateCsrf = document.getElementsByName('csrfmiddlewaretoken')


btnBack.addEventListener('click', () => {
    history.back();
})


$.ajax({
    type: 'GET',
    url: url,
    success: function (response) {
        console.log(response);
        const data = response.data;
        if (data.logged_in !== data.author){
            console.log('different');
            btnAuth.classList.add('not-visible')
        } else {
            console.log('same');
        }
        postBox.innerHTML += `
        <div class="card" style="background-color: rgb(236, 236, 236);">
        <img src="..." class="card-img-top" alt="...">
        <div class="card-body">
          <h1 class="card-title" id="post-detail-title">${data.title}</h1>
          <p><strong>By ${data.author}-</strong>${data.created}</p>
          <p class="card-text" id="post-detail-body">${data.body}</p>
        </div>
      </div>
        `
        postTitle.value = data.title;
        postBody.value = data.body;
    },
    error: function (error){
        console.log(error);
    }
});

formUpdate.addEventListener('submit', e=>{
    e.preventDefault();
    detailtitle = document.getElementById('post-detail-title')
    detailbody = document.getElementById('post-detail-body')
    $.ajax({
        type: 'POST',
        url: urlUpdate,
        data: {
            'csrfmiddlewaretoken':postUpdateCsrf[0].value,
            'title':postTitle.value,
            'body':postBody.value,
        },
        success: function(response){
            console.log(response)
            detailtitle.textContent = response.title
            detailbody.textContent = response.body
            handleAlerts('success','Post Updated Successfully')
        },
        error: function(error){
            console.log(error)
        },
    })
})

