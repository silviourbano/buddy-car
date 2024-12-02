# Buddy Car Project

Este projeto implementa um simulador de carro autônomo usando aprendizado por reforço com **Kivy**, **PyTorch** e **OpenGL**.

## Pré-requisitos

Certifique-se de ter os seguintes componentes instalados:

1. **Python 3.11 ou superior**
2. **Dependências do sistema**:
   - SDL2
   - Mesa (para OpenGL)
   - Outros utilitários gráficos

### Instalação no Ubuntu

Execute os comandos abaixo para garantir que as dependências estão instaladas:

```bash
sudo apt update
sudo apt install -y     python3 python3-pip python3-venv     libgl1-mesa-dri libgl1-mesa-glx mesa-utils     libsdl2-2.0-0 libsdl2-dev     libglew2.2 libglew-dev     libegl1-mesa-dev
```

## Configurando o Ambiente Python

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv kivy_env
   source kivy_env/bin/activate
   ```

2. Instale as dependências do Python:
   ```bash
   pip install --upgrade pip
   pip install kivy[full] torch numpy matplotlib
   ```

## Problema Conhecido: Carregamento de `libstdc++.so.6`

Durante a execução, o projeto pode encontrar problemas relacionados ao OpenGL, como:

```
libGL error: MESA-LOADER: failed to open iris: ...
X Error of failed request:  BadValue ...
```

Para resolver, localize a biblioteca `libstdc++.so.6`:

```bash
find / -name libstdc++.so.6 2>/dev/null
```

Use o caminho encontrado para exportar a variável `LD_PRELOAD` antes de executar o projeto:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
```

Adicione ao seu script ou shell para evitar problemas futuros.

## Executando o Projeto

1. Ative o ambiente virtual:
   ```bash
   source kivy_env/bin/activate
   ```

2. Export a variável necessária:
   ```bash
   export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
   ```

3. Execute o simulador:
   ```bash
   python map.py
   ```

Se tudo estiver configurado corretamente, o simulador será iniciado.

## Testando o Ambiente

Você pode verificar o funcionamento do Kivy com o seguinte script de teste:

```python
import kivy
from kivy.app import App
from kivy.uix.button import Button

kivy.logger.Logger.setLevel('DEBUG')

class TestApp(App):
    def build(self):
        return Button(text="Hello, Kivy!")

if __name__ == '__main__':
    TestApp().run()
```

## Solução Permanente

Se precisar rodar o projeto sem configurar manualmente o `LD_PRELOAD` toda vez, adicione a linha abaixo ao arquivo `~/.bashrc`:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
```

Atualize o terminal:
```bash
source ~/.bashrc
```

## Problemas Comuns

### OpenGL Não Funciona
Use `glxgears` para verificar:
```bash
sudo apt install mesa-utils
glxgears
```

Se falhar, reinstale os drivers do Mesa:
```bash
sudo apt install --reinstall libgl1-mesa-dri libgl1-mesa-glx
```

### Xorg vs Wayland
Certifique-se de estar usando **Xorg**. Na tela de login, selecione **Ubuntu on Xorg**.

## Contribuições

Se precisar de ajuda ou deseja contribuir, por favor, envie um PR ou abra uma issue no repositório.

---

Feito com ❤️ por Silvio e Sofia.