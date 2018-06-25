$(function() {
    $('#result').hide();
    // Enviando criação da instancia
    $('#create_instance').on('submit', function(event){
        event.preventDefault();
        var tenant_name = $('#id_subdomain').val();
        var email = $('#id_email').val();
        var password = $('#id_password').val();
        var name_fantasy = $('#id_name_fantasy').val();
        $.ajax({
        type: "POST",
        url: '{% url "tenant:register" %}',
        beforeSend: function () {
            // chamada para o loader
            $("#loader").show();
            $(".overlay").css("background-image",
                "url(https://i.stack.imgur.com/8t6P3.gif)",
                );
         },
        data: {
          'tenant_name': tenant_name,
          'email': email,
          'password': password,
          'name_fantasy': name_fantasy,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: 'json',
        success: function (response) {
          $("#loader").hide();
          if (response.tenant_exist == true) {
            $('#create_instance').hide('slow');
            $('#result').show().fadeIn(500).delay(5000);
            $('#result').append('<a href="http://'+ response.url_login_new_schema + ' " class="btn btn-success" id="access_instance">{% trans 'Acessar instância' %}</a>');
          }
          else{
            $("#loader").hide();
            $('#create_instance').show();
            $('#result').hide();
            $('#response_get_subdomin').css('color', 'blue');
            $('#response_get_subdomin').html('<strong>Ocorreu algo estranho ao buscar seu domínio, por favor confirme!</strong>');
          }
        }
      });
    });


    // Busca subdomain
    $("#loader").hide();
    $("#id_subdomain").change(function () {
      var subdomain = "atrix_" + $(this).val();
      $.ajax({
        url: '{% url "tenant:validate_tenant" %}',
        beforeSend: function () {
            // chamada para o loader
            $("#loader").show();
            $(".overlay").css("background-image",
                "url(https://i.stack.imgur.com/8t6P3.gif)",
                );
         },
        data: {
          'subdomain': subdomain
        },
        dataType: 'json',
        success: function (data) {
          $("#loader").hide();
          if (data.exist == true) {
            $('#response_get_subdomin').css('color', 'red');
            $('#response_get_subdomin').html('<strong>Este dominío já existe. Por favor escolha outro endereço!</strong>');
          }else if(data.exist == false){
            $('#response_get_subdomin').css('color', 'green');
            $('#response_get_subdomin').html('<strong>Domínio disponível para uso!</strong>');
          }
          else{
            $('#response_get_subdomin').css('color', 'blue');
            $('#response_get_subdomin').html('<strong>Ocorreu algo estranho ao buscar seu domínio, por favor confirme!</strong>');
          }
        }
      });
    });
    });