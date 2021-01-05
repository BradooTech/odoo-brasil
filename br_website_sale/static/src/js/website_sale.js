odoo.define('br_website_sale.address', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    function cnpj_cpf_mask () {
        var company = $('#radioCompany').prop('checked');
        if (company) {
            $('input[type=text][name=cnpj_cpf]').mask('00.000.000/0000-00');
            $('label[for=contact_name]').text('CNPJ');
        } else {
            $('input[type=text][name=cnpj_cpf]').mask('000.000.000-00');
            $('label[for=contact_name]').text('CPF');
        }
    }

    $(document).ready(function () {
        var SPMaskBehavior = function (val) {
            return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' :
                '(00) 0000-00009';
        },
        spOptions = {
            onKeyPress: function (val, e, field, options) {
                field.mask(SPMaskBehavior.apply({},
                            arguments), options);
            }
        };
        $('#select_state_id').trigger('change');
        $('input[type=text][name=zip]').mask('00000-000');

        $('#id_country').change(function () {
            var vals = {country_id: $(this).val()};
            ajax.jsonRpc("/shop/get_states", 'call', vals)
                .then(function (data) {
                    var selected = parseInt($('#input_state_id').val());
                    $('#select_state_id').find('option').remove().end();
                    $('#select_state_id').append(
                        '<option value="">Estado...</option>');
                    $.each(data, function (i, item) {
                        $('#select_state_id').append($('<option>', {
                            value: item[0],
                            text: item[1],
                            selected: item[0]===selected?true:false,
                        }));
                    });
                    $('#select_state_id').trigger('change');
                });
        });

        cnpj_cpf_mask();

        $('#select_state_id').change(function () {
            var vals = { state_id: $(this).val() };
            ajax.jsonRpc("/shop/get_cities", 'call', vals)
                .then(function (data) {
                    var selected = parseInt($('#input_city_id').val());
                    $('#select_city_id').find('option').remove().end();
                    $('#select_city_id').append(
                        '<option value="">Cidade...</option>');
                    $.each(data, function (i, item) {
                        $('#select_city_id').append($('<option>', {
                            value: item[0],
                            text: item[1],
                            selected: item[0]===selected?true:false,
                        }));
                    });
                });
        });

        $('#btn_search_zip').click(function () {
            var vals = {zip: $('input[name="zip"]').val()};
            ajax.jsonRpc("/shop/zip_search", 'call', vals)
                .then(function(data) {
                    if (data.sucesso) {
                        $('#input_state_id').val(data.state_id);
                        $('#input_city_id').val(data.city_id);
                        $('input[name="district"]').val(data.district);
                        $('input[name="street"]').val(data.street);
                        $('select[name="country_id"]').val(data.country_id);
                        $('select[name="country_id"]').change();
                        $('select[name="state_id"]').val(data.state_id);
                    } else {
                        alert('Nenhum cep encontrado');
                    }
                }
            );
        });   
        
        $('#btn_search_cnpj').click(function () {
            var vals = {cnpj_cpf: $('input[name="cnpj_cpf"]').val()};
            ajax.jsonRpc("/shop/cnpj_search", 'call', vals)
                .then(function(data) {
                    if (data.sucesso) {
                        console.log(data.name)
                        $('#input_state_id').val(data.state_id);
                        $('#input_city_id').val(data.city_id);
                        $('input[name="district"]').val(data.district);
                        $('input[name="street"]').val(data.street);
                        $('input[name="street2"]').val(data.street2);
                        $('select[name="country_id"]').val(data.country_id);
                        $('select[name="country_id"]').change();
                        $('select[name="state_id"]').val(data.state_id);
                        $('input[name="name"]').val(data.name);
                        $('input[name="phone"]').val(data.phone);
                        $('input[name="number"]').val(data.number);
                        $('input[name="zip"]').val(data.zip);
                    } else {
                        alert('CNPJ não encontrado');
                    }
                }
            );
        });

        $('#select_state_id').trigger('change');
        $('input[name="phone"]').mask(SPMaskBehavior, spOptions);

        $('input[type=radio][name=company_type]').change(function () {
            cnpj_cpf_mask();
        });
    });
});
