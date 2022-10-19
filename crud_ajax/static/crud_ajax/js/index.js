const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBtn = document.getElementById('end-box')
let visible = 3
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
              <a href="#" class="btn btn-outline-secondary">Detail</a>
              <a href="#" class="btn btn-outline-primary">Like</a>
            </div>
            <div class="card-footer text-muted">
              ${el.created}
            </div>
          </div>
            `
        });
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

getData()
loadBtn.addEventListener('click', ()=>{
  spinnerBox.classList.remove('not-visible')
  visible += 3
  getData()
})

