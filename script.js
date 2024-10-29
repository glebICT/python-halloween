const codeElements = document.querySelectorAll('code');

codeElements.forEach((element) => {
    element.addEventListener('copy', (event) => {
        event.preventDefault();
    }
)   
});
