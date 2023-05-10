
type.onchange = () => {
    var type = document.getElementById("type");
    var tariff = document.getElementById("tariff");
    type = type.value;
    fetch("http://127.0.0.1:5000/get/tariffs").then((response) =>{
        response.json().then((data) =>{
            optionHTML = '<option disabled selected value> -- Выберите тариф -- </option>';
            for(tariff of data){
                if(tariff.type == type){
                    optionHTML += '<option value="' + tariff.id + '">' + tariff.name + '</option>';
                }
            }
            document.getElementById("tariff").innerHTML = optionHTML;
        });
    });
}; 