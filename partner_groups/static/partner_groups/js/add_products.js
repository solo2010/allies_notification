$(document).ready(function() {

    //En esta parte guardamos la lista de los productos que hay en el select oculto
    let producsList = []
    $(".template-select-product option").each(function() {
        let val = $(this).val();
        let text = $(this).text();
        if (val !== "") {
            producsList.push({ id: val, title: text});
        }
    });

    //Creamos la función que actualizará la lista del select según los productos ya escogidos (Esto para que cada vez que escoja un producto desaparezca de la lista y no repetir)
    function updateOptions() {

        let selects = $(".select-product").map(function () {
            return $(this).val();
        }).get();

        $(".select-product").each(function() {
            let actualSelect = $(this);
            let actualValue = actualSelect.val();

            //Limpiamos la lista de opciones del select
            actualSelect.html('<option value="">Seleccione un producto</option>');

            //Agregamos las opciones disponibles
            producsList.forEach(product => {
                if (product.id === actualValue || !selects.includes(product.id)) {
                    actualSelect.append(
                        `<option value="${product.id}">${product.title}</option>`
                    );
                }
            })
            //Volvemos a seleccionar la opción original
            actualSelect.val(actualValue);
        });
    }

    //Al cambiar  cualquier select, actualiza la lista
    $(document).on("change", ".select-product", function () {
        updateOptions();
    });

    //Agregar nuevo select al formulario create de partner groups y actualizamos la lista con el updateSelects
    $("#btn-add").click(function(){
        let newSelect =  $(".template-select-product").html();
        $("#products-container").append(newSelect);
        updateOptions();
    });

    $(document).on("click", ".btn-remove", function(){
        $(this).parent().remove();
        updateOptions();
    });
});