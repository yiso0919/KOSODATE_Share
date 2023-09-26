function char_check (){
    let textElement = document.getElementById("limit_check");
    let errorMessageElement = document.getElementById("errorMessage");
    let text = textElement.value;
    console.log(text.length);
    if(text.length>30) {
        errorMessageElement.textContent = "タイトルは30文字以内にしてください";
    }
    else if(text.length==0){
        errorMessageElement.textContent = "タイトルを入力してください";
    }
    else{
        errorMessageElement.textContent = "";
    }
}
