// setting link active
// const activePage = window.location.pathname;
// const links = document.querySelectorAll('nav a').forEach(link => {
//         if (link.href.includes(`${activePage}`)) {
//             link.classList.add('active');
//         }
//     })

document.querySelectorAll('.nav-link').forEach(link => {
    if (link.href === window.location.href) {
        link.setAttribute('aria-current', 'page')
    }
})

// function clickLinkA(li) {
//     items = document.querySelectorAll('.list.active');

//     if (items.length > 0) {
//         items[0].classList.remove('active');
//     }

//     li.classList.add('list', 'active');
// }