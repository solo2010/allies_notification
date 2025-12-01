$(document).ready(function(){
    $('#product, #status').change(function(){
        var product = $('#product').val();
        var status = $('#status').val();
        if(status == 4) { //Status 4 es en mantenimiento
            $('#date_maintenance').css("display", "flex");
        }
        else {
            $('#date_maintenance').css("display", "none");
        }

        if(product && status) {
            $.ajax({
                url: 'get_templates',
                data: {
                    'product': product,
                    'status': status,
                },
                success: function(data){
                    if(data.product && data.subject && data.content && data.to){
                        let subject = data.subject + " - " + data.product;
                        $('#subject').val(subject);
                        let content = data.content.replace("###", data.product); //Reemplazamos los ### del contenido por el nombre del producto
                        $('#content').val(content);
                    }
                }
            })
        }
    });
    $('#start_date').on("change", function(){
        let star_date = $(this).val();
        let content = data.content.replace(/Fecha inicio: .*/, "Fecha inicio: " + star_date);
        $('#content').val(content);
    });

    $('#end_date').on("change", function(){
        let end_date = $(this).val();
        let content = $('#content').replace(/Fecha fin: .*/, "Fecha fin: " + end_date);
        $('#content').val(content);

    })
});