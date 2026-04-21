    //Script para gestionar la conexión a websockets
    //Se agrega esto para que no se corrompa en produccion
    const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';

    const chatSocket = new WebSocket(
        protocol + window.location.host + '/ws/chat/' + ID + '/'
    );

    const transmision_status = document.getElementById('transmision_status');
    chatSocket.onclose = function(e) {
        transmision_status.classList.remove('bg-success-subtle', 'text-success', 'border-success-subtle')
        transmision_status.classList.add('bg-danger-subtle', 'text-danger', 'border-danger-subtle')
        transmision_status.innerHTML = '<i class="fas fa-circle me-2 animate-pulse"></i> Sin conexión'
        console.error('Chat socket cerrado inesperadamente');
    };

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log("Mensaje recibido: ", data);

        // 1. Actualiza gráficas y diagnóstico (lo que ya tenías)
        updateChartsData(data.registro);
        showDiagnostic(data.registro, data.diagnostico);

        // 2. ACTUALIZAR TABLA HISTÓRICA EN VIVO
        // Agregamos el nuevo registro al inicio de nuestra lista maestra
        allItems.unshift(data.registro);

        // Verificamos si el dato nuevo debe mostrarse según el filtro actual
        const filtroActual = document.getElementById('filter-date').value;
        const fechaReg = new Date(data.registro.fecha_creacion);
        const fechaLocalStr = `${fechaReg.getFullYear()}-${String(fechaReg.getMonth() + 1).padStart(2, '0')}-${String(fechaReg.getDate()).padStart(2, '0')}`;

        if (!filtroActual || filtroActual === fechaLocalStr) {
            // Si coincide con el filtro (o no hay filtro), lo metemos a la lista filtrada
            filteredItems.unshift(data.registro);
            // Volvemos a renderizar para que aparezca en la página 1
            renderTable();
        }
    };
