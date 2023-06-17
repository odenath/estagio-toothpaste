// // validando os formulários

// const form = document.getElementById('form');
// const campos = document.querySelectorAll('.required');


// document.addEventListener('DOMContentLoaded', (event) => {
//     const form = document.getElementById('form');
//     const campos = document.querySelectorAll('#form input');

//     // Salvar dados do formulário ao enviar
//     form.addEventListener('submit', () => {
//         campos.forEach(campo => {
//             localStorage.setItem(campo.name, campo.value);
//         });
//     });

//     // Carregar dados do formulário ao carregar a página
//     window.addEventListener('load', () => {
//         campos.forEach(campo => {
//             const valorSalvo = sessionStorage.getItem(campo.name);
//             if (valorSalvo) {
//                 campo.value = valorSalvo;
//             }
//         });
//     });
// });

document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('form');
    const campos = document.querySelectorAll('#form input, #form select');


    // Salvar dados do formulário quando qualquer campo é alterado
    campos.forEach(campo => {
        campo.addEventListener('input', () => {
            sessionStorage.setItem(campo.name, campo.value);
        });
    });

    // Carregar dados do formulário ao carregar a página
    window.addEventListener('load', () => {
        campos.forEach(campo => {
            // const valorSalvo = localStorage.getItem(campo.name);
            const valorSalvo = sessionStorage.getItem(campo.name);
            if (valorSalvo) {
                campo.value = valorSalvo;
            }
        });
    });
});




























// formatando o telefone
// document.getElementById('cellhpone').addEventListener('input', function (e) {
//     var target = e.target, position = target.selectionEnd, length = target.value.length;
    
//     target.value = target.value.replace(/\D/g, '').replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');

//     if(position !== length) {
//         if(e.data && /\D/g.test(e.data)) {
//             target.selectionStart = position;
//             target.selectionEnd = position;
//         } else {
//             target.selectionStart = position - 1;
//             target.selectionEnd = position - 1;
//         }
//     }
// });