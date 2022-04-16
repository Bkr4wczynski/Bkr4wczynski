function porownaj$liczby(){
    const first$num = parseFloat(document.getElementById("first_num").value);
    const second$num = parseFloat(document.getElementById("second_num").value);  
    let wynik = document.getElementById("wynik");                                                 
    if(!first$num || !second$num){
        alert("Podaj wszystkie liczby!");
    }
    else{
        if(first$num > second$num){
            wynik.innerHTML = (`Pierwsza liczba: ${first$num} jest większa o ${first$num - second$num} od drugiej liczby: ${second$num}`);
        }
        else if(first$num < second$num){
            wynik.innerHTML = (`Druga liczba: ${second$num} jest większa o ${second$num - first$num} od pierwszej liczby: ${first$num}`);
        }
        else{
            wynik.innerHTML = (`Te liczby czyli ${first$num} i ${second$num} są sobie równe!`)
        }
        
    }

}
