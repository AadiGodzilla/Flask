const search = () => {
    const searchbox = document.getElementById('search').value.toUpperCase();
    const product = document.querySelectorAll('.products');
    const pname = document.getElementsByTagName('h3');

    for (var i = 0; i < pname.length; i++) {
        let match = product[i].getElementsByTagName('h3')[0];
        
        if (match) {
            let textvalue = match.textContent || match.innerHTML

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                product[i].style.display = "";
            }
            else {
                product[i].style.display = "none";
            }
        }
    }
}

let search_box = document.getElementById('search')

search_box.addEventListener('keyup', (e) => {
    if (e.keyCode === 13) {
        search();
    }
})