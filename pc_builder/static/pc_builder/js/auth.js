const elts = document.querySelectorAll('[data-login-required]');

function handleClick(e){
  if(!isAuthenticated) {
    e.preventDefault();
    alert('로그인해주세요.');
  }
}

for (let elt of elts){
  elt.addEventListener('click', handleClick)
}