function myAnalyser() {
    // document.querySelector('.main ').style.display = 'none';

    document.querySelector('.main').classList.add('spinner-border');

    setTimeout(() => {
        document.querySelector('.main').classList.remove('spinner-border');

        document.querySelector('.main ').style.display = 'block';
    }, 10000);
}
