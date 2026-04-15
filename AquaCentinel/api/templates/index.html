<x-app-layout>
    <div class="py-8">
        <!-- Header Section -->
        <div class="mb-8">
            <h1 class="text-3xl font-bold text-blue-900 mb-2">Mis Boyas Inteligentes</h1>
            <p class="text-gray-600 text-lg">Gestiona y monitorea todas tus boyas AquaSentinel en un solo lugar</p>
        </div>

        <!-- Grid de Boyas -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 mb-12">
            @forelse ($misboyas as $boya)
                <div class="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <!-- Header de la Boya -->
                    <div class="bg-gradient-to-r from-blue-600 to-blue-700 px-6 py-4">
                        <div class="flex justify-between items-start">
                            <h4 class="text-xl font-bold text-white">{{ $boya->nombre }}</h4>
                            <span class="bg-white bg-opacity-20 text-white text-xs font-semibold px-3 py-1 rounded-full">
                                Activa
                            </span>
                        </div>
                        <p class="text-blue-100 text-sm mt-1">Modelo: {{ $boya->modelo }}</p>
                    </div>

                    <!-- Contenido de la Boya -->
                    <div class="p-6">
                        <!-- Estado de la Boya -->
                        <div class="flex items-center mb-4">
                            <div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
                            <span class="text-sm font-medium text-gray-700">En línea</span>
                        </div>

                        <!-- Información de Mantenimiento -->
                        <div class="space-y-3">
                            <div>
                                <p class="text-sm text-gray-500 mb-1">Último mantenimiento</p>
                                <div class="flex items-center">
                                    <i class="fas fa-calendar-alt text-blue-500 mr-2"></i>
                                    <p class="text-gray-800 font-semibold">{{ $boya->fecha_mantenimiento }}</p>
                                </div>
                            </div>

                            <!-- Indicadores de Estado (opcional) -->
                            <div class="grid grid-cols-2 gap-3 pt-3 border-t border-gray-100">
                                <div class="text-center">
                                    <div class="text-lg font-bold text-blue-600">7.2</div>
                                    <div class="text-xs text-gray-500">pH</div>
                                </div>
                                <div class="text-center">
                                    <div class="text-lg font-bold text-green-600">25°C</div>
                                    <div class="text-xs text-gray-500">Temp</div>
                                </div>
                            </div>
                        </div>

                        <!-- Acciones -->
                        <div class="mt-6 flex space-x-3">
                            <a href="{{ route('boya.show', $boya->id) }}"
                               class="flex-1 bg-blue-600 hover:bg-blue-700 text-white text-center font-semibold px-4 py-3 rounded-lg transition-all duration-200 transform hover:scale-105 shadow-md hover:shadow-lg">
                                <i class="fas fa-chart-line mr-2"></i>
                                Ver Dashboard
                            </a>
                            <button class="bg-gray-100 hover:bg-gray-200 text-gray-700 p-3 rounded-lg transition-colors duration-200">
                                <i class="fas fa-cog"></i>
                            </button>
                        </div>
                    </div>
                </div>
            @empty
                <!-- Estado Vacío -->
                <div class="col-span-full">
                    <div class="bg-white rounded-2xl shadow-lg border-2 border-dashed border-gray-200 p-12 text-center">
                        <div class="w-24 h-24 mx-auto mb-6 bg-blue-50 rounded-full flex items-center justify-center">
                            <i class="fas fa-water text-blue-500 text-3xl"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-gray-800 mb-3">No tienes boyas registradas</h3>
                        <p class="text-gray-600 mb-8 max-w-md mx-auto">
                            Comienza agregando tu primera boya inteligente para monitorear la calidad del agua en tiempo real.
                        </p>
                        <button class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-lg shadow-md transition-all duration-200 transform hover:scale-105">
                            <i class="fas fa-plus mr-2"></i>
                            Agregar Primera Boya
                        </button>
                    </div>
                </div>
            @endforelse
        </div>

        <!-- Sección de Sincronización -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden">
            <!-- Header -->
            <div class="bg-gradient-to-r from-blue-50 to-blue-100 px-8 py-6 border-b border-blue-200">
                <div class="flex items-center">
                    <div class="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center mr-4">
                        <i class="fas fa-link text-white text-xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-blue-900">Sincronizar Nueva Boya</h3>
                        <p class="text-blue-700">Vincula una nueva boya a tu cuenta usando el código único</p>
                    </div>
                </div>
            </div>

            <!-- Contenido del Formulario -->
            <div class="p-8">
                <!-- Mensajes de Estado -->
                @if (session('success'))
                    <div class="bg-green-50 border border-green-200 rounded-xl p-4 mb-6 flex items-center">
                        <i class="fas fa-check-circle text-green-500 text-xl mr-3"></i>
                        <div>
                            <p class="text-green-800 font-semibold">¡Éxito!</p>
                            <p class="text-green-700 text-sm">{{ session('success') }}</p>
                        </div>
                    </div>
                @endif

                @if (session('error'))
                    <div class="bg-red-50 border border-red-200 rounded-xl p-4 mb-6 flex items-center">
                        <i class="fas fa-exclamation-triangle text-red-500 text-xl mr-3"></i>
                        <div>
                            <p class="text-red-800 font-semibold">Error</p>
                            <p class="text-red-700 text-sm">{{ session('error') }}</p>
                        </div>
                    </div>
                @endif

                <!-- Formulario -->
                <form action="" method="POST" class="space-y-6 max-w-2xl">
                    @csrf

                    <!-- Campo de Código -->
                    <div>
                        <label for="codigo_boya" class="block text-gray-700 font-semibold mb-3 text-lg">
                            <i class="fas fa-qrcode mr-2 text-blue-500"></i>
                            Código de la Boya
                        </label>
                        <div class="relative">
                            <input type="text" 
                                   name="codigo_boya" 
                                   id="codigo_boya"
                                   placeholder="Ejemplo: BYA-2025-XYZ-123"
                                   class="w-full border-2 border-gray-200 rounded-xl px-5 py-4 text-gray-800 placeholder-gray-400 focus:outline-none focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all duration-200 text-lg"
                                   required>
                            <div class="absolute right-3 top-1/2 transform -translate-y-1/2">
                                <i class="fas fa-key text-gray-400"></i>
                            </div>
                        </div>
                        <p class="text-gray-500 text-sm mt-2 flex items-center">
                            <i class="fas fa-info-circle mr-2 text-blue-500"></i>
                            Encuentra este código en la etiqueta de tu boya o en la documentación
                        </p>
                    </div>

                    <!-- Acciones -->
                    <div class="flex flex-col sm:flex-row gap-4 pt-4">
                        <button type="submit"
                                class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-4 rounded-xl shadow-lg transition-all duration-200 transform hover:scale-105 flex items-center justify-center">
                            <i class="fas fa-sync-alt mr-3"></i>
                            Sincronizar Boya
                        </button>
                        
                        <button type="button"
                                class="bg-gray-100 hover:bg-gray-200 text-gray-700 font-semibold px-8 py-4 rounded-xl transition-all duration-200 flex items-center justify-center">
                            <i class="fas fa-question-circle mr-3"></i>
                            ¿Dónde encuentro el código?
                        </button>
                    </div>
                </form>

                <!-- Información Adicional -->
                <div class="mt-8 pt-8 border-t border-gray-200">
                    <h4 class="text-lg font-semibold text-gray-800 mb-4 flex items-center">
                        <i class="fas fa-lightbulb mr-2 text-yellow-500"></i>
                        Consejos para la sincronización
                    </h4>
                    <div class="grid md:grid-cols-2 gap-4 text-sm text-gray-600">
                        <div class="flex items-start">
                            <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                            <span>Asegúrate de que la boya esté encendida y en modo de emparejamiento</span>
                        </div>
                        <div class="flex items-start">
                            <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                            <span>Verifica que el código no contenga espacios ni caracteres especiales</span>
                        </div>
                        <div class="flex items-start">
                            <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                            <span>La boya debe estar dentro del rango de conexión WiFi</span>
                        </div>
                        <div class="flex items-start">
                            <i class="fas fa-check-circle text-green-500 mt-1 mr-3"></i>
                            <span>Si tienes problemas, reinicia la boya y vuelve a intentarlo</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <style>
        /* Estilos adicionales para mejorar la visualización */
        .card-hover {
            transition: all 0.3s ease;
        }
        
        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .gradient-border {
            position: relative;
        }
        
        .gradient-border::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #0A75D1, #084B8A);
            border-radius: 8px 8px 0 0;
        }
    </style>
</x-app-layout>