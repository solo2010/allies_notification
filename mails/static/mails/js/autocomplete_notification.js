$(document).ready(function(){
    let tagify = new Tagify(document.querySelector("#recipients"), {tagTextProp: "name"});
    $('#product, #status').change(function(){
        let product = $('#product').val();
        let status = $('#status').val();
        let status_name = $('#status option:selected').text();
        
        if(status_name == "En Mantenimiento") { //Status 4 es en mantenimiento
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
                        tagify.removeAllTags();
                        let tags = data.to.map(function(item){
                            return {
                                value: item.id,
                                name: item.name
                            }
                        });
                        tagify.addTags(tags);
                    }
                }
            })
        }
    });
    $('#start_date').on("change", function(){
        let old_content = $('#content').val(); 
        let star_date = $(this).val();
        let content = old_content.replace(/Fecha inicio:.*/, "Fecha inicio: " + star_date);
        $('#content').val(content);
    });

    $('#end_date').on("change", function(){
        let old_content = $('#content').val();
        let end_date = $(this).val();
        let content = old_content.replace(/Fecha fin:.*/, "Fecha fin: " + end_date);
        $('#content').val(content);

    })
});