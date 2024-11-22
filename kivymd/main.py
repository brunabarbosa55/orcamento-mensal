# Importando as bibliotecas necessárias do KivyMD
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

# ajustar o tamanho da janela
class ManipulaJanela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        Window.size = (self.largura, self.altura)


# classe do MDApp
class OrçamentoApp(MDApp):
    def build(self):
        manipulador = ManipulaJanela(400, 700)
        manipulador.ajustar_tamanho_janela()

        #layout vertical para organizar os elementos na tela
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # texto dos valores dos gastos
        self.gasto_aluguel = MDTextField(
            hint_text="Gasto com Aluguel",  #dica para o usuário
            input_filter="float"  # só números decimais
        )
        self.gasto_alimentacao = MDTextField(
            hint_text="Gasto com Alimentação",
            input_filter="float"
        )
        self.gasto_transporte = MDTextField(
            hint_text="Gasto com Transporte",
            input_filter="float"
        )
        self.gasto_outros = MDTextField(
            hint_text="Outros Gastos",
            input_filter="float"
        )

        # texto para definir o orçamento mensal
        self.orcamento_total = MDTextField(
            hint_text="Meta de Orçamento Mensal",
            input_filter="float"
        )

        # botão calcula orçamento
        botao_calcular = MDRaisedButton(
            text="Calcular Orçamento",
            on_release=self.calcular_orcamento  
        )

        # resultado do calculo
        self.resultado = MDLabel(
            text="Resultado: ",  
            halign="center" 
        )

        # widgets do layout
        layout.add_widget(self.gasto_aluguel)
        layout.add_widget(self.gasto_alimentacao)
        layout.add_widget(self.gasto_transporte)
        layout.add_widget(self.gasto_outros)
        layout.add_widget(self.orcamento_total)
        layout.add_widget(botao_calcular)
        layout.add_widget(self.resultado)

        # exibe layout 
        return layout

    # ao clicar no botão ele calcula Orçamento
    def calcular_orcamento(self, instance):
        try:
            # Converte os valores digitados em numeros
            aluguel = float(self.gasto_aluguel.text)
            alimentacao = float(self.gasto_alimentacao.text)
            transporte = float(self.gasto_transporte.text)
            outros = float(self.gasto_outros.text)
            orcamento = float(self.orcamento_total.text)

            # calcula o total de gastos somando todas as categorias
            total_gastos = aluguel + alimentacao + transporte + outros

            # compara o total de gastos com a meta de orçamento definida
            if total_gastos > orcamento:
                # se os gastos ultrapassarem o orçamento, mostrar mensagem 
                resultado = f"Orçamento estourado! Total: R${total_gastos:.2f}, Meta: R${orcamento:.2f}"
            else:
                # se nao, indicar que está dentro do orçamento
                resultado = f"Orçamento dentro do limite. Total: R${total_gastos:.2f}, Meta: R${orcamento:.2f}"

            # atualiza o texto com o resultado do calculo
            self.resultado.text = f"Resultado: {resultado}"
        except ValueError:
            # se der valor invalido, mostrar mensagem
            self.resultado.text = "Por favor, insira valores válidos."


#executar
OrçamentoApp().run()