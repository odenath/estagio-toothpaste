document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('form');
    const campos = document.querySelectorAll('#form input, #form select');
	const erros = document.getElementById('erros');

	form.addEventListener('submit', (e) => {
		// Salvar dados do formulário quando qualquer campo é alterado
		campos.forEach(campo => {
			if (campo.type === 'radio') {
				// Para botões de opção, salvar o valor do botão selecionado
				if (campo.checked) {
					sessionStorage.setItem("CADASTRO_CLIENTE_" + campo.name, campo.value);
				}
			} else {
				sessionStorage.setItem("CADASTRO_CLIENTE_" + campo.name, campo.value);
			}
		});
	});

    // Carregar dados do formulário ao carregar a página
    if(erros) {
        campos.forEach(campo => {
            const valorSalvo = sessionStorage.getItem("CADASTRO_CLIENTE_" + campo.name);
            if (valorSalvo) {
                if (campo.type === 'radio') {
                    // Para botões de opção, marcar o botão cujo valor foi salvo
                    if (campo.value === valorSalvo) {
                        campo.checked = true;
                    }
                } else {
                    campo.value = valorSalvo;
                }
            }
        });
	}
});