// Função para controlar campo de telefone
var SPMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};

// Função para implementar máscaras em formulário
$(function(){
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
//    $('.mask-tel').mask('(00) 0000-0000');
    $('.mask-tel').mask(SPMaskBehavior, spOptions);
});