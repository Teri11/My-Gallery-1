
function imgWindow() {
  window.open("image")
}

const copy   = document.getElementById("copyButton");
const selection = window.getSelection();
const range = document.createRange();
const textToCopy = document.getElementById("copyUrl")

copy.addEventListener('click', function(e) {
    range.selectNodeContents(textToCopy);
    selection.removeAllRanges();
    selection.addRange(range);
    const successful = document.execCommand('copy');
    if(successful){
      alert('Phot URL Copied!') ;
    } else {
      alert('Unable to copy!');  
    }
    window.getSelection().removeAllRanges()
});
