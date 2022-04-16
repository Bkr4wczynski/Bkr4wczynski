function oblicz(operator){
    const first_num = parseFloat(document.getElementById("first_num").value);
    const second_num = parseFloat(document.getElementById("second_num").value);
    const wynik = document.getElementById("wynik");
    if(!first_num || !second_num){
        alert("Podaj wszystkie liczby!");
    }
    else{
        if(operator == '+'){
            wynik.innerHTML = first_num + second_num;
        }
        else if(operator == '-'){
            wynik.innerHTML = first_num - second_num;
        }
        else if(operator == '*'){
            wynik.innerHTML = first_num * second_num;
        }
        else if(operator == '/'){
            wynik.innerHTML = first_num / second_num;
        }
    }
}
