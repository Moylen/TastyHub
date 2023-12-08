let myToast = document.getElementById('myToast');

if (myToast) {
    window.onload = function () {
        let myToast = document.getElementById('myToast');
        let bsToast = new bootstrap.Toast(myToast);
        bsToast.show();
    };
}